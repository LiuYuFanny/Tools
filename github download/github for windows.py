import os
import urllib
from configure import *

urls = [
"/GitHub.exe.manifest",
"/7za.exe.deploy",
"/Akavache.dll.deploy",
"/Akavache.Sqlite3.dll.deploy",
"/Caliburn.Micro.dll.deploy",
"/CefSharp.BrowserSubprocess.Core.dll.deploy",
"/CefSharp.BrowserSubprocess.exe.deploy",
"/CefSharp.Core.dll.deploy",
"/CefSharp.dll.deploy",
"/CefSharp.Wpf.dll.deploy",
"/d3dcompiler_47.dll.deploy",
"/GitHub.Core.dll.deploy",
"/GitHub.exe.config.deploy",
"/GitHub.exe.deploy",
"/GitHub.PortableGit.dll.deploy",
"/GitHub.UI.dll.deploy",
"/gitignore.7z.deploy",
"/Gitpad.exe.deploy",
"/ICSharpCode.AvalonEdit.dll.deploy",
"/ICSharpCode.NRefactory.dll.deploy",
"/icudtl.dat.deploy",
"/lfs-amd64.7z.deploy",
"/lfs-x86.7z.deploy",
"/libcef.dll.deploy",
"/libEGL.dll.deploy",
"/LibGit2Sharp.dll.deploy",
"/libGLESv2.dll.deploy",
"/Microsoft.Expression.Effects.dll.deploy",
"/Microsoft.Expression.Interactions.dll.deploy",
"/Microsoft.WindowsAPICodePack.dll.deploy",
"/Microsoft.WindowsAPICodePack.Shell.dll.deploy",
"/Newtonsoft.Json.dll.deploy",
"/NLog.dll.deploy",
"/Octokit.dll.deploy",
"/Octokit.Reactive.dll.deploy",
"/PortableGit.7z.deploy",
"/posh-git.7z.deploy",
"/ReactiveUI.Events.dll.deploy",
"/ReactiveUI.Routing_Net45.dll.deploy",
"/ReactiveUI.Xaml_Net45.dll.deploy",
"/ReactiveUI_Net45.dll.deploy",
"/Splat.dll.deploy",
"/SQLitePCL.raw.dll.deploy",
"/System.Interactive.dll.deploy",
"/System.Reactive.Core.dll.deploy",
"/System.Reactive.Interfaces.dll.deploy",
"/System.Reactive.Linq.dll.deploy",
"/System.Reactive.PlatformServices.dll.deploy",
"/System.Reactive.Windows.Threading.dll.deploy",
"/System.Windows.Interactivity.dll.deploy",
"/tutorial.7z.deploy",
"/de/Microsoft.Expression.Interactions.resources.dll.deploy",
"/en/Microsoft.Expression.Interactions.resources.dll.deploy",
"/es/Microsoft.Expression.Effects.resources.dll.deploy",
"/es/Microsoft.Expression.Interactions.resources.dll.deploy",
"/fr/Microsoft.Expression.Effects.resources.dll.deploy",
"/fr/Microsoft.Expression.Interactions.resources.dll.deploy",
"/Images/App.ico.deploy",
"/it/Microsoft.Expression.Effects.resources.dll.deploy",
"/it/Microsoft.Expression.Interactions.resources.dll.deploy",
"/ja/Microsoft.Expression.Effects.resources.dll.deploy",
"/ja/Microsoft.Expression.Interactions.resources.dll.deploy",
"/ko/Microsoft.Expression.Effects.resources.dll.deploy",
"/ko/Microsoft.Expression.Interactions.resources.dll.deploy",
"/ru/Microsoft.Expression.Effects.resources.dll.deploy",
"/ru/Microsoft.Expression.Interactions.resources.dll.deploy",
"/zh-Hans/Microsoft.Expression.Effects.resources.dll.deploy",
"/zh-Hans/Microsoft.Expression.Effects.resources.dll_2.deploy",
"/zh-Hans/Microsoft.Expression.Interactions.resources.dll.deploy",
"/zh-Hans/Microsoft.Expression.Interactions.resources.dll_2.deploy",
"/zh-Hant/Microsoft.Expression.Effects.resources.dll.deploy",
"/zh-Hant/Microsoft.Expression.Interactions.resources.dll.deploy",
]

def download(url):
	urlList = url.split('/')
	if urlList[-2].find('GitHub') == -1:
		if not os.path.isdir(path + urlList[-2]):
			os.mkdir(path + urlList[-2])
		fileName  = path + urlList[-2] + "\\" + urlList[-1]
	else:
		fileName = path + urlList[-1]
	print "download " + fileName
	urllib.urlretrieve(url, fileName)

def rename():
	walkList = os.walk(path)
	for group in walkList:
		filePath = group[0]
		files = group[-1]
		for file in files:
			if file.find('.deploy'):
				fileName = file.replace('.deploy', '')
				os.rename(filePath + "\\" + file, filePath + "\\" + fileName)

for i in urls:
	download(preUrl + i)

rename()