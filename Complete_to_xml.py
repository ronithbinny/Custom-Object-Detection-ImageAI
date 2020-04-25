from imageai.Detection.Custom import CustomObjectDetection
import xml.etree.ElementTree as ET
import os

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("detection_model-ex-012--loss-0008.956.h5") 
detector.setJsonPath("detection_config.json")
detector.loadModel()

path  = r'C:\Users\Ronith\Desktop\Lincode Labs\Custom Object Detection\Test_Img'

for img in os.listdir(path) :
    if img.endswith(".jpg"):
        img_name = r'C:\Users\Ronith\Desktop\Lincode Labs\Custom Object Detection\Test_Img\{}'.format(img)
        img_out = r'C:\Users\Ronith\Desktop\Lincode Labs\Custom Object Detection\Output\{}'.format(img)
        detections = detector.detectObjectsFromImage(input_image = img_name, output_image_path = img_out)
        
        white_per = 0
        white = []
        normal_coating_per = 0
        normal_coating = []
        coilcore_present_per = 0
        coilcore_present = []
        innershell_good_per = 0
        innershell_good = []
        
        for detection in detections:
            name = detection["name"]
            loc = detection["box_points"]
            per = int(detection["percentage_probability"])
            
            if name == "white" and white_per < per :
                white.append(loc)

            elif name == "normal_coating" and normal_coating_per < per :
                normal_coating.append(loc)
                
            elif name == "coilcore_present" and coilcore_present_per < per :
                coilcore_present.append(loc)
                
            elif name == "innershell_good" and innershell_good_per < per :
                innershell_good.append(loc)
         
        # Create XML File Object :
        try :
            obj = ET.Element("object")
            name = ET.SubElement(obj, "name").text = "white"
            pos = ET.SubElement(obj, "pos").text = "Unspecified"
            truncated = ET.SubElement(obj, "truncated").text = '0'
            difficult = ET.SubElement(obj, "difficult").text = '0'
            bndbox = ET.SubElement(obj, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin").text = str(white[-1][0])
            ymin = ET.SubElement(bndbox, "ymin").text = str(white[-1][1])
            xmax = ET.SubElement(bndbox, "xmax").text = str(white[-1][2])
            ymax = ET.SubElement(bndbox, "ymax").text = str(white[-1][3])
        except :
            pass
        
        try :
            obj1 = ET.Element("object")
            name = ET.SubElement(obj1, "name").text = "normal_coating"
            pos = ET.SubElement(obj1, "pos").text = "Unspecified"
            truncated = ET.SubElement(obj1, "truncated").text = '0'
            difficult = ET.SubElement(obj1, "difficult").text = '0'
            bndbox = ET.SubElement(obj1, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin").text = str(normal_coating[-1][0])
            ymin = ET.SubElement(bndbox, "ymin").text = str(normal_coating[-1][1])
            xmax = ET.SubElement(bndbox, "xmax").text = str(normal_coating[-1][2])
            ymax = ET.SubElement(bndbox, "ymax").text = str(normal_coating[-1][3])
        except :
            pass
        
        try :
            obj2 = ET.Element("object")
            name = ET.SubElement(obj2, "name").text = "coilcore_present"
            pos = ET.SubElement(obj2, "pos").text = "Unspecified"
            truncated = ET.SubElement(obj2, "truncated").text = '0'
            difficult = ET.SubElement(obj2, "difficult").text = '0'
            bndbox = ET.SubElement(obj2, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin").text = str(coilcore_present[-1][0])
            ymin = ET.SubElement(bndbox, "ymin").text = str(coilcore_present[-1][1])
            xmax = ET.SubElement(bndbox, "xmax").text = str(coilcore_present[-1][2])
            ymax = ET.SubElement(bndbox, "ymax").text = str(coilcore_present[-1][3])
        except :
            pass
        
        try :
            obj3 = ET.Element("object")
            name = ET.SubElement(obj3, "name").text = "innershell_good"
            pos = ET.SubElement(obj3, "pos").text = "Unspecified"
            truncated = ET.SubElement(obj3, "truncated").text = '0'
            difficult = ET.SubElement(obj3, "difficult").text = '0'
            bndbox = ET.SubElement(obj3, "bndbox")
            xmin = ET.SubElement(bndbox, "xmin").text = str(innershell_good[-1][0])
            ymin = ET.SubElement(bndbox, "ymin").text = str(innershell_good[-1][1])
            xmax = ET.SubElement(bndbox, "xmax").text = str(innershell_good[-1][2])
            ymax = ET.SubElement(bndbox, "ymax").text = str(innershell_good[-1][3])
        except :
            pass
        
        tree = ET.parse(img_name[:-3] + 'xml')
        root = tree.getroot()
       
        root.append(obj)
        root.append(obj1)
        root.append(obj2)
        root.append(obj3)
        
        print(img_out[:-3])
        tree.write(img_out[:-3] + 'xml')
        
