from fastapi import FastAPI, Response
import requests
import json
import os

app = FastAPI()

# API key
Apikey = 'mkipQeIRuF90FiQgUAgD4qvRNNMLM9u2'

# URL for the text-to-speech service
url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
headers = {'Apikey': Apikey, 'Content-Type': 'application/json'}

# Function to load sentences from JSON file
def load_sentences(filename='sentences.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['sentences']

# Function to convert text to speech
def text_to_speech(text):
    data = {'input_text': text, 'speaker': 1, 'phrase_break': 0, 'audiovisual': 0}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        wav_url = response.json()['wav_url']
        return wav_url
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Endpoint to serve the audio file when the "Listen" button is clicked
@app.get("/get_audio/{sentence_id}")
def get_audio(sentence_id: int):
    sentences = load_sentences()
    
    if sentence_id >= len(sentences):
        return {"error": "Sentence ID out of range"}
    
    text_to_convert = sentences[sentence_id]  # Get the selected sentence
    
    wav_url = text_to_speech(text_to_convert)
    if wav_url:
        # Download the audio file from the wav_url
        audio_response = requests.get(wav_url, headers={'Apikey': Apikey})
        
        if audio_response.status_code == 200:
            # Serve the audio file for playback
            return Response(content=audio_response.content, media_type="audio/wav")
        else:
            return {"error": "Failed to download audio"}
    return {"error": "Failed to convert text to speech"}
