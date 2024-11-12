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

import myList

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

@app.post("/send_index")
async def receive_index(index : int = Form(...)):
    print('recieve index : %s' %(index))
    print(myList.mylist)
    wordIndex = myList.mylist[index]

    print(wordIndex)
    return JSONResponse(
                        content={"message2" : wordIndex},
                        status_code=200
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
