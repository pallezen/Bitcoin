class Transaction:
    def __init__(self, p1PubKey, hashPrevTx, p0Sign):
        self.p1PubKey = p1PubKey
        self.hashPrevTx = hashPrevTx
        self.p0Sign = p0Sign    # p0's private key used to hash information verifiable by its public key
