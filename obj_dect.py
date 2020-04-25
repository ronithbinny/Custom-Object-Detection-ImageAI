# !pip install tensorflow-gpu==1.13.1
# !pip install imageai

from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="BigData/")
trainer.setTrainConfig(object_names_array=["white","normal_coating","coilcore_present","innershell_good","innershell_bad","mantle_dent","misalignment"], 
                       batch_size=4, num_experiments=30, 
                       train_from_pretrained_model="pretrained-yolov3.h5")                
trainer.trainModel()


# After Training :
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="BigData/")
metrics = trainer.evaluateModel(model_path="BigData/models", json_path="BigData/json/detection_config.json", iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
print(metrics)


# Detection
detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("ens-ex-60--loss-2.76.h5") 
detector.setJsonPath("detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="holo3.jpg", output_image_path="holo3-detected.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
