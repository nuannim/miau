import re
import os
import requests
import json
import librosa
import numpy as np
import soundfile as sf
# from google.colab import drive
# drive.mount('/content/gdrive')
# import IPython.display as ipd
# ipd.Audio('C:/Users/noey/Desktop/github repo/miau/Python3/audiotest.wav') # load a local WAV file

url = "https://api.aiforthai.in.th/partii-webapi"
files = {'wavfile': (f'temp.wav', open(f'C:/Users/noey/Desktop/github repo/miau/Python3/audiotest.wav', 'rb'), 'audio/wav')}
headers = {
    'Apikey': "Zvm3yLtP2nK6McN0i6nOU5inHFWVVdHu",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
}

param = {"outputlevel": "--uttlevel", "outputformat": "--txt"}
response = requests.request(
    "POST", url, headers=headers, files=files, data=param)
ret = response.json()
print(ret["message"])