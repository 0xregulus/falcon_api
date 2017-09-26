import os
import hashlib
import base64

from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key, iv):
        self.bs = 32
        self.key = key
        self.iv = iv

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.decrypt(enc).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


def get_aes_key(password):
    key = hashlib.sha256(password.encode('utf-8')).digest()
    return base64.b32encode(key).decode('utf-8')[:32]

def generate_aes_iv():
    return base64.b32encode(os.urandom(16)).decode('utf-8')
