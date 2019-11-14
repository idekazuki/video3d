import argparse
import torch
from datetime import datetime
from tqdm import tqdm

from gulpio import GulpDirectory

def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_root', default='/home/yanai-lab/ide-k/ide-k/epic/data/processed/gulp/rgb_train/', type=str, help='Root path of video')
    parser.add_argument('--data_type', default='verb', type=str)
    args = parser.parse_args()
    return args

class EpicDataset_4_Vmodel(torch.utils.data.Dataset):
    def __init__(self, path='../../epic/data/processed/gulp/rgb_train/', data_type='verb_class'):
        self.path = path
        self.data_type = data_type
        self.dataset = GulpDirectory(self.path)
        self.gdict = list(self.dataset.merged_meta_dict.keys())
        self.datalen = len(self.gdict)

    def __getitem__(self, i):
        video_id = self.gdict[i]
        _, meta = self.dataset[video_id]
        
        if self.data_type == 'frame':
            start = meta['start_frame']
            stop = meta['stop_frame']
               
            return(stop - start) 
        else:
            return(meta[self.data_type])

        

    def __len__(self):
        return self.datalen

if __name__ =="__main__":
    opt = parse_opts()
    dataset = EpicDataset_4_Vmodel(path=opt.video_root, data_type=opt.data_type)
    maxf = 0
    minf =100000
    sumf = 0
    print(len(dataset))
    if opt.data_type == 'frame':
        for meta in tqdm(dataset):
            maxf = max(maxf, meta)
            minf = min(minf, meta)
            sumf += meta
        print('max:{} min:{} ave:{}'.format(maxf, minf ,sumf/len(dataset)))
    else:
        for meta in dataset:
            print('{}:{}'.format(opt.data_type, meta))