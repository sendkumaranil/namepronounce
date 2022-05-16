from flask import Flask,request,Response
from gtts import gTTS

app = Flask(__name__)

@app.route("/name/<string:name>")
def streamwav(name):
    language = request.args.get('language')
    def generate():
        reqLanguage = language
        splitLang = reqLanguage.split("@")
        mySpeech = gTTS(text=name,lang=splitLang[0],tld=splitLang[1],slow=False)
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