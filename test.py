import requests

import IPython.display as ipd
ipd.Audio('test.wav') # load a local WAV file

url = "https://api.aiforthai.in.th/partii-webapi"

files = {'wavfile':open('test.wav','rb')}

headers = {
        'Apikey': "DqcTil6kS0ivPoFQi8H84D6J0CHZrh20",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
}

# param = {"format":"json"}
# response = requests.request("POST", url, headers=headers, files=files, data=param)
# print("Result=" + response.text)

param = {"outputlevel": "--uttlevel", "outputformat": "--txt"}
response = requests.request(
    "POST", url, headers=headers, files=files, data=param)
ret = response.json()
print(ret["message"])