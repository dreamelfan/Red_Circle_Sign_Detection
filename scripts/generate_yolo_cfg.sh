data_path=$1/TT100K
proj_path=${PWD}/..
cfg_name=${proj_path}/yolo_cfg/red_sign_obj.data 
rm ${cfg_name}

echo "classes = 1" >> ${cfg_name}
echo "train = ${data_path}/train/train.txt" >> ${cfg_name}
echo "valid = ${data_path}/test/test.txt" >> ${cfg_name}
echo "names = ${proj_path}/yolo_cfg/red_sign_obj.names" >> ${cfg_name}
echo "backup = ${proj_path}/yolo_weights/" >> ${cfg_name}

echo "Done!"
