data_path=$1/TT100K

cd ../data_preprocess
echo "python3 preprocess_labels.py --path ${data_path}"
python3 preprocess_labels.py --path ${data_path}
echo "python3 generate_train_list.py --path ${data_path}" 
python3 generate_train_list.py --path ${data_path} 
echo "python3 convert_YOLO_labels_TT100K.py --path ${data_path}" 
python3 convert_YOLO_labels_TT100K.py --path ${data_path}  
