#!yolo mode=export model="E:\07-12_yolo\yolov8\training_results\sku\weights\best.pt" format=onnx
from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO(r"E:\07-12_yolo\yolov8\training_results\sku\weights\best.pt")  # Change this to your model file (e.g., "best.pt")

# Export the model to ONNX with a specific input size (384x640)
model.export(format="onnx", imgsz=(384, 640), dynamic=True)  # Set dynamic=True for flexibility