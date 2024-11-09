from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import wave
import io

app = FastAPI()

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

        # Process the WAV file in-memory
        audio_stream = io.BytesIO(file_content)
        with wave.open(audio_stream, 'rb') as wf:
            print("Number of channels:", wf.getnchannels())
            print("Sample width:", wf.getsampwidth())
            print("Frame rate:", wf.getframerate())
            print("Number of frames:", wf.getnframes())
            print("Parameters:", wf.getparams())

        # You can now work with the audio data in your Python code
        
        return JSONResponse(content={"message": "File successfully processed"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
