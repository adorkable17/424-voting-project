from tkinter import *
from tkinter import messagebox
import os
import binascii
import Crypto.Random
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from PIL import Image, ImageTk

def GetEmployeeID(option):
    f = open("myfile.txt", "w")
    f.write(option)
    f.close()
    
def GetCandidate(option):
    option = str(option.get())
    f = open("myfile.txt", "a")
    f.write("\n" + option)
    f.close()

def encrypt():
    key=binascii.hexlify(os.urandom(16))
    iv=Crypto.Random.get_random_bytes(16) 
    with open("votekey.key","wb") as file:
        file.write(key)
        file.write(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open("myfile.txt", "rb") as f:
        byteblock = f.read()
    ciphertext = cipher.encrypt(pad(byteblock, AES.block_size))
    f = open("myfile_EN.txt", "wb")
    f.write(ciphertext)

def on_closing():
    if messagebox.askokcancel("Quit", "Are you done voting?"):
        L1.destroy()
        E1.destroy()
        L3.destroy()
        R1.destroy()
        R2.destroy()
        R3.destroy()
        B.destroy()

top = Tk()
top.title("WadePoll")
var = IntVar()

L1 = Label(top, text = "Voter Employee ID:")
L1.pack(anchor = NW)
E1 = Entry(top, bd = 5)
E1.pack(anchor = NW)
L3 = Label(top, text = "Choose a Candidate:")
L3.pack(anchor = NW)

R1 = Radiobutton(top, text = "Candidate1", variable = var, value = 12345678)
R1.pack( anchor = W )
R2 = Radiobutton(top, text = "Candidate2", variable = var, value = 23456789)
R2.pack( anchor = W )
R3 = Radiobutton(top, text = "Candidate3", variable = var, value = 34567890)
R3.pack( anchor = W)

def callBack():
    VoterID = E1.get()
    GetEmployeeID(VoterID)
    GetCandidate(var)
    encrypt()
    on_closing()
    L2 = Label(top, text= "Thank you for using the WadePoll!")
    L2.config(font=("Comic Sans MS", 44))
    L2.pack(anchor = N)
    load = Image.open("finalpicture.png")
    render = ImageTk.PhotoImage(load)
    img = Label(top, image=render)
    img.image = render
    img.pack(anchor = CENTER)
    
B = Button(top, text = "Submit", command = callBack)
B.place(x = 50,y = 50)
B.pack(anchor = S)

top.mainloop()