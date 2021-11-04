# -*- coding: utf-8 -*-
import sys
import random
import pyperclip


class OneTimePad(object):
    SYMBOLS = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}' + '’“”'
    SYMBOLSLIST = list(SYMBOLS)

    def __init__(self, filePath):
        self.filePath = filePath
        self.key = None
        self.content = None
        self.encryptedContent = None
        self.decryptedContent = None

    def __str__(self):
        return self.filePath

    def ContentValidation(self):
        self.content = self.content.replace(
            '\n', '~')  # ~ symbol represents \n
        for i in self.content:
            if i != " ":
                if i != '~':
                    if i not in self.SYMBOLS:
                        message = "{} Unrecognized character. The input must not contain non-ASCII characters".format(
                            i)
                        print(message)
                        sys.exit()
        return True

    def GenerateKey(self):
        key = ""
        for i in self.content:
            if i != " ":
                keyValue = self.SYMBOLS[random.randint(
                    0, len(self.SYMBOLS) - 1)]
                while keyValue in ["'", '"']:
                    keyValue = self.SYMBOLS[random.randint(
                        0, len(self.SYMBOLS) - 1)]
                key += keyValue
            else:
                key += " "
        return key

    def Encrypt(self):
        file = open(self.filePath, 'r')
        self.content = file.read()
        file.close()

        self.key = list(self.GenerateKey())
        self.ContentValidation()
        self.encryptedContent = ""
        for ContentValue, KeyValue in zip(self.content, "".join(self.key)):
            if ContentValue != " ":
                if ContentValue != "~":
                    keyIndex = (self.SYMBOLS.find(ContentValue) +
                                self.SYMBOLS.find(KeyValue)) % len(self.SYMBOLSLIST)
                    self.encryptedContent += self.SYMBOLSLIST[keyIndex]
                else:
                    self.encryptedContent += "~"  # werid symbol represents \n
            else:
                self.encryptedContent += " "
        file = open(self.filePath, 'w')
        file.write(self.encryptedContent)
        file.close()


    def Decrypt(self, key):
        file = open(self.filePath, 'r')
        self.content = file.read()
        file.close()
        self.key = key

        self.decryptedContent = ""
        for encryptedContent, KeyValue in zip(self.content, "".join(self.key)):
            if encryptedContent != " ":
                if encryptedContent != "~":  # Weird symbol represents \n
                    keyIndex = (self.SYMBOLS.find(encryptedContent) -
                                self.SYMBOLS.find(KeyValue)) % len(self.SYMBOLS)
                    self.decryptedContent += self.SYMBOLSLIST[keyIndex]
                else:
                    self.decryptedContent += "\n"
            else:
                self.decryptedContent += " "

        file = open(self.filePath, 'w')
        file.write(self.decryptedContent)
        file.close()