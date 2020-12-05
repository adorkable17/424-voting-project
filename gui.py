from tkinter import *
from tkinter import messagebox
import os
import binascii
import Crypto.Random
from Crypto.Cipher import AES

def GetEmployeeID(option):
    f = open("myfile.txt", "w")
    f.write(option)
    f.close()

def AddBS():
    option = 123456789087654323751937457192384691237401234238423423748237472346278364923746298374283746127384682374692374692387462837461923741293746238429346239847621384762198374612834698123746798236498137462798569347613984168923746128973641827364982374398
    f = open("myfile.txt", "a")
    f.write("\n" + str(option))
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
    pad = len(byteblock)%16 * -1
    byteblock_trimmed = byteblock[64:pad]
    ciphertext = cipher.encrypt(byteblock_trimmed)
    ciphertext = byteblock[0:64] + ciphertext + byteblock[pad:]
    f = open("myfile.txt", "wb")
    f.write(ciphertext)

def on_closing():
    if messagebox.askokcancel("Quit", "Are you done voting?"):
        L1.destroy()
        E1.destroy()
        R1.destroy()
        R2.destroy()
        R3.destroy()
        B.destroy()

top = Tk()
top.title("WadePoll")
var = IntVar()

L1 = Label(top, text = "Voter Employee ID")
L1.pack(anchor = NW)
E1 = Entry(top, bd = 5)
E1.pack(anchor = NW)

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
    AddBS()
    encrypt()
    on_closing()
    # canvas = Canvas(top, width = 300, height = 300)      
    # canvas.pack()
    # img = PhotoImage(file="finalpicture.ppm")      
    # canvas.create_image(anchor=CENTER, image=img)
    # L2 = Label(top, text = "Thanks for using the WadePoll!")
    
B = Button(top, text = "Submit", command = callBack)
B.place(x = 50,y = 50)
B.pack(anchor = S)

top.mainloop()