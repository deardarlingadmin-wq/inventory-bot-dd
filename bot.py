
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Dear Darling Inventory Bot is running."

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.form.get("Body", "").strip()

    print(f"Received WhatsApp message: {incoming_msg}", flush=True)

    response = MessagingResponse()
    response.message(
        f"Dear Darling Inventory Bot received: {incoming_msg}"
    )

    print(f"Sending TwiML: {response}", flush=True)

    return Response(str(response), mimetype="text/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
