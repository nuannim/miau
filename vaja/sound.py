import requests
import IPython
import json
 
#ระบุ api key
Apikey='mkipQeIRuF90FiQgUAgD4qvRNNMLM9u2'
 
# สังเคราะห์เสียง
url = 'https://api.aiforthai.in.th/vaja9/synth_audiovisual'
headers = {'Apikey':Apikey,'Content-Type' : 'application/json'}

# ฟังก์ชันสำหรับโหลดคำจากไฟล์ JSON
def load_sentences(filename='sentences.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['sentences']

text = 'ข้อความที่ต้องการสังเคราะห์เสียง'
data = {'input_text':text,'speaker': 1, 'phrase_break':0, 'audiovisual':0}
response = requests.post(url, json=data, headers=headers)
print(response.json())
 
# ดาวน์โหลดไฟล์เสียง
resp = requests.get(response.json()['wav_url'],headers={'Apikey':Apikey})
if resp.status_code == 200:
  with open('test.wav', 'wb') as a:
    a.write(resp.content)
    print('Downloaded: ')
    IPython.display.display(IPython.display.Audio('test.wav'))
else:
  print(resp.reason)