# Red_Circle_Sign_Detection
Machine learning model for red circle traffic sign detection

## How to use
### Download TT100K dataset
```
cd scripts
./download_TT100K.sh <data_path>
```

### Prepare training data and labels
```
./prepare_data.sh <data_path>
```

### Generate YOLO model configuration file
```
./generate_yolo_cfg.sh <data_path>
```

### Train YOLO
#### Download darknet framework
```
git clone https://github.com/AlexeyAB/darknet
```

#### Build darknet framework
Refer to https://github.com/AlexeyAB/darknet#how-to-compile-on-linux

#### Download conv layer weights of pretrained dark53 model
```
wget https://pjreddie.com/media/files/darknet53.conv.74
```

#### Start training
```
./train.sh
```

### Test YOLO (measure mAP)
```
./test.sh
```
