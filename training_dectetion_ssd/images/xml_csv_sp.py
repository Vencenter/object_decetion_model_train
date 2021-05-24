# -*- coding:utf-8 -*-

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import random

def xml_to_csv(path):
    xml_list = []
    # 设置训练集所占比例
    i = 0
    img_file = glob.glob(path + '/*.xml')
    print (img_file)
    random.shuffle(img_file)
    for xml_file in img_file:
        i = i + 1
        tree = ET.parse(xml_file)
        root = tree.getroot()
        if True:
            for member in root.findall('object'):
                value = (
                         "E:/Download/object_detection_training/training_dectetion_ssd/images/"+"test/"+root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
         
                
            xml_list.append(value)
        print(i)

      
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
    # xml文件的存储地址，根据自己xml存储路径进行调整
    image_path = 'test/'
    # csv文件保存位置，自行调整
    # 训练集
    csv_save_path = 'test_labels.csv'
    # 测试集
    csv_save_path_test = 'test_labels.csv'

    xml_df= xml_to_csv(image_path)

    print(xml_df)
    xml_df.to_csv(csv_save_path, index=None)
    print('Successfully converted xml to csv.')
main()
