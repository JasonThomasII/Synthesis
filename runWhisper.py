import whisper
import eel 

model = whisper.load_model("base")

@eel.expose
def runWisper(filePath):
    out = model.transcribe(filePath)
    return out['text']
