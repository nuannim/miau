import requests
import json
import IPython


import time


# ระบุ API key
Apikey = 'mkipQeIRuF90FiQgUAgD4qvRNNMLM9u2'

# สังเคราะห์เสียง
url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
headers = {'Apikey': Apikey, 'Content-Type': 'application/json'}

# ฟังก์ชันสำหรับโหลดคำจากไฟล์ JSON
def load_sentences(filename='sentences.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['sentences']

# ฟังก์ชันสำหรับแปลงข้อความเป็นเสียง
def text_to_speech(text):
    data = {'input_text': text, 'speaker': 1, 'phrase_break': 0, 'audiovisual': 0}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        wav_url = response.json()['wav_url']
        return wav_url
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# ฟังก์ชันสำหรับดาวน์โหลดและเล่นไฟล์เสียง
def download_and_play_audio(wav_url, filename='test2.wav'):
    resp = requests.get(wav_url, headers={'Apikey': Apikey})
    
    if resp.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(resp.content)
            print(f'Downloaded: {filename}')
            IPython.display.display(IPython.display.Audio(filename))
    else:
        print(f"Error downloading file: {resp.reason}")

# หลักการทำงาน:

# โหลดคำจาก JSON
sentences = load_sentences()

# เลือกคำที่ต้องการจากคำที่โหลดมา (เช่น คำแรก)
text_to_convert = sentences[0]

# แปลงข้อความเป็นเสียง
time.sleep(2)
wav_url = text_to_speech(text_to_convert)

# หากแปลงสำเร็จ ให้ดาวน์โหลดและเล่นไฟล์เสียง
if wav_url:
    download_and_play_audio(wav_url)
