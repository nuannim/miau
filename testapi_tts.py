from aift import setting
 
setting.set_api_key('0niRHCX9q2pEknt3HHKiuWowW6k264Su')


# from aift.nlp import text_cleansing
 
# text = text_cleansing.clean('ข้อความ')

# print(text)

from aift.speech import tts
 
tts('สวัสดีครับ', 'file.wav')
# tts('โอ้ย', 'file2.wav')
