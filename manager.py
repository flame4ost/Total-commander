try:
    import os
    from tkinter import *
    from modules import essentialSkript
    from modules import fileSkript
except ImportError:
    print("Installing requirements")
    os.system("pip install -r requirements.txt")
    os.system("manager.py")
    exit()




#AUTO-UPDATE
essentialSkript.updateSkript()

codeVersion = "(0.1.7.1)"
actualPath = os.getcwd()
actualPathList = None

class creatingRoot:

    def __init__(self,rootTitle):
        self.root = Tk()
        self.root.title(rootTitle)
        self.root.resizable(0,0)
        try:
            self.root.iconbitmap("images\File-Manager-Logo.ico")
        except:
            pass
        self.root.configure(bg="black")

    def pathContent(self):
        global actualPathList
        actualPathList = Listbox(self.baseFrame,bg="black",fg="red",width=20,height=12)
    
        list = fileSkript.content(actualPath)
        list = sorted(list, key=str.lower)
        j=1
        for i in list:
            if(os.path.isdir(actualPath+"\\"+i)):
                actualPathList.insert(j,i)
                j=j+1
        for i in list:
            if(os.path.isfile(actualPath+"\\"+i)):
                actualPathList.insert(j,i)
                j=j+1
                
        actualPathList.focus()
        actualPathList.grid(column=0,row=1,padx=10,pady=10)


    def backList(self):
        global actualPath
        actualPath = os.path.dirname(actualPath)
        print(actualPath)
        self.pathContent()
        self.label1.config( text="Path:\n" + actualPath, bg="black",justify=CENTER, fg="white",width=40, font = ("Sansita One",10,"bold"))

    def deleteList(self):
        selection = actualPathList.get(ACTIVE)
        fileSkript.delete(actualPath+"\\"+selection)
        actualPathList.delete(ACTIVE)
        print("\n\nDeleted: "+actualPath+"\\"+selection+"\n\n")

    def enterList(self):
        global actualPath
        selection = actualPathList.get(ACTIVE)
        if(os.path.isdir(actualPath+ "\\" +selection)):
            if(actualPath[-1] == "\\"):
                actualPath = actualPath + selection
            else:
                actualPath = actualPath+"\\"+selection
            self.pathContent()
            print(actualPath)
            self.label1.config( text="Path:\n" + actualPath, bg="black",justify=CENTER, fg="white",width=40, font = ("Sansita One",10,"bold"))
        else:
            print("That's Not A Directory!")

    def renameFun(self):
        selection = actualPathList.get(ACTIVE)

        def renameNow():
            try:
                fileSkript.rename(actualPath+"\\"+selection,actualPath+"\\"+ent.get())
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
            rnPopUp.iconbitmap("images\\logo.ico")
        except:
            pass
        rnPopUp.config(bg="black")
        tempFrame = Frame(rnPopUp,bg="black")
        tempFrame.grid(columnspan=5,rowspan=5)
        Label(tempFrame, text="Enter new name for: "+selection, bg="black", fg="white", font = ("Sansita One",10,"bold")).grid(column=1,row=1,padx=30,pady=10)
        ent = Entry(tempFrame)
        ent.grid(column=1,row=2,padx=30,pady=10)
        Button(tempFrame, text="Rename",bg="black",fg="white",width=10,command=renameNow,font=("Sansita One",10,"bold")).grid(column=1,row=3,padx=30, pady=10)
        rnPopUp.mainloop()

    def copyClip(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(actualPath)
        self.root.update()

    def newFolder(self):
        def makeFolder():
            try:
                print(actualPath)
                fileSkript.newDir(actualPath + "\\" +  ent.get())
            except:
                print("Cannot create a folder")
            nfPopUp.destroy()
            self.pathContent()

        nfPopUp = Tk()
        nfPopUp.title("New Folder")
        nfPopUp.resizable(0,0)
        try:
            nfPopUp.iconbitmap("images\\logo.ico")
        except:
            pass
        nfPopUp.config(bg="black")
        tempFrame = Frame(nfPopUp,bg="black")
        tempFrame.grid(columnspan=5,rowspan=5)
        Label(tempFrame, text="Enter Folder Name: ", bg="black", fg="white", font = ("Sansita One",10,"bold")).grid(column=1,row=1,padx=30,pady=10)
        ent = Entry(tempFrame)
        ent.grid(column=1,row=2,padx=30,pady=10)
        Button(tempFrame, text="Create",bg="black",fg="white",width=10,command=makeFolder,font=("Sansita One",10,"bold")).grid(column=1,row=3,padx=30, pady=10)
        nfPopUp.mainloop()

    def newFile(self):
        def makeFile():
            try:
                fileSkript.makeFile(actualPath + "\\" + ent.get())
            except:
                print("Cannot create a file")
            nfPopUp.destroy()
            self.pathContent()

        nfPopUp = Tk()
        nfPopUp.title("New File")
        nfPopUp.resizable(0,0)
        try:
            nfPopUp.iconbitmap("images\\logo.ico")
        except:
            pass
        nfPopUp.config(bg="black")
        tempFrame = Frame(nfPopUp,bg="black")
        tempFrame.grid(columnspan=5,rowspan=5)
        Label(tempFrame, text="Enter File Name with extension: ", bg="black", fg="white", font = ("Sansita One",10,"bold")).grid(column=1,row=1,padx=30,pady=10)
        ent = Entry(tempFrame)
        ent.grid(column=1,row=2,padx=30,pady=10)
        Button(tempFrame, text="Create",bg="black",fg="white",width=10,command=makeFile,font=("Sansita One",10,"bold")).grid(column=1,row=3,padx=30, pady=10)
        nfPopUp.mainloop()


    def interface(self):
        #CREATING BASE-FRAME
        self.baseFrame = Frame(self.root,width=600,height=300,bg="black")
        self.baseFrame.grid(columnspan=10,rowspan=10)

        #CREATING MANAGER OPTIONS
        self.label1 = Label(self.baseFrame, text="Path:\n" + actualPath, bg="black",justify=CENTER, fg="white",width=40, font = ("Sansita One",10,"bold"))
        self.label1.grid(column=0, row=0, padx=10, pady=10)
            #navigation buttons
        Button(self.baseFrame,text="Copy Path",bg="black",fg="white",width=10,command=self.copyClip,font=("Sansita One",10,"bold")).grid(column=1,row=0, padx=10, pady=10)
        Button(self.baseFrame,text="Parent Dir",bg="black",fg="white",width=10,command=self.backList,font=("Sansita One",10,"bold")).grid(column=2,row=0, padx=10, pady=10)
        Button(self.baseFrame,text="Enter Dir",bg="black",fg="white",width=10,command=self.enterList,font=("Sansita One",10,"bold")).grid(column=3,row=0, padx=10, pady=10)
            #show Content
        self.pathContent()
            #file Manipulation buttons
        self.secFrame = Frame(self.baseFrame,bg="black")
        self.secFrame.grid(column=1,row=1)
        Button(self.secFrame,text="Delete",bg="black",fg="white",width=10,command=self.deleteList,font=("Sansita One",10,"bold")).grid(column=0,row=0,padx=10, pady=10)
        Button(self.secFrame,text="Rename",bg="black",fg="white",width=10,command=self.renameFun,font=("Sansita One",10,"bold")).grid(column=0,row=1,padx=10, pady=10)
        Button(self.secFrame,text="New Folder",bg="black",fg="white",width=10,command=self.newFolder,font=("Sansita One",10,"bold")).grid(column=0,row=2,padx=10, pady=10)
        self.thrFrame = Frame(self.baseFrame,bg="black")
        self.thrFrame.grid(column=2,row=1)
        Button(self.thrFrame,text="New File",bg="black",fg="white",width=10,command=self.newFile,font=("Sansita One",10,"bold")).grid(column=0,row=0,padx=10, pady=10)
        
        
        #CREATING DEVELOPER OPTIONS
        Button(self.baseFrame,text="EXIT",command=exit,bg="black",fg="white",width=10).grid(column=3,row=10,padx=10, pady=10)
        #Button(self.baseFrame,text="COMMUNITY\nCHAT",command=createChat,bg="black",fg="white",width=10).grid(column=1,row=9,padx=10, pady=10)
        self.updateButton = Button(self.baseFrame,text="UPDATE",command=essentialSkript.updateSkript,bg="black",fg="white",width=10).grid(column=2,row=10,padx=10, pady=10)
        #self.restartButton = Button(self.baseFrame,text="RESTART",command=essentialSkript.restart,bg="black",fg="white",width=10).grid(column=0,row=10,padx=10, pady=10) #Developer Button Only (Remove when released)

root = creatingRoot("File-Manager "+codeVersion)
root.interface()
root.root.mainloop()
