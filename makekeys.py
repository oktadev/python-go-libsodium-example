import nacl.utils
from nacl.public import PrivateKey
from nacl.encoding import HexEncoder
import sys

def write(name, hex, sp):
    filename = 'key_' + name + '_' + sp 
    file = open(filename, 'wb')
    file.write(hex)
    file.close()

def makekeys(name):
    sk = PrivateKey.generate()
    write(name, sk.encode(encoder=HexEncoder), 'sk')
    pk = sk.public_key
    write(name, pk.encode(encoder=HexEncoder), 'pk')

if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "name")
    sys.exit()

makekeys(sys.argv[1])