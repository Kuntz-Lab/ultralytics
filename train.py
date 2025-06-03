from ultralytics import YOLO


def train(model_name, data, epochs=100):
    model = YOLO(model_name)  # load a pretrained model (recommended for training)
    model.train(data=data, epochs=epochs, imgsz=640, batch=16, device="0")  # train the model

    model_path = model.export(format="onnx")  # export the model to PyTorch format
    print(f"Model trained and exported to {model_path}")


if __name__ == "__main__":
    # load pre-trained segmentation model
    model_name = "yolo11m-seg.pt"  # load a pretrained model (recommended for training)

    # train model
    train(model_name=model_name, data="medvision_dataset/data.yaml", epochs=10)

