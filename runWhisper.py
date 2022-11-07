import whisper

model = whisper.load_model("base")
def runWisper(filePath):
    out = model.transcribe(filePath)
    return out['text']

    