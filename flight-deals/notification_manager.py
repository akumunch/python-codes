from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self,msg:str,to:str):
        self.msg=msg
        self.to=to
        self.account_sid=os.environ.get("ACCOUNT_SID")
        self.auth_token=os.environ.get("AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
    def send_message(self):
        self.message=self.client.messages.create(
            body=self.msg,from_="whatsapp:+14155238886",
            to=f"whatsapp:{self.to}"
            )
        print(self.message.status)
            