


class Notifier:
    def send(self, type_, message):
        if type_ == "email":
            print(f"Sending Email: {message}")