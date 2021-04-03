import albumentations as A
import numpy as np


def preprocess(frame):
    transform = A.Compose(
        [
            A.Resize(width=1920, height=1080),
        ]
    )

    processor = transform(image=frame)
    preprocessed = processor["image"]

    return preprocessed
