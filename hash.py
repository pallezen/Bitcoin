import hashlib
input_string = "Test"

class hasher:

    def __init__(self, input_string):
        self.input_string = hashlib.md5(input_string.encode())

    def hash(input_string):
        return(hashlib.md5(input_string.encode()).hexdigest())
