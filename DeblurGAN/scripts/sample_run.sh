#!/bin/bash
ScriptPath="$( cd "$(dirname "$BASH_SOURCE")" ; pwd -P )"
ModelPath="${ScriptPath}/../model"
common_script_dir=${THIRDPART_PATH}/common
. ${common_script_dir}/sample_common.sh
FOLDER_PATH="/home/HwHiAiUser/projectv0.1/DeblurGAN/out/output"
function main()
{   
    # 检查文件夹是否存在
    if [ -d "$FOLDER_PATH" ]; then
    # 删除文件夹内的所有文件
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
