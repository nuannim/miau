from fastapi import FastAPI, Response
import requests
import json
import IPython

app = FastAPI()

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

# สร้าง endpoint สำหรับการแปลงข้อความเป็นเสียง
@app.get("/get_audio")
def get_audio():
    sentences = load_sentences()
    text_to_convert = sentences[0]  # ใช้คำแรกจากไฟล์ JSON

    wav_url = text_to_speech(text_to_convert)
    if wav_url:
        # ดาวน์โหลดไฟล์เสียงจาก wav_url
        audio_response = requests.get(wav_url, headers={'Apikey': Apikey})
        
        if audio_response.status_code == 200:
            return Response(content=audio_response.content, media_type="audio/wav")
        else:
            return {"error": "Failed to download audio"}
    return {"error": "Failed to convert text to speech"}
