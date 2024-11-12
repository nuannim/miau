from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from fastapi.middleware.cors import CORSMiddleware
import os

import requests
import numpy as np
import soundfile as sf

from aift import setting 
from aift.speech import tts

import json

setting.set_api_key('mkipQeIRuF90FiQgUAgD4qvRNNMLM9u2')

# tts.convert('สวัสดีครับ', 'file.wav')

app = FastAPI()

# Allow all CORS origins, methods, and headers (for development purposes) 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["*"], # Change this to specify allowed origins in production 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 

# Mount a directory of static files (such as the HTML file)
app.mount("/css", StaticFiles(directory="front/css"), name="css")
app.mount("/images", StaticFiles(directory="front/images"), name="images")
template = Jinja2Templates(directory="front")

@app.get("/", response_class=HTMLResponse)
async def serve_html(request : Request):
    return template.TemplateResponse(
        "index.html", 
        {"request": request}
    )

@app.post("/upload")
async def upload_file(file_stt: UploadFile = File(...)):
    if file_stt.filename == '':
        return JSONResponse(content={"message": "No selected file_stt"}, status_code=400)
    if file_stt:
        file_content = await file_stt.read()

        file_stt.read() # Specify the directory where you want to save the file 
        save_directory = "C:/Users/noey/Desktop/github repo/miau/Python3" 
        os.makedirs(save_directory, exist_ok=True) 
        file_path = os.path.join(save_directory, file_stt.filename) 
        # Save the file to the specified location 
        with open(file_path, "wb") as f: 
            f.write(file_content) 

        url = "https://api.aiforthai.in.th/partii-webapi"
        files = {'wavfile': (f'temp.wav', open(f'C:/Users/noey/Desktop/github repo/miau/Python3/audio.wav', 'rb'), 'audio/wav')}
        headers = {
            'Apikey': "Zvm3yLtP2nK6McN0i6nOU5inHFWVVdHu",
            'Cache-Control': "no-cache",
            'Connection': "keep-alive",
        }

        param = {"outputlevel": "--uttlevel", "outputformat": "--txt"}
        response = requests.request(
            "POST", url, headers=headers, files=files, data=param)
        ret = response.json()
        # print(ret["message"])
        word = ret["message"]
        word = word.replace(" ", "")
        print(word)

        # if word == ('สวัสดี'):
        #     print(True)
        # else:
        #     print(False)

        return JSONResponse(content={"message": word}, status_code=200)

@app.post("/play_audio")
async def play_audio(index : int = Form(...)):
    # mylist = ["สวัสดี", "วันปีใหม่", "น้องคะ"]
    with open('front/css/sentences.json', 'r', encoding='utf-8') as f: 
        data = json.load(f) 
        mylist = data['sentences'] 
        word = mylist[index] # Process the word 
        # tts.convert(word, "file.wav")

        print('word :', word)
    
        import os

        Apikey = '0niRHCX9q2pEknt3HHKiuWowW6k264Su'

        # สังเคราะห์เสียง
        url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
        headers = {'Apikey': Apikey, 'Content-Type': 'application/json'}
        text = "สวัสดี"  # Replace this with the actual text you want to process
        data = {'input_text': text, 'speaker': 1, 'phrase_break': 0, 'audiovisual': 0}
        response = requests.post(url, json=data, headers=headers)
        print(response.json())

        # Create the downloads directory if it doesn't exist
        download_dir = 'C:/Users/noey/Desktop/github repo/miau/Python3'
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # # ดาวน์โหลดไฟล์เสียง
        # resp = requests.get(response.json()['wav_url'], headers={'Apikey': Apikey})
        # if resp.status_code == 200:
        #     file_path = os.path.join(download_dir, 'file.wav')
        #     with open(file_path, 'wb') as a:
        #         a.write(resp.content)
        #         print(f'Downloaded: {file_path}')
        #         # IPython.display.display(IPython.display.Audio(file_path))
        # else:
        #     print(resp.reason)
        if (response.json()['msg'] == 'success'):
            with open('test.wav', 'wb') as a:
                resp = requests.get(response.json()['wav_url'],headers={'Apikey':Apikey})
                if resp.status_code == 200:
                    a.write(resp.content)
                    print('Downloaded: '+response.json()['wav_url'])
                    # IPython.display.display(IPython.display.Audio('test.wav'))
                else:
                    print(resp.reason)
                    exit(1)







    return

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
