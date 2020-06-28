from gtts import gTTS
from datetime import datetime
import winsound

input_text = input("Enter the text")

language = 'en'

myobj = gTTS(text=input_text, lang=language, slow=False)

current_date = datetime.now()
timestamp = current_date.strftime("%m-%d-%Y-%H-%M-%S")
song = timestamp+".mp3"
myobj.save(song)



from playsound import playsound
playsound(song)
