//
// 此文件是由 JavaTM Architecture for XML Binding (JAXB) 引用实现 v2.2.8-b130911.1802 生成的
// 请访问 <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a>
// 在重新编译源模式时, 对此文件的所有修改都将丢失。
// 生成时间: 2016.05.17 时间 05:02:00 PM CST
//

package com.miri.blephone.mediainjector.mgtv.api.category;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;

import com.miri.blephone.mediainjector.mgtv.api.Info;

/**
 * <p>
 * anonymous complex type的 Java 类。
 * <p>
 * 以下模式片段指定包含在此类中的预期内容。
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="assettype" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *         &lt;element name="assetdesc" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *         &lt;element name="assetoperation" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *         &lt;element name="content">
 *           &lt;complexType>
 *             &lt;complexContent>
 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                 &lt;sequence>
 *                   &lt;element name="assetid" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="originalid" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="baseId" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="assetpath" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="fstname" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="fstlvlid" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="extag" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="clipname" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="othernme" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="keyword" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="director" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="adaptor" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="leader" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="kind" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="area" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="language" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="caption" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="tags" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="story" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="awards" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="year" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="duration" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="updatetime" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="createtime" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="relasetime" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="playtime" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="inital" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="fullspell" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="simplespell" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="serialcount" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="productid" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="producername" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="channel" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="countrycode" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="canDown" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="filmorsingleset" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                   &lt;element name="periods" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="images">
 *                     &lt;complexType>
 *                       &lt;complexContent>
 *                         &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                           &lt;sequence>
 *                             &lt;element name="image" maxOccurs="unbounded" minOccurs="0">
 *                               &lt;complexType>
 *                                 &lt;complexContent>
 *                                   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                                     &lt;sequence>
 *                                       &lt;element name="imageid" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                                       &lt;element name="filename" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                                       &lt;element name="resolution" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                                       &lt;element name="imgtype" type="{http://www.w3.org/2001/XMLSchema}short"/>
 *                                       &lt;element name="filesize" type="{http://www.w3.org/2001/XMLSchema}int"/>
 *                                       &lt;element name="imghash" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                                     &lt;/sequence>
 *                                   &lt;/restriction>
 *                                 &lt;/complexContent>
 *                               &lt;/complexType>
 *                             &lt;/element>
 *                           &lt;/sequence>
 *                         &lt;/restriction>
 *                       &lt;/complexContent>
 *                     &lt;/complexType>
 *                   &lt;/element>
 *                 &lt;/sequence>
 *               &lt;/restriction>
 *             &lt;/complexContent>
 *           &lt;/complexType>
 *         &lt;/element>
 *         &lt;element name="info">
 *           &lt;complexType>
 *             &lt;complexContent>
 *               &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *                 &lt;sequence>
 *                   &lt;element name="pushcode" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="queuename" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                   &lt;element name="contentprovider" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *                 &lt;/sequence>
 *               &lt;/restriction>
 *             &lt;/complexContent>
 *           &lt;/complexType>
 *         &lt;/element>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "assetcontent", propOrder = { "assettype", "assetdesc", "assetoperation", "content", "info" })
@XmlRootElement(name = "assetcontent")
public class UpdateCategoryAssetContent {

    @XmlElement(required = true, nillable = false)
    protected short assettype;

    @XmlElement(required = true, nillable = false)
    protected short assetdesc;

    @XmlElement(required = true, nillable = false)
    protected short assetoperation;

    @XmlElement(required = true, nillable = false)
    protected UpdateCategoryContent content;

    @XmlElement(required = true, nillable = false)
    protected Info info;

    /**
     * 获取assettype属性的值。
     */
    public short getAssettype() {
        return this.assettype;
    }

    /**
     * 设置assettype属性的值。
     */
    public void setAssettype(final short value) {
        this.assettype = value;
    }

    /**
     * 获取assetdesc属性的值。
     */
    public short getAssetdesc() {
        return this.assetdesc;
    }

    /**
     * 设置assetdesc属性的值。
     */
    public void setAssetdesc(final short value) {
        this.assetdesc = value;
    }

    /**
     * 获取assetoperation属性的值。
     */
    public short getAssetoperation() {
        return this.assetoperation;
    }

    /**
     * 设置assetoperation属性的值。
     */
    public void setAssetoperation(final short value) {
        this.assetoperation = value;
    }

    /**
     * 获取content属性的值。
     * @return possible object is {@link UpdateCategoryContent }
     */
    public UpdateCategoryContent getContent() {
        return this.content;
    }

    /**
     * 设置content属性的值。
     * @param value allowed object is {@link UpdateCategoryContent }
     */
    public void setContent(final UpdateCategoryContent value) {
        this.content = value;
    }

    /**
     * 获取info属性的值。
     * @return possible object is {@link Info }
     */
    public Info getInfo() {
        return this.info;
    }

    /**
     * 设置info属性的值。
     * @param value allowed object is {@link Info }
     */
    public void setInfo(final Info value) {
        this.info = value;
    }
}
