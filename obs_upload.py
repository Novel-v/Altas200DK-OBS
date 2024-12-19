#!/usr/bin/env python3.9
# coding=utf-8
from obs import ObsClient
# 创建ObsClient实例
obsClient = ObsClient(
    access_key_id='4JUXOHHR10BQSBBHCH8B',     # myself
    secret_access_key='Aq8aUrscgEsVSdzhO4bSgxKtynpbayOPiBCrk85u',  # myself 
    server='obs.cn-east-3.myhuaweicloud.com'   # myself
)
bucketName = "course-atlas" # myself
# 定义本地1.zip文件的路径和在OBS存储桶中的文件名
local_ply_path = './1.zip' # 替换为本地1.zip文件的路径
object_key = 'photos/1.zip' # OBS中存储的文件名
response=obsClient.deleteObject('bucketName', object_key)

# 使用访问OBS

try:
    from obs import PutObjectHeader

    headers = PutObjectHeader()
    headers.contentType = 'application/zip'

    resp = obsClient.putFile(
        'course-atlas',
        object_key,    # 这里是上传后的文件名
        local_ply_path,     # 这里替换为你本地文件的路径
        metadata={'meta1': 'value1', 'meta2': 'value2'},
        headers=headers,
        #progressCallback=callback

    )
    if resp.status < 300:
        print(resp)
        print('objectUrl:',resp.body.objectUrl)
        print('requestId:', resp.requestId)
        print('etag:', resp.body.etag)
        print('versionId:', resp.body.versionId)
        print('storageClass:', resp.body.storageClass)
    else:
        print(resp)
        print('errorCode:', resp.errorCode)
        print('errorMessage:', resp.errorMessage)
except:
    import traceback

    print(traceback.format_exc())

# 关闭obsClient
obsClient.close()

