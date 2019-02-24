# Red Circle Traffic Sign Detection
Machine learning model for red circle traffic sign detection

## How to use
### 1. Download this repo
```
git clone https://github.com/dreamelfan/Red_Circle_Sign_Detection
```

### 2. Download TT100K dataset
```
cd Red_Circle_Sign_Detection
cd scripts
./download_TT100K.sh <TT100K_download_path>
```

### 3. Prepare training data and labels
```
./prepare_data.sh <TT100K_download_path>
```

### 4. Train YOLO
#### 4.1. Generate YOLO model configuration file
```
./generate_yolo_cfg.sh <TT100K_download_path>
```

#### 4.2. Download darknet framework
```
cd ..
git clone https://github.com/AlexeyAB/darknet
```

#### 4.3. Build darknet framework
Refer to https://github.com/AlexeyAB/darknet#how-to-compile-on-linux

#### 4.4. Download conv layer weights of pretrained dark53 model
```
cd darknet
wget https://pjreddie.com/media/files/darknet53.conv.74
```

#### 4.5. Start training
```
cd ../script
./train.sh
```

### 5. Test YOLO (measure mAP)
```
./test.sh
```
