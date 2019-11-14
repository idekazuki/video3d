import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3'
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from PIL import Image
import cv2
from read_gulpio import EpicDataset_4_Tmodel, EpicDataset_4_Vmodel
from spatial_transforms import Scale, CenterCrop, Compose, UnitNorm, ComposeVideo, RandHorFlipVideo, RandomCropVideo, RandomCornerCrop
import numpy as np
import torch
import matplotlib
import matplotlib.pyplot as plt
from opts import parse_opts
import random


if __name__ =="__main__":
    opt = parse_opts()
    opt.class_counts = (125, 352)
    opt.snippet_length = 1  # Numbertemporal_transform of frames composing the snippet, 1 for RGB, 5 for optical flow
    opt.snippet_channels = 3  # Number of channels in a frame, 3 for RGB, 2 for optical flow

    #image proccesing parameter
   
    image_transforms = [
                        Scale(opt.cropSsize),
    ]
    video_transforms = [
                        RandomCornerCrop(opt.cropCsize),
                        RandHorFlipVideo()
    ]
    
    vtransforms = ComposeVideo(image_transforms, video_transforms)
#    dataset = EpicDataset_4_Tmodel(transforms, class_type=opt.class_type, frame_size=opt.framesize, path=opt.video_root)
    dataset = EpicDataset_4_Vmodel(vtransforms, class_type=opt.class_type, frame_size=opt.framesize, path=opt.video_root)
    print(opt.cropCsize)

    for epoch in range(opt.epoch_num):
        for batch_num, (data, label) in enumerate(dataset):
            data = data.transpose(1, 2, 3, 0)
            print(data.shape)

            for i in range(opt.framesize):
                plt.imsave('./img/e{}b{}f{}.jpg'.format(epoch, batch_num, i),data[i])

