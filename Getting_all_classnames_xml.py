import os
import xml.etree.ElementTree as ET

clas = []

for xml in os.listdir() :
    print(xml)
    tree = ET.parse(xml)
    root = tree.getroot()
    
    for obj in root.findall('object') :
        
        if obj[0].text in clas :
            pass
        else :  
            clas.append(obj[0].text)
