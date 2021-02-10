import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from nacl.encoding import HexEncoder
from nacl.secret import SecretBox
import sys

class Encoder :
    def __init__(self):
        self.key = nacl.utils.random(SecretBox.KEY_SIZE)
        file = open('key_secret', 'wb')
        file.write(self.key)
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

encode = Encoder()
encode.encrypt('Jabberwocky.txt', 'message.sec')
print('Done!')
