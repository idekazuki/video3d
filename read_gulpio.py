from gulpio import GulpDirectory
import time
import numpy as np
import torch


import matplotlib.pyplot as plt


class EpicDataset_4_Tmodel(torch.utils.data.Dataset):
    def __init__(self, transform, path='../../epic/data/processed/gulp/rgb_train/', frame_size=16, class_type='verb'):
        self.transform = transform
        self.path = path
        self.class_type = class_type
        self.frame_size = frame_size
        self.dataset = GulpDirectory(self.path)
        self.gdict = list(self.dataset.merged_meta_dict.keys())
        self.datalen = len(self.gdict)

    def __getitem__(self, i):
        video_id = self.gdict[i]
        frames, meta = self.dataset[video_id]

        dist_img = meta['num_frames'] / float(self.frame_size)
        seg_list = np.array([int(dist_img / 2.0 + dist_img * x)
                             for x in range(self.frame_size)])
        img_group = []
        for j in seg_list:
            frame = self.transform(frames[j])
            img_group.append(frame)
        img_group = np.array(img_group)
        img_group = img_group.transpose(3, 0, 1, 2)
        return(img_group, meta['verb_class'])

    def __len__(self):
        return self.datalen

class EpicDataset_4_Vmodel(torch.utils.data.Dataset):
    def __init__(self, transform, path='../../epic/data/processed/gulp/rgb_train/', frame_size=16, class_type='verb'):
        self.transform = transform
        self.path = path
        self.class_type = class_type
        self.frame_size = frame_size
        self.dataset = GulpDirectory(self.path)
        self.gdict = list(self.dataset.merged_meta_dict.keys())
        self.datalen = len(self.gdict)

    def __getitem__(self, i):
        video_id = self.gdict[i]
        frames, meta = self.dataset[video_id]

        dist_img = meta['num_frames'] / float(self.frame_size)
        seg_list = np.array([int(dist_img / 2.0 + dist_img * x)
                             for x in range(self.frame_size)])
        img_group = []
        for j in seg_list:
            frame = frames[j]
            img_group.append(frame)
        img_group = self.transform(img_group)
        img_group = np.array(img_group)
        img_group = img_group.transpose(3, 0, 1, 2)
        return(img_group, meta['verb_class'])

    def __len__(self):
        return self.datalen
    


