from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

'''Sends a message to whoever texts the number '''

app = Flask(__name__)


@app.route("/", methods= ['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("Welcome to Seidenberg Tech Collective!")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)