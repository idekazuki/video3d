import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3'
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from PIL import Image
import cv2
from read_gulpio import EpicDataset_4_Tmodel
from gulpio.transforms import Scale, CenterCrop, Compose, UnitNorm
import numpy as np
import torch
import matplotlib
import matplotlib.pyplot as plt
from opts import parse_opts




if __name__ =="__main__":
    opt = parse_opts()
    opt.class_counts = (125, 352)
    opt.snippet_length = 1  # Number of frames composing the snippet, 1 for RGB, 5 for optical flow
    opt.snippet_channels = 3  # Number of channels in a frame, 3 for RGB, 2 for optical flow

    #image proccesing parameter
    transforms = Compose([
                        Scale(opt.cropSsize),
                        CenterCrop(opt.cropCsize[0]),
                        ])
    dataset = EpicDataset_4_Tmodel(transforms, class_type=opt.class_type, frame_size=opt.framesize, path=opt.video_root)

    for epoch in range(opt.epoch_num):
        for batch_num, (data, label) in enumerate(dataset):
            data = data.reshape(opt.batch_size, -1, 224, 224)
            datat = torch.tensor(data, dtype=torch.float32)
            img = data[0]
            img = img.reshape(-1,opt.cropCsize[0],opt.cropCsize[0])
            img = img.transpose(1,2,0)

            for i in range(opt.framesize):
                plt.imsave('./img/e{}b{}f{}.png'.format(epoch, batch_num, i),img[:,:,i*3:i*3+
