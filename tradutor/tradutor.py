from googletrans import Translator


tradutor = Translator()
#escreva = input("escreva")

esse = tradutor.translate(input(), dest="en").text
print(esse)
