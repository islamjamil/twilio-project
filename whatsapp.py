from twilio.rest import Client
import json

with open("private.json") as private:
    credentials = json.load(private)

account_sid = credentials["account_sid"]
auth_token = credentials["auth_token"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    # twilio's whatsapp number below
    from_='whatsapp:+14155238886',
    body='Your appointment is coming up on July 21 at 3PM',
    to=F'whatsapp:+{credentials["phone_number"]}'
)

print(message.sid)
