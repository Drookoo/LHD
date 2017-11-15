from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/", methods= ['GET', 'POST'])
def sms_reply():
    resp = VoiceResponse()

    resp.play('https://demo.twilio.com/docs/classic.mp3')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)