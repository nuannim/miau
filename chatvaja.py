import requests
import json
import IPython

import time

import os

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
        print("Response JSON:", response.json())
        wav_url = response.json()['wav_url']
        return wav_url
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None



def download_audio(wav_url, filename):
    retry_count = 0
    max_retries = 5  # กำหนดจำนวนครั้งสูงสุดในการลองใหม่
    while retry_count < max_retries:
        resp = requests.get(wav_url, headers={'Apikey': Apikey})
        if resp.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(resp.content)
                print(f'Downloaded: {filename}')
            return
        else:
            retry_count += 1
            print(f"Error downloading file: {resp.reason}")
            time.sleep(10)

# สร้างโฟลเดอร์สำหรับเก็บไฟล์เสียง (ถ้าไม่มีอยู่แล้ว)
os.makedirs("audio_files", exist_ok=True)


# โหลดคำจาก JSON
sentences = load_sentences()

# Loop ผ่าน sentences เพื่อแปลงและดาวน์โหลดไฟล์เสียง
for i, sentence in enumerate(sentences):
    print(f"Processing sentence {i + 1}: {sentence}")
    
    # แปลงข้อความเป็นเสียง
    wav_url = text_to_speech(sentence)
    
    # หากแปลงสำเร็จ ให้ดาวน์โหลดไฟล์เสียงและเก็บไว้ในโฟลเดอร์
    if wav_url:
        filename = f"audio_files/sentence_{i + 1}.wav"
        download_audio(wav_url, filename)
        
        # เพิ่มหน่วงเวลาเพื่อป้องกันการชน Rate Limit
        time.sleep(10)

# # เลือกคำที่ต้องการจากคำที่โหลดมา (เช่น คำแรก)
# text_to_convert = sentences[0]

# # แปลงข้อความเป็นเสียง
# time.sleep(2)
# wav_url = text_to_speech(text_to_convert)

# # หากแปลงสำเร็จ ให้ดาวน์โหลดและเล่นไฟล์เสียง
# if wav_url:
#     download_and_play_audio(wav_url)
