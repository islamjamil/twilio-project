from twilio.rest import Client
import json

with open("private.json") as private:
    credentials = json.load(private)

account_sid = credentials["account_sid"]
auth_token = credentials["auth_token"]
messaging_sid = credentials["messaging_sid"]
number = credentials["phone_number"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid=messaging_sid,
    body="Testing from Jamil!!",
    to=number,
    # mount rainier
    # media_url="https://upload.wikimedia.org/wikipedia/commons/e/eb/Mount_Rainier_from_west.jpg"
)

print(message.sid)
