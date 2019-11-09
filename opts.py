import argparse

def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_root', default='/home/yanai-lab/ide-k/ide-k/epic/data/processed/gulp/rgb_train/', type=str, 'Root path of video' )
    parser.add_argument('--batch_size', default=16, type=int, help='Batch size')
    parser.add_argument('--category_num', default=-1, type=int, help='The number of categories to use. -1 represents all use.')
    parser.add_argument('--train_val', default=0.8, type=float, help='Ratio of training data to test data')
    parser.add_argument('--crop_position', default=0, type=int, help='Position selection when crop. 0:center, 1:4corner+center random')
    parser.add_argument('--cropSsize', default=256, type=int)
    parser.add_argument('--cropCsize', default=[224], type=list)
    parser.add_argument('--cropRsize', default=-1)
    parser.add_argument('--framesize', default=16, type=int, help='Number of frames to get')
    parser.add_argument('--temporal-p', default=0, type=int, help='temporal sampling point 0:divdide evenly, 1:random')
    parser.add_argument('--horizon', action='store_ture', help='If ture, horizon flip 0.5')
    parser.defaults(verbose=True)
    parser.add_argument('--normalization', action='store_ture', help='If ture, normalization RGB')
    parser.defaults(verbose=True)

