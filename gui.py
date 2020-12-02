from tkinter import *
from tkinter import messagebox

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
    print("it works")

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

R1 = Radiobutton(top, text = "Candidate1", variable = var, value = 1) # values will be replaced with employee idea
R1.pack( anchor = W )
R2 = Radiobutton(top, text = "Candidate2", variable = var, value = 2)
R2.pack( anchor = W )
R3 = Radiobutton(top, text = "Candidate3", variable = var, value = 3)
R3.pack( anchor = W)

def callBack():
    VoterID = E1.get()
    GetEmployeeID(VoterID)
    GetCandidate(var)
    encrypt()
    on_closing()
    canvas = Canvas(top, width = 300, height = 300)      
    canvas.pack()
    img = PhotoImage(file="finalpicture.ppm")      
    canvas.create_image(anchor=CENTER, image=img)
    L2 = Label(top, text = "Thanks for using the WadePoll!")
    
B = Button(top, text = "Submit", command = callBack)
B.place(x = 50,y = 50)
B.pack(anchor = S)

top.mainloop()