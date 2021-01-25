
from cryptography.fernet import Fernet
import os
import sys
from tkinter import filedialog, Text

import tkinter as tk
from time import sleep
import base64
import cryptography
import random
status = 00

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

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")

    canvas.pack()


    Label = tk.Label(
        canvas, text=' Welcome to The Crypt,\n to encrypt a file prees the "Encrypt File" button. To decrypt a file, press the "Decrypt File" button. \n [!PLEASE NOTE!]: This is a work in progress desktop application, so expect bugs (and report them to the website!).\n Thank you for using :)')

    Label.pack()
    openFile = tk.Button(root, text="Encrpt File", padx=10,
                        pady=5, fg="white", bg="#263D42", command=newcrypt)
    openFile.pack()
    closefile = tk.Button(root, text="Decrypt File", padx=10,
                        pady=5, fg="white", bg="#263D42", command=readcrypt)
    closefile.pack()

    root.mainloop()



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


def newpass():
    global e1
    string = e1.get() 
    f = open('userdetails.txt', 'w')
    f.write(string)  
    main()
    master.destroy()
def enterpass():
    f = open('userdetails.txt', 'r')
    global password
    password = f.read()
    global e1
    string = e1.get() 
    
    if string==password:
        global auth
        auth = True
        print('Authorised')
    else:
        
        auth = False
    f.close()
    if auth==True:
        main()
        master.destroy()
    else:
        master.destroy()
    



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
f = open('userdetails.txt', 'r')
logindetails = f.read()
f.close()

if logindetails=='':
    status = 0
    message2 = 'Welcome new user, please enter a new password?'
    message2 = str(message2)
else:
    status = 1

# Put this somewhere safe!
file = open('key.key', 'rb')
key = file.read()
file.close()
master = tk.Tk()
canvas = tk.Canvas(master, height=700, width=700, bg="#263D42")

canvas.pack()

if status==0:
    welcomemessage = message2
    label2 = tk.Label(canvas, text=welcomemessage)
    e1 = tk.Entry(master)
    e1.pack()
    e1.focus_set()

    b = tk.Button(master,text='okay',command=newpass)
    b.pack(side='bottom')
    label2.pack()
    master.mainloop()

elif status==1:
    welcomemessage = 'Welcome back, enter your password'
    label2 = tk.Label(canvas, text=welcomemessage)
    e1 = tk.Entry(master)
    e1.pack()
    e1.focus_set()

    b = tk.Button(master,text='okay',command=enterpass)
    b.pack(side='bottom')
    label2.pack()
    master.mainloop()


