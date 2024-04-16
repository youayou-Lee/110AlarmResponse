**程序运行流程：**


有可能需要ffmpeg，要用的时候再找我要

1. 后端文件server.py 开启监听
2. 前端开始录音，结束录音会上传到/src/uploads/中
3. 默认文件类型是opus，然后可以通过 tools包下的changeFileType.py 脚本将文件类型转换成wav
4. 然后就可以通过/src/下的recognize.py 脚本进行识别了









