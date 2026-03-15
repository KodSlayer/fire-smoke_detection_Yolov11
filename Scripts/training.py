# This is the script to train the model after unzipping 


import os
from ultralytics import YOLO

# Verification of dataset path
data_path = "/content/Fire-Smoke-Detection-Yolov11-2/data.yaml"
if not os.path.exists(data_path):
    print(f"❌ Warning: {data_path} not found. Check if the extraction was successful.")
else:
    model = YOLO("yolo11n.pt")

    results = model.train(
        data=data_path,
        epochs=50,
        imgsz=640,
        batch=16,
        name="fire_smoke_yolo11",
        patience=10,
        device=0,
        workers=4,
        save=True,
        plots=True
    )

    print("✅ Training complete!")