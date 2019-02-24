# Red_Circle_Sign_Detection
Machine learning model for red circle traffic sign detection

## How to use
### Download this repo
```
git clone https://github.com/dreamelfan/Red_Circle_Sign_Detection
cd Red_Circle_Sign_Detection
```

### Download TT100K dataset
```
cd scripts
./download_TT100K.sh <TT100K_download_path>
```

### Prepare training data and labels
```
./prepare_data.sh <TT100K_download_path>
```

### Train YOLO
#### Generate YOLO model configuration file
```
./generate_yolo_cfg.sh <TT100K_download_path>
```

#### Download darknet framework
```
cd ..
git clone https://github.com/AlexeyAB/darknet
```

#### Build darknet framework
Refer to https://github.com/AlexeyAB/darknet#how-to-compile-on-linux

#### Download conv layer weights of pretrained dark53 model
```
cd darknet
wget https://pjreddie.com/media/files/darknet53.conv.74
```

#### Start training
```
cd ../script
./train.sh
```

### Test YOLO (measure mAP)
```
./test.sh
```
