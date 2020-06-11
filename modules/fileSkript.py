import os
import shutil
from tkinter import *


#Function to rename a file or directory
def rename(oldName,newName):
    os.rename(oldName, newName)

#Check if item is file or dir...
def checkItem(path):
    if(os.path.isFile(path)):
        return "file"
    elif(os.path.isDir(path)):
        return "dir"
    else:
        return "inavlid"

#Delete
def delete(path):
    if(os.path.isfile(path)):
        deleteFile(path)
    else:
        deleteDir(path)

#Function to delete a file
def deleteFile(path):
    os.remove(path)

#Function to remove nonempty dir
def deleteDir(name):
    shutil.rmtree(name, ignore_errors=True) #Delete non empty dirs    

#Function to make new dir
def newDir(name):
    os.mkdir(name)

#Function to make new file
def makeFile(name): #name of file with extension
    file = open(name, "w")
    file.close()

#function to copy a file
def copyFile(sName, dPath):
    shutil.copy(sName, dPath)
    shutil.copystat(sName, dPath)

#function to cut a file
def cutFile(sName, dPath):
    shutil.copy(sName, dPath)
    shutil.copystat(sName, dPath)
    deleteFile(sName)

#Function that store all files and directories of current directory in a list
def content(path):
    files = os.listdir(path)
    return files #returns list
