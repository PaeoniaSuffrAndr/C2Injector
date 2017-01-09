#!/usr/bin/python
# coding=utf8

from multiprocessing import Process, Queue
from time import sleep
import ftplib
import os
import signal
import socket
import sys
import threading
import time
import traceback

import MySQLdb


MGFTPURL = "ftp://gdyd:XqUrM8Gos2Ck@175.6.15.94:21"
WEFTPURL = "ftp://gdydott:mangguo123@183.235.21.141:21/update/"
DOWNLOADDIR = "/home/gdydott/update/"

# 日志文件
LOG = DOWNLOADDIR + "ftpdownload.log"

# 处理进程数
PROCESSNUM = 3

# 存放目录
SAVEDIR = "/"

global G_RUNFLAG
global ONLYDEL
G_RUNFLAG = True
ONLYDEL = False

# mysql info

DBIP = "127.0.0.1"
DBPort = 3306
DBName = "bledb"
DBUser = "bledb"
DBPW = "bledb"


class FtpObj(Process):

    class perTimer(threading.Thread):

        def __init__(self, interval, func):
            threading.Thread.__init__(self)
            self.interval = interval
            self.func = func

        def run(self):
            while True:
                sleep(self.interval)
                self.func()

    def __init__(self, taskQuery, resultQuery):
        Process.__init__(self)
        self.taskQ = taskQuery
        self.resultQ = resultQuery
        self.filePath = ""
        self.lock = None

    def setFilePath(self, filePath):
        self.lock.acquire()
        self.filePath = filePath
        self.lock.release()

    def getFilePath(self):
        self.lock.acquire()
        filePath = self.filePath
        self.lock.release()
        return filePath

    def checkFile(self):
        filePath = self.getFilePath()
        if os.path.exists(filePath):
            if time.time() - 180 > os.path.getmtime(filePath):
                # print "程序退出"
                os.kill(self.pid, 9)

    def downloadFile(self, ftpSerInfo, ftpFile, localPath, fileSize):
        try:
            curDownSize = 0
            if os.path.exists(localPath):
                curDownSize = os.path.getsize(localPath)
                if curDownSize == fileSize:
                    return True
                else:
                    try:
                        os.remove(localPath)
                    except:
                        pass

            if "ftp://" != ftpSerInfo[0:6]:
                return False

            temp = ftpSerInfo[6:].split('/')[0].split('@')
            userList = temp[0].split(':')
            serInfo = temp[1].split(':')
            ftpUser = userList[0]
            ftpPW = userList[1]
            ftpIP = serInfo[0]
            ftpPort = serInfo[1]

            localSaveDir = os.path.dirname(localPath)
            if not os.path.exists(localSaveDir):
                os.makedirs(localSaveDir)
        except:
            print traceback.format_exc()
            return False

        try:
            ftp = ftplib.FTP()
            try:
                ftp.connect(ftpIP, ftpPort)
                ftp.login(ftpUser, ftpPW)
                ftp.cwd(os.path.dirname(ftpFile).lstrip("/"))
                file_handler = open(localPath, 'wb')
            except:
                return False

            self.setFilePath(localPath)
            ftp.retrbinary('RETR %s' %
                           os.path.basename(ftpFile), file_handler.write)
            file_handler.close()
            ftp.quit()
            strTemp = localPath + ".bak"
            self.setFilePath(strTemp)
            if os.path.getsize(localPath) != fileSize:
                os.remove(localPath)
                print("verify file size failed.")
                return False
        except:
            print traceback.format_exc()
            file_handler.close()
            #print("Download file from ftp://%s:%s@%s:%s%s to local[%s] failed" % (ftpUser,ftpPW,ftpIP,ftpPort,ftpFile, localPath))
            try:
                os.remove(localPath)
            except:
                pass
            return False
        return True

    def deleteFile(self, filePath):
        try:
            os.remove(filePath)
        except:
            pass

        return True

    def run(self):
        self.lock = threading.Lock()
        chkTime = self.perTimer(3, self.checkFile)
        chkTime.start()
        while True:
            try:
                newTask = self.taskQ.get()
                if newTask["FLAG"] == 1:
                    tryNum = 0
                    while tryNum < 3:
                        if not self.downloadFile(newTask["FTPURL"], newTask["FTPFILE"], newTask["LOCALFILE"], newTask["FILESIZE"]):
                            newTask["RET"] = -1
                            tryNum += 1
                            sleep(5)
                        else:
                            newTask["RET"] = 0
                            break
                else:
                    if not self.deleteFile(newTask["LOCALFILE"]):
                        newTask["RET"] = -1
                    else:
                        newTask["RET"] = 0
                self.resultQ.put(newTask)
            except:
                print traceback.format_exc()
                pass
        return 0


