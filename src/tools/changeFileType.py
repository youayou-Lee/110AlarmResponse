import os
import wave
import subprocess

def file_exists(file_path: str) -> bool:
    """
    判断指定路径的文件是否存在。

    参数:
        file_path (str): 待检查文件的完整路径。

    返回:
        bool: 如果文件存在返回True，否则返回False。
    """
    return os.path.exists(file_path)

def check_audio_format(filename):
    # 读取文件的前44个字节（WAV文件的头部长度为44字节）
    with open(filename, 'rb') as f:
        header = f.read(44)

    # 判断文件是否是WAV格式
    if header[0:4] == b'RIFF' and header[8:12] == b'WAVE':
        return 'WAV'

    # 判断文件是否是PCM格式
    if header[0:2] == b'\x50\x4b' and header[30:34] == b'\x4d\x4d\x50\x34':
        return 'PCM'

    # 判断文件是否是MP3格式
    if header[0:3] == b'\xff\xfb' or header[0:3] == b'\xff\xf3':
        return 'MP3'

    # 判断文件是否是Opus格式
    if header[0] == 0x1a and header[1] == 0x45:
        return 'Opus'

    return 'Unknown'

def rename_file(filename, new_extension, index):
    basename, _ = os.path.splitext(filename)
    new_filename = f"{basename}.{new_extension}"
    if index > 0:
        new_filename = f"{basename}_{index}.{new_extension}"
    os.rename(filename, new_filename)
    print(f"文件名已修改为：{new_filename}")

def convert_to_16000hz_wav(filename):
    # 打开原始wav文件
    with wave.open(filename, 'rb') as wf:
        params = wf.getparams()
        if params.framerate != 16000:
            # 设置新的参数
            new_params = (params.nchannels, params.sampwidth, 16000, params.nframes, params.comptype, params.compname)
            # 创建新的16000Hz的wav文件
            with wave.open(filename, 'wb') as new_wf:
                new_wf.setparams(new_params)
                new_wf.writeframes(wf.readframes(params.nframes))
            print(f"文件 {filename} 已转换为采样率为16000Hz的WAV文件。")

def convert_to_wav_with_ffmpeg(filename):
    fName, extension = os.path.splitext(filename)
    new_filename = fName + '_16k.wav'
    command = f"ffmpeg -y -i {filename} -ar 16000 {new_filename}"
    subprocess.run(command, shell=True)
    print(f"文件 {filename} 已使用ffmpeg转换为采样率为16000Hz的WAV文件：{new_filename}")

if __name__ == "__main__":
    folder_path = "F:/pycharm/pythonProject/src/uploads/"
    flag = True
    while flag:
        file_count = 0
        for filename in os.listdir(folder_path):
            full_path = os.path.join(folder_path, filename)
            if os.path.isfile(full_path):
                format_type = check_audio_format(full_path)
                print(f"文件 {filename} 的格式为：{format_type}")
                if format_type == 'WAV':
                    convert_to_16000hz_wav(full_path)
                elif format_type != 'Unknow':
                    user_input = input(f"文件 {filename} 的格式为{format_type}，是否要将其转换为采样率为16000Hz的WAV文件？(y/n): ")
                    if user_input.lower() == 'y':
                        convert_to_wav_with_ffmpeg(full_path)
                    else:
                        print("不处理\n")

                    rename_file(full_path, format_type.lower(), file_count)
                    file_count += 1


        flag = False
        print("所有文件处理完成。")

    print("程序结束。")
