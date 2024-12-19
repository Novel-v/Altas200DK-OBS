#!/usr/bin/env python
from obs import GetObjectHeader
from obs import ObsClient
import os
import traceback
obsClient = ObsClient(
        access_key_id='4JUXOHHR10BQSBBHCH8B',     
        secret_access_key='Aq8aUrscgEsVSdzhO4bSgxKtynpbayOPiBCrk85u',  
        server='obs.cn-east-3.myhuaweicloud.com'   
    )
def obs_download():
    try:
        headers = GetObjectHeader()
        # 下载后文件存储到本地的路径
        downloadPath = './video_data/video.mp4'
        # 下载的文件在OBS中的路径
        objectKey = "video/2.MP4"
        bucketName = "course-atlas"
        resp = obsClient.getObject(bucketName, objectKey, downloadPath, headers=headers)
        if resp.status < 300:
            print('Get Object Succeeded')
            print('requestId:', resp.requestId)
            print('url:', resp.body.url)
            response=obsClient.deleteObject('course-atlas', objectKey)
            obsClient.close()
            return True
        else:
            print('Get Object Failed')
            print('requestId:', resp.requestId)
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
            return False
    except:
        print('Get Object Failed') 
        print(traceback.format_exc())