class Person:
    def __init__(self, privateKey, publicKey, coins):
        self.privateKey = privateKey
        self.publicKey = publicKey
        self.coins = coins
        self.info = "Private key: " + str(self.privateKey) + " Public Key: " + str(self.publicKey) + " Coins: " + str(self.coins)

class Transaction:
    def __init__(self, p1PubKey, hashPrevTx, p0Sign, id):
        self.p1PubKey = p1PubKey
        self.hashPrevTx = hashPrevTx
        self.p0Sign = p0Sign    # p0's private key used to hash information verifiable by its public key
        self.id = id

def hash(n):
    return n*9876+7

kal = Person(1000, 1/1000, 100)
ray = Person(1/50, 50, 20)

tx50 = Transaction(ray.publicKey, 2345, hash(kal.privateKey), 50)
tx51 = Transaction(kal.publicKey, hash(tx50.id), hash(ray.privateKey), tx50.id+1)

print(tx51.hashPrevTx)
print(kal.info)
