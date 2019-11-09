# video3d
3docnv model for epic-kitchen
## how to use
install https://github.com/kenshohara/video-classification-3d-cnn-pytorch

and copy 3dtrain.py, read_gulpio.py to under /video-classification-3d-cnn-pytorch/

### ResNet18
python 3dtrain.py --model ./pretrain_data/resnet-18-kinetics.pth --mode score --model_depth 18 --structure resnet18 --batch_size 128
### ResNeXt101
python 3dtrain.py --model pretrain_data/resnext-101-kinetics.pth --mode score --model_depth 101 --structure resnext101 --batch_size 64 --model_name resnext --resnet_shortcut B

### if you want to start from the check point.
ex)
python 3dtrain.py --model ./pretrain_data/resnet-18-kinetics.pth --mode score --model_depth 18 --structure resnet18 --batch_size 128 --checkpoint ./logfile/save_8_resnet18.pth

