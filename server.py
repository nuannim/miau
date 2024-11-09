from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
import os

import requests
import numpy as np
import soundfile as sf

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
app.mount("/static", StaticFiles(directory="C:/Users/noey/Desktop/github repo/miau/front"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_html():
    with open("C:/Users/noey/Desktop/github repo/miau/front/test.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.filename == '':
        return JSONResponse(content={"message": "No selected file"}, status_code=400)
    if file:
        file_content = await file.read()

        file.read() # Specify the directory where you want to save the file 
        save_directory = "C:/Users/noey/Desktop/github repo/miau/Python3" 
        os.makedirs(save_directory, exist_ok=True) 
        file_path = os.path.join(save_directory, file.filename) 
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

        return JSONResponse(content={"message": "File successfully processed"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
