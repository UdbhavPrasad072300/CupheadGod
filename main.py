from grabscreen import grab_screen
from preprocess import preprocess, getLaplacianEdgeImage, toPILfromTensor
from directkeys import PressKey, ReleaseKey, W, A, S, D, UP, DOWN, LEFT, RIGHT

import time
import torch
import torch.nn as nn
import torchvision
import numpy as np
from PIL import Image

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(DEVICE)

torch.manual_seed(0)
np.random.seed(0)

model = torch.hub.load('pytorch/vision:v0.6.0', 'deeplabv3_resnet101', pretrained=True)
model.to(DEVICE).eval()


def get_pred(img, model):
    input_tensor = img.unsqueeze(0).float()
    input_tensor = input_tensor.to(DEVICE)

    with torch.no_grad():
        output = model(input_tensor)["out"][0]
        output = output.argmax(0)

    return output.cpu()


if __name__ == '__main__':
    time.sleep(10)
    last_time = time.time()
    while True:
        screen = preprocess(grab_screen((0, 0, 2560, 1440)))
        img = toPILfromTensor(screen)
        edges = preprocess(np.array(getLaplacianEdgeImage(img)))

        print(edges.size(), screen.size())
        out = get_pred(screen, model)
        toPILfromTensor(out.float()).show()
        print(time.time() - last_time)
        last_time = time.time()
        # print(torch_array.size())
        # print(mask.size())
        # img.show()

        exit()
