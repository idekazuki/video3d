import os
import tarfile

dir_name = '/home/yanai-lab/ide-k/ide-k/EPIC-KITCHENS/frames_rgb_flow/rgb/train/P01/P01_01.tar'
def jpg_open(tar,frame_dist=30):
    for i in range(0, 1000, int(frame_dist)):
        s = str(i + 1)
        s = s.zfill(10)
        file_name = './frame_' + s + '.jpg'
        print(file_name)
        img = tar.getmember(file_name)
        yield img

with tarfile.open(dir_name, mode='r') as tar:
    tar.extractall(members=jpg_open(tar, frame_dist=30),path='tmp')

print('end')
