from tkinter import *
import os
from modules.essentialSkript import *
from modules.fileSkript import *

actualPath = os.getcwd()
#AutoUpdate
updateSkript()

class Manager(Tk):
    def __init__(self):
        super().__init__()

        self.CODE_VERSION = "0.2.1"
        self.WINDOW_TITLE = "Python File Manager"
        self.FONT = ("Josefin Sans","12","bold")
        self.FONT_UNDELINED = ("Josefin Sans","12","bold","underline")
        
        self.resizable(1,1)
        self.geometry("600x400")
        self.title(" - ".join([self.WINDOW_TITLE,self.CODE_VERSION]))
        try:
            self.iconbitmap("images\\File-Manager-Logo.ico")
        except Exception as exception_error:
            print(exception_error)
        self.configure(bg="black")
        self.Interface()

    def Interface(self):
        self.frame = Frame(self,bg="black")
        self.frame.pack(expand=True,fill=BOTH)

        self.menu = Menu(self)

        file_menu = Menu(self.menu,tearoff = 0)
        file_menu.add_command(label="New File",accelerator="Control+N",command=self.newFile)
        file_menu.add_command(label="New Folder",accelerator="Control+F",command=self.newFolder)
        file_menu.add_command(label="Rename Path",accelerator="F2",command=self.renamePath)
        file_menu.add_command(label="Delete Path",accelerator="Control+D",command=self.deletePath)
        file_menu.add_separator()
        file_menu.add_command(label="Copy Path",command=self.copyPath)

        self.menu.add_cascade(label="File",menu=file_menu)

        help_menu = Menu(self.menu,tearoff = 0)
        help_menu.add_command(label="About[Development]",command=self.About)
        help_menu.add_separator()
        help_menu.add_command(label="Restart Programm",command=restart)
        help_menu.add_command(label="Check Updates",command=updateSkript)

        self.menu.add_cascade(label="Help",menu=help_menu)

        self.configure(menu=self.menu)

        self.backButton()
        self.pathContent()

    def pathContent(self):
        try:
            self.actualPathList.destroy()
        except:
            pass

        self.actualPathList = Listbox(self.frame,bg="black",width=25,fg="#FFC88E",font=self.FONT,bd=0,highlightthickness=0)
    
        list = content(actualPath)
        list = sorted(list, key=str.lower)
        j=1
        for i in list:
            if(os.path.isdir(actualPath+"\\"+i)):
                self.actualPathList.insert(j,i)
                j=j+1
        for i in list:
            if(os.path.isfile(actualPath+"\\"+i)):
                self.actualPathList.insert(j,i)
                j=j+1
                
        self.actualPathList.pack(expand=True,fill=Y)
        self.actualPathList.focus()
        #BIND
        self.actualPathList.bind("<F2>",self.renamePath)
        self.actualPathList.bind("<Control-d>",self.deletePath)
        self.actualPathList.bind("<Double-Button-1>",self.enterList)
        self.actualPathList.bind("<Control-n>",self.newFile)
        self.actualPathList.bind("<Control-f>",self.newFolder)

    def copyPath(self,event=None):
        self.clipboard_clear()
        self.clipboard_append(actualPath)
        self.update()

    def renamePath(self,event=None):
        selection = self.actualPathList.get(ACTIVE)

        def renameNow():
            try:
                rename(actualPath+"\\"+selection,actualPath+"\\"+ent.get())
                print("\n\""+selection + "\" renamed to \"" + ent.get()+"\"\n")
            except:
                print("\nSomething went wrong. Couldn't rename file\n")
            rnPopUp.destroy()
            self.pathContent()
            
        #Popup to take new name
        rnPopUp = Tk()
        rnPopUp.title("Rename")
        rnPopUp.resizable(0,0)
        try:
            rnPopUp.iconbitmap("images\\File-Manager-Logo.ico")
        except:
            pass
        rnPopUp.config(bg="black")
        tempFrame = Frame(rnPopUp,bg="black")
        tempFrame.grid(columnspan=5,rowspan=5)
        Label(tempFrame, text="Enter new name for: "+selection, bg="black", fg="white", font = self.FONT).grid(column=1,row=1,padx=30,pady=10)
        ent = Entry(tempFrame)
        ent.grid(column=1,row=2,padx=30,pady=10)
        ent.focus_force()
        Button(tempFrame, text="Rename",bg="black",fg="white",width=10,command=renameNow,font=self.FONT).grid(column=1,row=3,padx=30, pady=10)
        rnPopUp.mainloop()

    def deletePath(self,event=None):
        selection = self.actualPathList.get(ACTIVE)
        delete(actualPath+"\\"+selection)
        self.actualPathList.delete(ACTIVE)
        print("\n\nDeleted: "+actualPath+"\\"+selection+"\n\n")

    def enterList(self,event=None):
        global actualPath
        selection = self.actualPathList.get(ACTIVE)
        if(os.path.isdir(actualPath+ "\\" +selection)):
            if(actualPath[-1] == "\\"):
                actualPath = actualPath + selection
            else:
                actualPath = actualPath+"\\"+selection
            self.pathContent()
            print(actualPath)
        else:
            print("That's Not A Directory!")

    def backButton(self,event=None):
        backButton = Button(self.frame,command=self.backList,text="BACK",bg="black",fg="#FFC88E",bd=0,font=self.FONT_UNDELINED,width=25)
        backButton.pack()

    def backList(self,event=None):
        global actualPath
        actualPath = os.path.dirname(actualPath)
        print(actualPath)
        self.pathContent()

    def newFile(self,event=None):
        def createFile():
            try:
                makeFile("/".join([actualPath,ent.get()]))
            except:
                print("Cannot create a file")
            nfPopUp.destroy()
            self.pathContent()

        nfPopUp = Tk()
        nfPopUp.title("New File")
        nfPopUp.resizable(0,0)
        try:
            nfPopUp.iconbitmap("images\\File-Manager-Logo.ico")
        except:
            pass
        nfPopUp.config(bg="black")
        tempFrame = Frame(nfPopUp,bg="black")
        tempFrame.grid(columnspan=5,rowspan=5)
        Label(tempFrame, text="Enter File Name with extension: ", bg="black", fg="white", font = self.FONT).grid(column=1,row=1,padx=30,pady=10)
        ent = Entry(tempFrame)
        ent.grid(column=1,row=2,padx=30,pady=10)
        Button(tempFrame, text="Create",bg="black",fg="white",width=10,command=createFile,font=self.FONT).grid(column=1,row=3,padx=30, pady=10)
        nfPopUp.mainloop()

    def newFolder(self,event=None):
        def makeFolder():
            try:
                newDir("/".join([actualPath,ent.get()]))
            except:
                print("Cannot create a folder")
            nfPopUp.destroy()
            self.pathContent()

        nfPopUp = Tk()
        nfPopUp.title("New Folder")
        nfPopUp.resizable(0,0)
        try:
            nfPopUp.iconbitmap("images\\File-Manager-Logo.ico")
        except:
            pass
        nfPopUp.config(bg="black")
        tempFrame = Frame(nfPopUp,bg="black")
        tempFrame.grid(columnspan=5,rowspan=5)
        Label(tempFrame, text="Enter Folder Name: ", bg="black", fg="white", font = self.FONT).grid(column=1,row=1,padx=30,pady=10)
        ent = Entry(tempFrame)
        ent.grid(column=1,row=2,padx=30,pady=10)
        Button(tempFrame, text="Create",bg="black",fg="white",width=10,command=makeFolder,font=self.FONT).grid(column=1,row=3,padx=30, pady=10)
        nfPopUp.mainloop()

    def About(self,event=None):
        pass

Manager = Manager()
Manager.mainloop()

