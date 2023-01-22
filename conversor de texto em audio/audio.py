from gtts import gTTS
from playsound import playsound

audio = "audio.mp3"
lenguage = "pt-br"
lenguage2 = "en-us"
la_ele_mil_vezes = "la ele "

sp = gTTS(
    text=la_ele_mil_vezes,
    lang=lenguage)
sp.save(audio)


while True:
    playsound(audio)


