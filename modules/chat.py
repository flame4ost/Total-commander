from tkinter import *
try:
	import requests as rq
except ImportError:
	print("Install Requirements!")

class chat:
    def __init__(self,rootTitle=""):
        self.root = Tk()
        self.root.title(rootTitle)
        self.root.resizable(0,0)
        self.root.geometry("400x400")
        try:
            self.root.iconbitmap("images\\logo.ico")
        except:
            pass
        self.root.configure(bg="black")
    
    def interface(self):
        #CREATING BASE-FRAME
        self.chatFrame = Frame(self.root,bg="black",width=400,height=400)
        self.chatFrame.pack()

        #CREATING CHAT OPTIONS
        msgEntry = Entry(self.chatFrame,bg="white")
        msgEntry.pack()
        msgEntry.focus()
        

        