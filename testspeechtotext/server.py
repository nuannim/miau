from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
import wave
import io
import os

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
            
        return JSONResponse(
            content={"message": f"File successfully saved to {file_path}"}, 
            status_code=200
        )

        # # Log the first few bytes of the file content to check the format 
        # print(file_content[:20]) 
        # # Process the WAV file in-memory 
        # try: 
        #     audio_stream = io.BytesIO(file_content) 
        #     with wave.open(audio_stream, 'rb') as wf: 
        #         print("Number of channels:", wf.getnchannels()) 
        #         print("Sample width:", wf.getsampwidth()) 
        #         print("Frame rate:", wf.getframerate()) 
        #         print("Number of frames:", wf.getnframes()) 
        #         print("Parameters:", wf.getparams()) 
                
        #         # You can now work with the audio data in your Python code 
        #         return JSONResponse(content={"message": "File successfully processed"}, status_code=200) 
        # except wave.Error as e: 
        #     return JSONResponse(content={"message": f"Error processing file: {e}"}, status_code=400)

        # # Process the WAV file in-memory
        # audio_stream = io.BytesIO(file_content)
        # with wave.open(audio_stream, 'rb') as wf:
        #     print("Number of channels:", wf.getnchannels())
        #     print("Sample width:", wf.getsampwidth())
        #     print("Frame rate:", wf.getframerate())
        #     print("Number of frames:", wf.getnframes())
        #     print("Parameters:", wf.getparams())

        # # You can now work with the audio data in your Python code
        
        # return JSONResponse(content={"message": "File successfully processed"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
