import os,threading
from Tkinter import *
from Configure import *
from Command import *

class ConfigurationRadios:
	def __init__(self, parent):
		self.frame = Frame(parent)
		self.frame.pack(fill=BOTH)
		
		self.v = StringVar()
		self.v.set('Debug')

		Radiobutton(self.frame, text='Debug', variable=self.v,value='Debug').pack(side=LEFT, anchor=W)
		Radiobutton(self.frame, text='Release', variable=self.v,value='Release').pack(side=LEFT, anchor=W)

	def __str__(self):
		return self.v.get()

class PlatformRadios:
	def __init__(self, parent):
		self.frame = Frame(parent)
		self.frame.pack(fill=BOTH)
		
		self.v = StringVar()
		self.v.set('Win32')

		Radiobutton(self.frame, text='Win32', variable=self.v,value='Win32').pack(side=LEFT, anchor=W)
		Radiobutton(self.frame, text='x64', variable=self.v,value='x64').pack(side=LEFT, anchor=W)

	def __str__(self):
		return self.v.get()


class MainWindow():
	def __init__(self):
		root = Tk()
		self.configurationRadios = ConfigurationRadios(root)
		self.platformRadios = PlatformRadios(root)

		self.frame = Frame(root)
		self.frame.pack(fill=BOTH)

		self.v = IntVar()
		self.v.set(0)

		for i in range(len(pathMap)):
			Radiobutton(self.frame, text=pathMap[i]['setting']['name'], variable=self.v, value=i).pack(side=LEFT, anchor=W)

		Button(root,text='Open',command=self.openCommand).pack(side=LEFT, anchor=W)
		Button(root,text='Build',command=self.BuildCommand).pack(side=LEFT, anchor=W)
		Button(root,text='ReBuild',command=self.ReBuildCommand).pack(side=LEFT, anchor=W)
		Button(root,text='Clean',command=self.CleanCommand).pack(side=LEFT, anchor=W)
		Button(root,text='Update',command=self.UpdateCommand).pack(side=LEFT, anchor=W)

		root.mainloop()

	def openCommand(self):
		bat('Open', self.v.get(), str(self.configurationRadios), str(self.platformRadios))

	def BuildCommand(self):
		bat('Build', self.v.get(), str(self.configurationRadios), str(self.platformRadios))

	def ReBuildCommand(self):
		bat('ReBuild', self.v.get(), str(self.configurationRadios), str(self.platformRadios))

	def CleanCommand(self):
		bat('Clean', self.v.get(), str(self.configurationRadios), str(self.platformRadios))
	
	def UpdateCommand(self):
		bat('Update', self.v.get(), str(self.configurationRadios), str(self.platformRadios))

if __name__ == '__main__':
	window = MainWindow()