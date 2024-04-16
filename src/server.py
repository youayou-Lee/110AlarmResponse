from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # 允许所有源的跨域请求

@app.route('/audio/upload', methods=['POST'])
def upload_audio():
    # 获取前端上传的音频数据
    print('yes')
    audio_file = request.files.get('audio')

    # 确定保存音频文件的目录（这里假设为当前目录下的'uploads'子目录）
    upload_dir = os.path.join(os.getcwd(), 'src/uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # 生成保存文件的完整路径（包含文件名）
    file_path = os.path.join(upload_dir, 'input.opus')

    # 将音频数据保存为PCM文件
    with open(file_path, 'wb') as f:
        f.write(audio_file.read())

    return 'Audio data received and saved successfully.'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
