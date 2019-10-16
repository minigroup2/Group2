from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    print('TESTING ENCRYPTION')
    fr=input("Enter the frame name with extension..:")
    msg=input('Message...: ')
    pwd=input('Password..: ')
    text=AESCipher(pwd).encrypt(msg).decode('utf-8')
    print('Ciphertext:',text)

    from stegano import lsb


    secret=lsb.hide("C:/Users/jithu/PycharmProjects/j/im/"+fr,text)
    sa=input("Enter the image name with extension to be saved..:")
    secret.save("./im/"+sa)
    clear_message = lsb.reveal("C:/Users/jithu/PycharmProjects/j/im/"+sa)
    print("successfully inserted text= ",clear_message)



"""
    print('\nTESTING DECRYPTION')
    clear_message = lsb.reveal("C:/Users/jithu/PycharmProjects/j/im/"+sa)
    print("Ciphertext....",clear_message)
    cte=clear_message

    #cte = input('Ciphertext: ')
    pwd = input('Password..: ')
    print('Message...:', AESCipher(pwd).decrypt(cte).decode('utf-8'))
"""