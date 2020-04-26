import os
import xml.etree.ElementTree as ET

for xml in os.listdir() :
    if xml.endswith(".xml") :
        print(xml)
        tree = ET.parse(xml)
        root = tree.getroot()
        
        for obj in root.findall('object') :
               
            # Changing :
            
            if obj[0].text == "damged_cell" :
                obj[0].text = "damaged_cell"
                tree.write(xml)
                
            elif obj[0].text == "normail_coating" :
                print(xml)
                obj[0].text = "normal_coating"
                tree.write(xml)