import hashlib

class hasher:
    
    def hash(self, mystring):
        self.mystring = hashlib.md5(mystring.encode())
        return(self.mystring.hexdigest())
