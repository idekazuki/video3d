import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3'
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from PIL import Image
import cv2
from read_gulpio import EpicDataset_4_Tmodel
from gulpio.transforms import Scale, CenterCrop, Compose, UnitNorm
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

class_counts = (125, 352)


batch_size = 1
segment_count = 8
snippet_length = 1  # Number of frames composing the snippet, 1 for RGB, 5 for optical flow
snippet_channels = 3  # Number of channels in a frame, 3 for RGB, 2 for optical flow
height, width = 224, 224


#image proccesing parameter




transforms = Compose([
                     Scale(224),
                     CenterCrop(224),
                     ])
dataset = EpicDataset_4_Tmodel(transforms, class_type='verb', frame_size=8)

for epoch in range(10):
    for batch_num, (data, label) in enumerate(dataset):
        data = data.reshape(batch_size, -1, 224, 224)
        datat = torch.tensor(data, dtype=torch.float32)
#        result = tsm.features(datat)
#        verb, noun = tsm.logits(result)
#        print(verb.shape, noun.shape, torch.argmax(verb, dim=1))
#        print(verb)
        img = data[0]
        img = img.reshape(-1,224,224)
        img = img.transpose(1,2,0)
        print(type(img))
        print(img.shape)
#        plt.imsave('./img/img{}.png'.format(batch_num * (epoch+1)), img)

        for i in range(8):
            plt.imsave('./img/img{}-{}.png'.format(batch_num*(epoch + 1),i),img[:,:,i*3:i*3+3])
