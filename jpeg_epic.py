import os
import tarfile

dir_name = '/home/yanai-lab/ide-k/ide-k/EPIC-KITCHENS/frames_rgb_flow/rgb/train/P01/P01_01.tar'
def jpg_open(tar,frame_dist=30):
    for i in range(0, 1000000000, int(frame_dist)):
        s = str(i + 1)
        s = s.zfill(10)
        file_name = './frame_' + s + '.jpg'
        print(file_name)
        try:
            img = tar.getmember(file_name)
        except KeyError:
            print('end of video index')
            return 0
        
        yield img

with tarfile.open(dir_name, mode='r') as tar:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar, members=jpg_open(tarframe_dist="3000"), path="tmp")

print('end')
