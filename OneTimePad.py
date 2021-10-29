import sys
import random


class OneTimePad(object):
    def __init__(self, filePath, encrypt=True,  extension="text"):
        self.filePath = filePath
        self.encrypt = encrypt
        self.extension = extension

    def __str__(self):
        return f"{self.filePath}  {self.encrypt}"

    def Encrypt(self, key):
        return "Encrypting File"

    def Decrypt(self, key):
        return "Decrypting File"
