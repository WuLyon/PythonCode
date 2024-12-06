import pyaudio
import wave
from pydub import AudioSegment

# 配置录音参数
FORMAT = pyaudio.paInt16  # 16位深度
CHANNELS = 1  # 单声道
RATE = 44100  # 采样率
CHUNK = 1024  # 每次读取的帧数
RECORD_SECONDS = 5  # 录音时长（秒）
OUTPUT_FILE = "output.wav"  # 输出文件名

def record_audio():
    audio = pyaudio.PyAudio()
    
    # 打开音频流
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    
    print("开始录音...")
    frames = []
    
    # 开始录制
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("录音结束。")
    
    # 停止并关闭音频流
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # 保存为 wav 文件
    with wave.open(OUTPUT_FILE, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    print(f"音频已保存为 {OUTPUT_FILE}")

def convert_to_mp3(input_file, output_file):
    audio = AudioSegment.from_wav(input_file)
    audio.export(output_file, format="mp3")
    print(f"音频已转换为 {output_file}")

if __name__ == "__main__":
    record_audio()
    
    # 如果需要保存为 mp3 文件
    mp3_file = "output.mp3"
    convert_to_mp3(OUTPUT_FILE, mp3_file)

