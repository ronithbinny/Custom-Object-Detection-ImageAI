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
