from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Dear Darling Inventory Bot is running."

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.form.get("Body", "").strip()

    response = MessagingResponse()

    if incoming_msg:
        response.message(
            f"Dear Darling Inventory Bot received: {incoming_msg}"
        )
    else:
        response.message("I received your message.")

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
