import sys

lastText = []

def encrypt(msg,key):
    global lastText
    print "Decrypting"
    c = strxor(key, msg)
    c = c.encode('utf8')
    i = 0
    while i+4 < c.__len__():
        print strxor( c[i:i+4], " the ") #XOR with " the " should reveal any text between the strings that have " the " in one of them, but not the other.
        i=i+4

    print
    return c

def strxor(a, b): # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

class CipherDecrypter:

    lastText = []
    def strxor(a, b): # xor two strings of different lengths
        if len(a) > len(b):
            return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
        else:
            return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

    
    def random(size=16):
        return open("/dev/urandom").read(size)

    def main(self):
        fp = open("cipherText.txt", "r")
        MSGS = fp.readlines()
        print "Decrypting Text"
        ciphertexts = [encrypt(MSGS[10], msg) for msg in MSGS]


CipherDecrypter().main()