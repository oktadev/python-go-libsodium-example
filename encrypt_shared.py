import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import HexEncoder
from nacl.secret import SecretBox
import sys

class Encrypter :
    def __init__(self):
        file = open('key_secret', 'rb')
        self.key = file.read()
        file.close()

    def encrypt(self, textfile, encfile):
        box = SecretBox(self.key)
        tfile = open(textfile, 'rb')
        text = tfile.read()
        tfile.close()
        etext = box.encrypt(text)
        efile = open(encfile, 'wb')
        efile.write(etext)
        efile.close()

encrypter = Encrypter()
encrypter.encrypt('Jabberwocky.txt', 'message.sec')
print('Done!')
