from aip import AipSpeech
from src.youayou.changeFileType import file_exists
import os

""" 你的 APPID AK SK """
APP_ID = '55625094'
API_KEY = 'L21LyDJNsHsEr0KHl5bDa90y'
SECRET_KEY = 'Gf8PpwdH2n9HxjR29t0finNju3haGMmj'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
if __name__ == '__main__':
    fileDir = os.getcwd() + "\\uploads\\"
    #显示该文件夹下所有文件名
    print(os.listdir(fileDir))

    filename = input("请输入需要识别的文件名（wav）：")

    full_name = os.path.join(fileDir, filename)

    if file_exists(full_name) == False:
        print("文件不存在")
        exit()

    # 识别本地文件
    res = client.asr(get_file_content(full_name), 'wav', 16000, {
        'dev_pid': 1537,
    })
    print(res['err_no'])
    print(res['err_msg'])
    print(res['sn'])
    print(res['result'])

