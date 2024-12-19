#!/usr/bin/env python3.9
# coding=utf-8
from obs import ObsClient
# ����ObsClientʵ��
obsClient = ObsClient(
    access_key_id='4JUXOHHR10BQSBBHCH8B',     # myself
    secret_access_key='Aq8aUrscgEsVSdzhO4bSgxKtynpbayOPiBCrk85u',  # myself 
    server='obs.cn-east-3.myhuaweicloud.com'   # myself
)
bucketName = "course-atlas" # myself
# ���屾��1.zip�ļ���·������OBS�洢Ͱ�е��ļ���
local_ply_path = './1.zip' # �滻Ϊ����1.zip�ļ���·��
object_key = 'photos/1.zip' # OBS�д洢���ļ���
response=obsClient.deleteObject('bucketName', object_key)

# ʹ�÷���OBS

try:
    from obs import PutObjectHeader

    headers = PutObjectHeader()
    headers.contentType = 'application/zip'

    resp = obsClient.putFile(
        'course-atlas',
        object_key,    # �������ϴ�����ļ���
        local_ply_path,     # �����滻Ϊ�㱾���ļ���·��
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

# �ر�obsClient
obsClient.close()