def sig_kill(a, b):
    global G_RUNFLAG
    G_RUNFLAG = False


def initSignal():
    signal.signal(signal.SIGTERM, sig_kill)


def curDataTime():
    timeArray = time.localtime()
    return time.strftime("%Y%m%d", timeArray)


def curTime():
    timeArray = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


def connectDB():
    conn = MySQLdb.connect(
        host=DBIP,
        port=DBPort,
        user=DBUser,
        passwd=DBPW,
        db=DBName,
    )
    return conn


def getRecordFromDB():
    taskList = []
    try:
        conn = connectDB()
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        delFileSql = "SELECT A.ID, A.FILENAME,A.DOWNLOADSTATUS,A.STATUS,A.INITALTIME,A.FILESIZE FROM T_FILE A,T_CATEGORY B " \
            "WHERE A.ORIASSETID = B.ORIGINALID AND A.STATUS=6 OR A.STATUS=3 AND A.DOWNLOADSTATUS=2 AND A.ID>=27902 LIMIT 5"

        cur.execute(delFileSql)
        delkList = list(cur.fetchall())
        taskList.extend(delkList)

        global ONLYDEL
        if not ONLYDEL:

            # 下载检索算法
            downSql = "SELECT A.ID, A.FILENAME,A.DOWNLOADSTATUS,A.STATUS,A.INITALTIME,A.FILESIZE FROM T_FILE A,T_CATEGORY B,T_CLIP C "\
                      "WHERE  A.ORIASSETID = B.ORIGINALID AND A.ORIPARTID = C.ORIGINALID AND C.ORIASSETID=B.ORIGINALID "\
                      "AND A.FILEFORMATDESC >= 2 AND A.DOWNLOADSTATUS=1 AND A.ID>=27902 " \
                      "AND A.STATUS IN(1,2) ORDER BY A.ORIASSETID,C.SERIALNO LIMIT 3"

            cur.execute(downSql)
            downList = list(cur.fetchall())
            taskList.extend(downList)
    finally:
        cur.close()
        conn.close()
    return taskList


def updateRecordToDB(updateList, deleteList):
    try:
        conn = connectDB()
        cur = conn.cursor()
        for row in updateList:
            updateSql = "UPDATE T_FILE SET URLPREFIX='%s',DOWNLOADSTATUS=%d WHERE ID=%ld" % (
                row[0], row[2], row[1])
            cur.execute(updateSql)
            conn.commit()

        for ID in deleteList:
            delSql = "UPDATE T_FILE SET DOWNLOADSTATUS=3 WHERE ID=%d" % (ID)
            cur.execute(delSql)
            conn.commit()
    finally:
        cur.close()
        conn.close()
    return True


def getUsableSpace():
    # 保留25G空间
    disk = os.statvfs(SAVEDIR)
    val = disk.f_bsize * disk.f_bavail - 26843545600
    return val


