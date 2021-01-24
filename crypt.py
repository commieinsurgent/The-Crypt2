
from cryptography.fernet import Fernet
import os
import sys
from tkinter import filedialog, Text

import tkinter as tk
from time import sleep
import base64
import cryptography
import random
#    print('[ENCODING]...')
#   encode = message.encode()
sleep(0.5)
#  print('[ENCODE SUCCESSFUL]')
# sleep(0.3)
# print('[ENCRYPTING]...')
# a = Fernet(key)
#    encrypted = a.encrypt(encode)
#   print('ENCRYPT SUCCESSFUL')
#   f.write(encrypted)
#  f.close()


def readcrypt():
    filename2 = filedialog.askopenfilename(
        initialdir='/', title='Select File', filetypes=[("Text files", "*.txt"), ("Documents", "*.doc"), ("Documents (Word)", ("*.docx"))])
    file = open(filename2, 'wb+')

    k2 = Fernet(key)
    decrypted = k2.decrypt(file)

    print(filename2)
    file.write(decrypted)
    print(decrypted)
    file.write(decrypted)
    print('[DECRYPTING]')


def newcrypt():
    filename = filedialog.askopenfilename(
        initialdir='/', title='Select File', filetypes=[("Text files", "*.txt"), ("Documents", "*.doc"), ("Documents (Word)", ("*.docx"))])
    file = open(filename, "wb+")
    coded = file.encode()
    k = Fernet(key)
    filecrypt = k.encrypt(coded)
    file.write(filecrypt)
    file.close()
    print(filename)


# Put this somewhere safe!
file = open('key.key', 'rb')
key = file.read()
file.close()

root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")

canvas.pack()


Label = tk.Label(
    canvas, text=' Welcome to The Crypt,\n to encrypt a file brees the "Encrypt File" button. To decrypt a file, press the "Decrypt File" button. \n [!PLEASE NOTE!]: This is a work in progress desktop application, so expect bugs (and report them to the website!).\n Thank you for using :)')

Label.pack()
openFile = tk.Button(root, text="Encrpt File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=newcrypt)
openFile.pack()
closefile = tk.Button(root, text="Decrypt File", padx=10,
                      pady=5, fg="white", bg="#263D42", command=readcrypt)
closefile.pack()

root.mainloop()
