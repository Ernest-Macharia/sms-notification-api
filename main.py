from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1144b5e640b36681426e3bb4f7a4f6b4"
# Your Auth Token from twilio.com/console
auth_token  = "956e74e0f9acd7c2bbb5755f37a6ee0e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+254713028761", 
    from_="+254710992763",
    body="Shiru enda ulale")

print(message.sid)
