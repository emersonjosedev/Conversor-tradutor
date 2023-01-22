from gtts import  gTTS
from playsound import playsound

audio = "audio.mp3"
lenguage = "pt-br"
escreva = input("Escreva e para ter sua frase em audio")
la_ele = "la ele"
sp = gTTS(
    text=la_ele,
    lang=lenguage
)
sp.save(audio)
playsound(audio)