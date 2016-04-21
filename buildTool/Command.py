import os,threading
from Configure import *

class batch_command:
	def __init__(self):
		self.commands = []

	def add_command(self, cmd):
		self.commands += [cmd]

	def execute(self):
		batch_file = "build.bat"
		batch_f = open(batch_file, "w")
		batch_f.writelines([cmd_line + "\n" for cmd_line in self.commands])
		batch_f.close()
		ret_code = os.system(batch_file)
		os.remove(batch_file)
		return ret_code

class bat:
	def __init__(self, operation, index, configuration, platform):
		build_cmd = batch_command()

		if operation == 'Update':
			build_cmd.add_command('@cd /d %s' % pathMap[index]['setting']['dir'])
			build_cmd.add_command('@svn update')
			build_cmd.execute()
			
		else:
			path = pathMap[index]['path']

			flag = False
			for (key, value) in path:
				if key == 'GGPDIR':
					flag = True
				if key == 'Path' and flag:
					value += '%%GGPDIR%%\\Bin\\%s\\%s;' % (platform, configuration)

				build_cmd.add_command('SET %s=%s' % (key, value))

			if operation == 'Open':
				build_cmd.add_command('@CALL "%%VS%dCOMNTOOLS%%..\\IDE\\devenv.exe" %s' % (140, pathMap[index]['setting']['dir'] + pathMap[index]['setting']['sloution']))
				threading.Thread(target=build_cmd.execute).start()

			else:
				#if platform == 'Win32':
					#build_cmd.add_command('@CALL "%%VS%dCOMNTOOLS%%..\\..\\VC\\vcvarsall.bat" %s' % (100, 'x86'))
				#else:
					#build_cmd.add_command('@CALL "%%VS%dCOMNTOOLS%%..\\..\\VC\\vcvarsall.bat" %s' % (100, 'x86_amd64'))
				
				#build_cmd.add_command('@SET VisualStudioVersion=10.0')
				#build_cmd.add_command('@MSBuild %s /nologo /m /v:m /t:%s /p:Configuration=%s,Platform=%s' % (pathMap[index]['setting']['dir'] + pathMap[index]['setting']['sloution'], operation, configuration, platform))

				build_cmd.add_command('@CALL "%%VS%dCOMNTOOLS%%..\\IDE\\devenv" %s /%s "%s|%s"' % (100, pathMap[index]['setting']['dir'] + pathMap[index]['setting']['sloution'], operation, configuration, platform))
				build_cmd.execute()