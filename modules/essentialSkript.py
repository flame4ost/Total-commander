import os
import sys
from modules.fileSkript import makeFile
import requests as rq


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def updateSkript():
	versions = []
	updatedModules = 0
	try:
		for codeUpdate in ["File_Manager.py","manager.py","modules/essentialSkript.py","modules/fileSkript.py","restart.py"]:
			actualPath = os.getcwd()
			if codeUpdate == "manager.py" or codeUpdate == "restart.py" or codeUpdate == "File_Manager.py":
				codePathNF = actualPath+"/"+codeUpdate
				codePath = codePathNF.replace("/modules","")

			else:
				codePath = actualPath+"/"+codeUpdate

			codeDownload = rq.get("https://raw.githubusercontent.com/SerTor-TEAM/File-Manager/master/"+codeUpdate).text

			try:
				codeEdit = open(codePath,"r")
			except:
				makeFile(codePath)
				restart()

			if codeEdit.read() == codeDownload:
				versions.append(codeUpdate+" is last version!")
				codeEdit.close()
			else:
				codeEdit.close()
				codeEdit = open(codePath,"w")
				codeEdit.write(codeDownload)
				versions.append(codeUpdate+" updated!")
				codeEdit.close()
				updatedModules += 1


		print("\n		UPDATE INFORMATION")
		print("	----------------------------------------")
		for ok in versions:
			print("	  -"+ok)

		if updatedModules >= 1:
			print("	----------------------------------------\n\n")
			print("Restarting...")
			
			restart()

		print("	----------------------------------------\n\n")
		
	except Exception as Error:
		print("Something Were Wrong\nTry again Later!")
		print(Error,"\n\n")

def forceUpdate():
	codeUpdate = "modules/essentialSkript.py"
	actualPath = os.getcwd()

	codePath = actualPath+"/"+codeUpdate

	codeDownload = rq.get("https://raw.githubusercontent.com/SerTor-TEAM/File-Manager/master/"+codeUpdate).text

	try:
		codeEdit = open(codePath,"r")
	except:
		makeFile(codePath)
		restart()

	if codeEdit.read() == codeDownload:
		codeEdit.close()
	else:
		codeEdit.close()
		codeEdit = open(codePath,"w")
		codeEdit.write(codeDownload)
		codeEdit.close()

		print("Forced Update!")
		restart()
