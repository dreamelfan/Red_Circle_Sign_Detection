import os
import json
import numpy as np
import traceback
import time
import argparse
from utils import *


def prepare_labels(datapath = "/data/TT100K"):
    """
        Create new annotation file with only red circle signs labels
    """
    # list of the labels of red circular traffic sign
    red_label_list = "p1,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p2,p20,p21,p22,p23,p24,p25,p26,p27,p28,p3,p4,p5,p6,p7,p8,p9,pa10,pa12,pa13,pa14,pa8,pb,pc,ph1.5,ph2,ph2.1,ph2.2,ph2.4,ph2.5,ph2.8,ph2.9,ph3,ph3.2,ph3.5,ph3.8,ph4,ph4.2,ph4.3,ph4.5,ph4.8,ph5,ph5.3,ph5.5,pl10,pl100,pl110,pl120,pl15,pl20,pl25,pl30,pl35,pl40,pl5,pl50,pl60,pl65,pl70,pl80,pl90,pm10,pm13,pm15,pm1.5,pm2,pm20,pm25,pm30,pm35,pm40,pm46,pm5,pm50,pm55,pm8,pn,pne,po,pw2,pw2.5,pw3,pw3.2,pw3.5,pw4,pw4.2,pw4.5"
    red_label_list = red_label_list.split(',')

    # read old annotations    
    label_file = datapath+"/"+"annotations.json"
    annos = json.loads(open(label_file).read())

    # create new annotations
    for img_id, features in annos['imgs'].copy().items():
        # ignore and delete non-training data
        if not features['path'].startswith('train'):
            annos['imgs'].pop(img_id, None)
        else:
            # keep only red circle signs labels
            tmp_objects = []
            for obj in features['objects']:            
                if obj['category'] in red_label_list:
                    # delete unwanted keys
                    obj.pop('ellipse_org', None)
                    obj.pop('ellipse', None)
                    # create new objects list
                    tmp_objects.append(obj)
            annos['imgs'][img_id]['objects'] = tmp_objects

    # save new annotations into "annotations_red_train.json"
    new_label_file = datapath+"/"+"annotations_red_train.json"
    with open(new_label_file, 'w') as NewJson:
        json.dump(annos, NewJson)


def main(datapath = "/data/TT100K"):
    # prepare labels
    print("[INFO] Preparing labels...")
    if not os.path.isfile(datapath+"/"+"annotations_red_train.json"):        
        prepare_labels(datapath)
    else:
        print("[INFO] Labels were already preprocessed! Skip...")

    print("[INFO] Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Path to TT100K dataset")
    args = parser.parse_args()

    if args.path:
        main(args.path)
    else:
        main()

