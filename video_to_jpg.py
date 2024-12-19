#!/usr/bin/env python3.9
# coding=utf-8
#视频转换为图片

import os
import cv2
from pathlib import Path

def clear_folder_contents(folder_path):
    path = Path(folder_path)
    if path.exists():
        # 遍历路径中的所有文件和文件夹
        for child in path.iterdir():
            try:
                # 如果是文件或链接，则删除
                if child.is_file() or child.is_symlink():
                    child.unlink()
                # 如果是文件夹，则递归删除
                elif child.is_dir():
                    child.rmdir()
            except Exception as e:
                print(f'Failed to delete {child}. Reason: {e}')
                
#所有视频输出的图片按递增顺序排列，XXXX
def convert_videos_to_images(input_folder, output_folder, frame_interval=12, image_index = 0):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有视频文件
    for video_file in os.listdir(input_folder):
        if video_file.endswith(('.mp4', '.avi')):  # 现支持mp4和avi格式
            video_path = os.path.join(input_folder, video_file)
            
            # 打开视频文件
            cap = cv2.VideoCapture(video_path)
            
            frame_index = 0 #视频帧
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                # 每12帧保存一张图片
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
    #首先删除输出文件夹中已有文件
    clear_folder_contents(output_folder)
    convert_videos_to_images(input_folder, output_folder)
    #再次删除上传的视频文件
    clear_folder_contents(input_folder)