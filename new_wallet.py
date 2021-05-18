import secrets

class wallet:
    def __init__(self):
        self.private_address = secrets.randbits(256)
        print(self.private_address)
