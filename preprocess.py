import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
import numpy as np
from PIL import Image, ImageFilter
from torchvision import transforms


def toPILfromTensor(tensor):
    tensor2pil = transforms.Compose([
        transforms.ToPILImage(),
    ])
    return tensor2pil(tensor)


def getLaplacianEdgeImage(image):
    image = image.convert("L")
    image = image.filter(ImageFilter.FIND_EDGES)
    return image


def preprocess(frame):
    transform = A.Compose(
        [
            A.Resize(width=1280, height=720),
            ToTensorV2(),
        ]
    )

    processor = transform(image=frame)
    preprocessed = processor["image"]

    return preprocessed
