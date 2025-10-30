from ultralytics import YOLO
import torch

def train_model():
    if torch.cuda.is_available():
        print("CUDA device:", torch.cuda.get_device_name(0))
    else:
        print("CUDA not available, will train on CPU")

    model = YOLO("yolov8n.yaml")

    results = model.train(
        data="../config/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0
    )

if __name__ == "__main__":
    train_model()


