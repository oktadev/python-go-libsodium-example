import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import HexEncoder
import sys

class Encoder :
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.sk = PrivateKey(self.getKey(sender, 'sk'), encoder=HexEncoder)
        self.pk = PublicKey(self.getKey(receiver, 'pk'), encoder=HexEncoder)

    def getKey(self, name, suffix):
        filename = 'key_' + name + '_' + suffix
        file = open(filename, 'rb')
        data = file.read()
        file.close()
        return data

    def encrypt(self, textfile, encfile):
        box = Box(self.sk, self.pk)
        tfile = open(textfile, 'rb')
        text = tfile.read()
        tfile.close()
        etext = box.encrypt(text)
        efile = open(encfile, 'wb')
        efile.write(etext)
        efile.close()

encode = Encoder('alice', 'bob')
encode.encrypt('Jabberwocky.txt', 'message.enc')
print('Done!')
