from gtts import gTTS
from playsound import playsound
from googletrans import Translator

audio = "audio.mp3"
lenguage = "pt-br"
lenguage2 = "en-us"


def play():

    escreva = input("digite pt para portugues ou en para english\n")
    tradutor = Translator()
    if escreva == "en":
        esse = tradutor.translate(input(), dest="en").text
        print(esse)
        sp = gTTS(
            text=esse,
            lang=lenguage2)
        sp.save(audio)
        playsound(audio)
    elif escreva == "pt":
        esse = tradutor.translate(input(), dest="pt").text
        print(esse)
        sp = gTTS(
            text=esse,
            lang=lenguage)
        sp.save(audio)
        playsound(audio)

play()