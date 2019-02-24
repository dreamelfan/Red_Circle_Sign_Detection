import numpy as np
import json
import traceback
import os
import time
import argparse
from utils import *

def prepare_labels_yolo(datapath = "/data/TT100K"):
    """
        prepare label for training
    """
    error_imgs = []

    # read training annotations    
    label_file = datapath+"/"+"annotations.json"    
    annos = json.loads(open(label_file).read())

    # train and test file path
    train_path = datapath+"/"+"train"
    test_path = datapath+"/"+"test"
    other_path = datapath+"/"+"other"
    train_list = open(train_path+"/"+"ids.txt").read().splitlines()
    test_list = open(test_path+"/"+"ids.txt").read().splitlines()

    # iterate through all images
    avg_time = 0
    total_task = len(annos['imgs'])
    start_time = time.time()

    for idx, (img_id, features) in enumerate(annos['imgs'].copy().items(),1):
        # estimate time
        if idx % 20 == 1:
            avg_time = (time.time()-start_time)/idx

        task_left = total_task-idx
        eta = int(avg_time*task_left)
        print("[INFO] Creating YOLO labels for image #{}/{}; ETA: {} m {} s".format(idx,total_task,eta//60,eta%60), end="\r")

        try:
            # convert to yolo format
            formated_label_list = []
            for obj in features['objects']:
                formated_label_list.append(convert_labels(datapath+"/"+features['path'],obj['bbox'], return_string=True))

            # save bbox and class info to .txt for each img_id
            if img_id in train_list:
                output_dir = train_path
            elif img_id in test_list:
                output_dir = test_path
            else:
                output_dir = other_path

            with open(output_dir+'/'+img_id+".txt", "w") as TextFile:
                for formated_label in formated_label_list:
                    TextFile.write("0"+" "+formated_label+"\n")
        except:
            traceback.print_exc()
            error_imgs.append(img_id)
            print("[ERROR] Error happened at image", img_id)
        
    # print processing infos
    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Path to TT100K dataset")
    args = parser.parse_args()

    if args.path:
        prepare_labels_yolo(args.path)
    else:
        prepare_labels_yolo()
    
        

