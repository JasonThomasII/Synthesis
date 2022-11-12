import eel
import whisper

# eel isn't going to work. Lets try electron next.
#https://www.youtube.com/watch?v=627VBkAhKTc


model = whisper.load_model("base")

@eel.expose
def hello():
    print("hello world")

@eel.expose
def runWisper(filePath):
    out = model.transcribe(filePath)
    return out['text']


eel.init("app")
eel.start("index.html")