#!/usr/bin/env python3.9
# coding=utf-8
# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import zipfile
import os
import cv2
from pathlib import Path

def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # �����������ļ�·��
                file_path = os.path.join(root, file)
                # ���ļ���ӵ� zip �ļ��У�arcname �������� zip �ļ��е�·��
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def clear_folder_contents(folder_path):
    path = Path(folder_path)
    if path.exists():
        # ����·���е������ļ����ļ���
        for child in path.iterdir():
            try:
                # ������ļ������ӣ���ɾ��
                if child.is_file() or child.is_symlink():
                    child.unlink()
                # ������ļ��У���ݹ�ɾ��
                elif child.is_dir():
                    child.rmdir()
            except Exception as e:
                print(f'Failed to delete {child}. Reason: {e}')

# ����ɾ��input�ļ����µ�����������ļ�
folder_path = './final_data/input'
clear_folder_contents(folder_path)

FILE_PATH = './final_previous_data/'
for file in os.listdir(FILE_PATH):
    img_path = FILE_PATH + file
    img = cv2.imread(img_path)
    img = cv2.resize(img, (3840, 2160))
    save_path = './final_data/input/' + file.split('.')[0] + '.jpg'
    cv2.imwrite(save_path, img)
print("transform successful")
folder_to_compress = './final_data'
zip_file_name = './1.zip'
zip_folder(folder_to_compress, zip_file_name)
print("zip successful")