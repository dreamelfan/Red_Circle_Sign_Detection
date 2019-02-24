import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Path to TT100K dataset")
args = parser.parse_args()

if args.path:
    data_dir = args.path
else:
    data_dir = "/data/TT100K"
    
train_list = open(data_dir+"/train/ids.txt").read().splitlines()
test_list = open(data_dir+"/test/ids.txt").read().splitlines()

with open(data_dir+"/train/"+"train.txt", "w") as TrainList:
    for train_id in train_list:
        TrainList.write(data_dir+"/train/"+train_id+".jpg\n")

with open(data_dir+"/test/"+"test.txt", "w") as TestList:
    for test_id in test_list:
        TestList.write(data_dir+"/test/"+test_id+".jpg\n")

print("Done!")
