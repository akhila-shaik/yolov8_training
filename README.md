# yolov8

YOLOv8 Training and Inference Report

1. Project Overview

This project focuses on training a YOLOv8s model for object detection on a Retail Store Dataset. The process includes training, inference, and conversion to the ONNX format to optimize inference speed.

2. run data_preprocessing.py to get structured dataset(if needed)

Dataset Structure
Images:
    ├── train
    │   ├── image_1.png
    │   ├── image_2.png
    ├── val
    │   ├── image_3.png
    │   ├── image_4.png
    ├── test
    │   ├── image_5.png
    │   ├── image_6.png
Labels:
    ├── train
    │   ├── image_1.txt
    │   ├── image_2.txt
    ├── val
    │   ├── image_3.txt
    │   ├── image_4.txt
    ├── test
    │   ├── image_5.txt
    │   ├── image_6.txt
 
2. Training Setup on cpu

Environment Setup:

conda create -n yolov8 python=3.8

3.run yolov8_custom_training.ipynb to train a custom yolov8s.pt model.

4.run TORCH_TO_ONNX.py to get onnx model.

5.Test both the models (.pt and .onnx) and observe the results and inference time.

6.Inference time :

pytorch model - 417.2 ms
onxx model - 288.3ms

The inference time is decreased by approximately 30.90%(on cpu) for onnx model






