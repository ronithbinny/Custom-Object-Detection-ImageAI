from imageai.Detection.Custom import CustomObjectDetection
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import os

# Creat XML File Object :
obj = ET.Element("object")
name = ET.SubElement(obj, "name").text = "white"
pos = ET.SubElement(obj, "pos").text = "Unspecified"
truncated = ET.SubElement(obj, "truncated").text = '0'
difficult = ET.SubElement(obj, "difficult").text = '0'
bndbox = ET.SubElement(obj, "bndbox")
xmin = ET.SubElement(bndbox, "xmin").text = '200'

tree = ET.ElementTree(obj)
tree.write("filename.xml")

