from abc import ABC, abstractmethod


class MessageNotifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(MessageNotifier):
    def send(self, message):
        super().send(message)
        print(f"[+] Sending email with msg {message}")


class SMS(MessageNotifier):
    def send(self, message):
        super().send(message)
        print(f"[+] Sending sms with msg {message}")


class SLACK(MessageNotifier):
    def send(self, message):
        super().send(message)
        print(f"[+] Sending slack with msg {message}")


class Notifier:
    def __init__(self, message_service: MessageNotifier):
        self.message_service = message_service
    
    def send(self, message):
        self.message_service.send(message)
        

email_notifier = Notifier(message_service=Email())
slack_notifier = Notifier(message_service=SLACK())
sms_notifier = Notifier(message_service=SMS())


email_notifier.send("Hello email")
slack_notifier.send("Hello Slack")
sms_notifier.send("Hello sms")



