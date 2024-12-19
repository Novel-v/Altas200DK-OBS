#!/bin/bash
ScriptPath="$( cd "$(dirname "$BASH_SOURCE")" ; pwd -P )"
ModelPath="${ScriptPath}/../model"
common_script_dir=${THIRDPART_PATH}/common
. ${common_script_dir}/sample_common.sh
FOLDER_PATH="/home/HwHiAiUser/projectv0.1/DeblurGAN/out/output"
function main()
{   
    # ����ļ����Ƿ����
    if [ -d "$FOLDER_PATH" ]; then
    # ɾ���ļ����ڵ������ļ�
        rm -f "$FOLDER_PATH"/*
        echo "All files in $FOLDER_PATH have been deleted."
    else
        echo "Error: Folder does not exist."
    fi
    echo "[INFO] The sample starts to run"
    running_command="./main ../data"
    # start runing
    running
    if [ $? -ne 0 ];then
        return 1
    fi
}
main
