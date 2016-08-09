import os
import urllib
from configure import *

def downloadApplication():
	fileName = "GitHub.application"
	url = "http://github-windows.s3.amazonaws.com/" + fileName
	if not os.path.isdir(path):
			os.mkdir(path)
	urllib.urlretrieve(url, path + fileName)

downloadApplication()