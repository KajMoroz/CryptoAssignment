import sys

spaceList = []

def decrypt(msg,key):
    global lastText

    spaces = []

    c = strxor(key, msg)
    c = c.encode("hex")
    i=0
    while i < len(c):
        if int((c[i:i+2]), 16) < 65:
            print chr(int((c[i:i+2]), 16)+97),
        else:
            print (int(c[i:i+2], 16)),
            spaces.append(i)
        i = i+2

    print

    spaceList.append(spaces)
    return c

def strxor(a, b): # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

class CipherDecrypter:

    lastText = []


    def main(self):
        fp = open("cipherText.txt", "r")
        MSGS = fp.readlines()
        lastMsg = []
        print "Decrypting Text"
        for msg in MSGS:
            if lastMsg != []:
                decrypt(msg,lastMsg)
            lastMsg = msg

        #print "Cipher 10 and 9"
       # ciphertexts = [decrypt(MSGS[10], MSGS[9])]
        #print "Cipher 10 and 8"
        #ciphertexts = [decrypt(MSGS[10], MSGS[8])]
        #print "Cipher 9 and 8"
        #ciphertexts = [decrypt(MSGS[9], MSGS[8])]

        print spaceList

CipherDecrypter().main()