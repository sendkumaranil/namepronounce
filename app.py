from flask import Flask, Response
from gtts import gTTS

app = Flask(__name__)

@app.route("/name/<string:name>")
def streamwav(name):
    def generate():
        language = 'en'
        mySpeech = gTTS(text=name,lang=language,slow=False)
        mySpeech.save('speechname.mp3')
        with open("speechname.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-mp3")

if __name__ == "__main__":
    app.debug = False
    app.run()