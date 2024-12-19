#!/usr/bin/env python
# coding=utf-8
import sys
sys.path.append('./')
import numpy
import os
import cv2
import subprocess
import time
import pexpect
from obs_getfile import obs_download

def project_run():
    print("[INFO] vtoj start")
    res=os.system("python3.9 ./video_to_jpg.py")
    while res != 0:
        time.sleep(2)
    print("[INFO] vtoj success")
    print("[INFO] transform start")
    res=os.system("python3.9 ./transform_model.py")
    while res != 0:
        time.sleep(2)
    print("[INFO] transform end")
    print("[INFO] sample_build.sh start")
    res=os.system("expect ./scripts_run/auto_input.exp")
    while res != 0:
        time.sleep(10)
    print("[INFO] sample_build.sh end")
    print("[INFO] sample_run.sh start")
    res=os.system("./scripts_run/sample_run.sh")
    while res != 0:
        time.sleep(10)
    print("[INFO] sample_run.sh end")
    print("[INFO] transform2 start")
    res=os.system("python3.9 ./transform_4k.py")
    while res != 0:
        time.sleep(2)
    print("[INFO] transform2 end")
    print("[INFO] obs_upload start")
    res=os.system("python3.9 ./obs_upload.py")
    while res != 0:
        time.sleep(2)
    print("[INFO] obs_upload end")


def main():
    while True:
        test_value = obs_download()
        if test_value:
            print("200dk start")
            project_run()
            print("200dk end")
        else:
            print("continue to receive mp4 file")
            time.sleep(5)

if __name__ == "__main__":
    main()