def process():
    # multiprocessing.freeze_support()
    initSignal()

    global ONLYDEL

    # 检查磁盘空间
    if getUsableSpace() <= 0:
        print "磁盘空间不足25G，停止下载"
        return 0

    if not os.path.exists(DOWNLOADDIR):
        os.makedirs(DOWNLOADDIR)

    taskQueue = Queue(PROCESSNUM * 5)
    resultQueue = Queue(PROCESSNUM * 5)

    logFile = open(LOG, "a+")
    lastCheckProcess = time.time() + 100
    debugTime = lastCheckProcess
    curTask = 0

    proList = []
    for i in range(PROCESSNUM):
        proObj = FtpObj(taskQueue, resultQueue)
        proObj.daemon = True
        proObj.start()

        proList.append(proObj)

    totalRecord = {}
    while G_RUNFLAG:
        try:
            # 获取数据库记录
            if curTask <= 0:
                # 磁盘空间的计算方式，在获取一批任务后，获取实际的磁盘空间，再根据下载所需要的大小确认是否需要下载
                # 为了保证磁盘空间不会满，这里忽略对删除任务的磁盘空间调整
                curSpaceSize = getUsableSpace()
                # 检查磁盘空间，当空间足够时开启下载任务
                if ONLYDEL:
                    if curSpaceSize > 0:
                        ONLYDEL = False

                taskList = getRecordFromDB()
                logFile.write("Get Task, time=%s\n" % (curTime()))
                tempSize = 0
                for rowInfo in taskList:
                    # 根据记录下载或删除文件
                    inputTime = "%04d%02d%02d" % (
                        rowInfo["INITALTIME"].year, rowInfo["INITALTIME"].month, rowInfo["INITALTIME"].day)
                    savePath = DOWNLOADDIR + inputTime + rowInfo["FILENAME"]
                    newTask = {}
                    newTask["ID"] = rowInfo["ID"]
                    newTask["INPUTTIME"] = inputTime
                    newTask["FTPURL"] = MGFTPURL
                    newTask["FTPFILE"] = rowInfo["FILENAME"]
                    newTask["FILESIZE"] = rowInfo["FILESIZE"]
                    newTask["LOCALFILE"] = savePath
                    if rowInfo["DOWNLOADSTATUS"] == 1:
                        newTask["FLAG"] = 1
                        if curSpaceSize - newTask["FILESIZE"] < 0:
                            ONLYDEL = True
                            logFile.write(
                                "磁盘空间不足，最少保留15G, time=%s\n" % (curTime()))
                            break
                        else:
                            if newTask["ID"] in totalRecord.keys():
                                totalRecord[newTask["ID"]] += 1
                                if totalRecord[newTask["ID"]] > 3:
                                    #
                                    updateRecordToDB(
                                        [["", newTask["ID"], -1]], [])
                                    totalRecord.pop(newTask["ID"])
                                    continue
                            else:
                                totalRecord[newTask["ID"]] = 0
                            curSpaceSize -= newTask["FILESIZE"]
                    elif rowInfo["STATUS"] == 6:
                        newTask["FLAG"] = 0
                    else:
                        continue
                    taskQueue.put(newTask)
                    curTask = curTask + 1

            # 检查工作进程
            temp = time.time()
            if temp > lastCheckProcess:
                lastCheckProcess = temp + 90
                for pro in proList:
                    if pro.is_alive():
                        pass
                    else:
                        pro.join(3)
                        proList.remove(pro)
                        curTask = curTask - 1
                        proObj = FtpObj(taskQueue, resultQueue)
                        proObj.daemon = True
                        proObj.start()
                        proList.append(proObj)
                        break

            # 检查任务
            updateList = []
            deleteList = []
            while not resultQueue.empty():
                resultTask = resultQueue.get(False)

                curTask = curTask - 1
                if resultTask["ID"] in totalRecord.keys():
                    totalRecord.pop(resultTask["ID"])

                if resultTask["FLAG"] == 1:
                    if resultTask["RET"] == 0:
                        updateList.append(
                            [WEFTPURL + resultTask["INPUTTIME"], resultTask["ID"], 2])
                        logFile.write("DOWNLOAD OK:ftp=%s%s, ID=%d, time=%s\n" % (
                            resultTask["FTPURL"], resultTask["FTPFILE"], resultTask["ID"], curTime()))
                    else:
                        try:
                            os.remove(resultTask["LOCALFILE"])
                        except:
                            pass
                        updateList.append(
                            [WEFTPURL + resultTask["INPUTTIME"], resultTask["ID"], -1])
                        logFile.write("DOWNLOAD FAILED:ftp=%s%s,ID=%d, time=%s\n" % (
                            resultTask["FTPURL"], resultTask["FTPFILE"], resultTask["ID"], curTime()))
                elif resultTask["FLAG"] == 0:
                    deleteList.append(resultTask["ID"])
                    logFile.write("DEL OK:localFile=%s, ID=%d, time=%s\n" % (
                        resultTask["LOCALFILE"], rowInfo["ID"], curTime()))

            # 更新数据库记录
            updateRecordToDB(updateList, deleteList)

            if temp > debugTime:
                debugTime = temp + 60
                # logFile.write("curTaskSize=%d, info=%s" %
                #              (curTask, totalRecord))
            logFile.flush()
            time.sleep(1)
        except:
            print traceback.format_exc()
            time.sleep(10)

    for pro in proList:
        pro.terminate()
        pro.join()

    logFile.close()

if __name__ == "__main__":
    process()
