#!/usr/bin/env python3.9
# coding=utf-8
#��Ƶת��ΪͼƬ

import os
import cv2
from pathlib import Path

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
                
#������Ƶ�����ͼƬ������˳�����У�XXXX
def convert_videos_to_images(input_folder, output_folder, frame_interval=12, image_index = 0):
    # ȷ������ļ��д���
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # ���������ļ����е�������Ƶ�ļ�
    for video_file in os.listdir(input_folder):
        if video_file.endswith(('.mp4', '.avi')):  # ��֧��mp4��avi��ʽ
            video_path = os.path.join(input_folder, video_file)
            
            # ����Ƶ�ļ�
            cap = cv2.VideoCapture(video_path)
            
            frame_index = 0 #��Ƶ֡
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                # ÿ12֡����һ��ͼƬ
                if frame_index % frame_interval == 0:
                    image_filename = f'test{image_index:04d}.jpg'
                    image_path = os.path.join(output_folder, image_filename)
                    cv2.imwrite(image_path, frame)
                    image_index += 1
                
                frame_index += 1
            
            cap.release()
    print("video to picture successful")

if __name__ == "__main__":
    input_folder = './video_data'
    output_folder = './raw_data'
    #����ɾ������ļ����������ļ�
    clear_folder_contents(output_folder)
    convert_videos_to_images(input_folder, output_folder)
    #�ٴ�ɾ���ϴ�����Ƶ�ļ�
    clear_folder_contents(input_folder)