# pip install pytsx3
# pip install pywin32
import pyttsx3

data = input("\nenter the text to covert to speech::")

engin = pyttsx3.init()
engin.say(data)
# engin.say("hello kashi bhattarai")
engin.runAndWait()