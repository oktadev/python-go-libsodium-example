import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import HexEncoder
import sys

class EncryptFile :
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.sk = PrivateKey(self.get_key(sender, 'sk'), encoder=HexEncoder)
        self.pk = PublicKey(self.get_key(receiver, 'pk'), encoder=HexEncoder)

    def get_key(self, name, suffix):
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

encrypter = EncryptFile('alice', 'bob')
encrypter.encrypt('Jabberwocky.txt', 'message.enc')
print('Done!')
