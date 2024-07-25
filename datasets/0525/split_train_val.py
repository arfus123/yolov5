# coding:utf-8
 
import os
import random
import argparse
 
parser = argparse.ArgumentParser()
#txt文件的地址，根据自己的数据进行修改 txt一般存放在Annotations下
parser.add_argument('--yolo_txt_path', default='labels', type=str, help='input yolo_txt label path')
#数据集的划分，地址选择自己数据下的ImageSets/Main
parser.add_argument('--txt_path', default='imagesets', type=str, help='output txt label path')
opt = parser.parse_args()
 
trainval_percent = 1.0  # 训练集和验证集所占比例。 这里没有划分测试集
train_percent = 0.9     # 训练集所占比例，可自己进行调整
txtfilepath = opt.yolo_txt_path
txtsavepath = opt.txt_path
total_xml = os.listdir(txtfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)
 
num = len(total_xml)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)
 
file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')
 
for i in list_index:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
 
file_trainval.close()
file_train.close()
file_val.close()


import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val']
classes = ["1", "2", "3"]   # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)

wd = getcwd()
for image_set in sets:
    image_ids = open('D:/yolov5-master/datasets/0525/imagesets/%s.txt' % (image_set)).read().strip().split()
   
    if not os.path.exists('D:/yolov5-master/datasets/0525/dataset_path/'):
        os.makedirs('D:/yolov5-master/datasets/0525/dataset_path/')
     
    list_file = open('dataset_path/%s.txt' % (image_set), 'w')
    # 这行路径不需更改，这是相对路径
    for image_id in image_ids:
        list_file.write('D:/yolov5-master/datasets/0525/images/%s.jpg\n' % (image_id))
    list_file.close()