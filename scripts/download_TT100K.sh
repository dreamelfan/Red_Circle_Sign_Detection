data_path=$1
mkdir -p ${data_path}
cd ${data_path}

wget http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/data.zip
unzip data.zip
mv data TT100K
cd TT100K

echo "Done!"
