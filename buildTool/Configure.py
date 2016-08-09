GGPTrunkDir = r'H:\GGP\trunk'
GGPViewerDir = r'H:\GGP\trunk\Tools\GGPViewer'
GGPProNDir = r'H:\GGP\ProdN'
GGPProMDir = r'H:\GGP\ProdM'

BIM5DDir = r'E:\BIM5D'
BIM5DDir_V25 = r'E:\BIM5D_V2.5'

GMBDir = r'E:\GMB_Version1'

GQIDir = r'H:\GQI'
GQIGGP = r'F:\GQI\Externals\GBIM'

GMPDir = r'F:\GMPT'
GMPGGP = r'F:\GMPT\Externals\GBIM'

TASDir = r'H:\TAS'

pathMap = [
	{
		'setting' :
		{
			'name' : 'GGPTrunk',
			'dir' : GGPTrunkDir,
			'sloution' : r'\Demos\ViewDemos\ViewDemos.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('QTDIR_x64' , r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_64_opengl'),
			('Path', r'%QTDIR%\bin;%QTDIR_x64%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'GGPViewer',
			'dir' : GGPViewerDir,
			'sloution' : r'\src\GGPViewer.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('QTDIR_x64' , r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_64_opengl'),
			('Path', r'%QTDIR%\bin;%QTDIR_x64%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'GGPProN',
			'dir' : GGPProNDir,
			'sloution' : r'\Demos\ViewDemos\ViewDemos.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('QTDIR_x64' , r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_64_opengl'),
			('Path', r'%QTDIR%\bin;%QTDIR_x64%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'GGPProM',
			'dir' : GGPProMDir,
			'sloution' : r'\Demos\ViewDemos\ViewDemos.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('QTDIR_x64' , r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_64_opengl'),
			('Path', r'%QTDIR%\bin;%QTDIR_x64%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'BIM5D',
			'dir' : BIM5DDir,
			'sloution' : r'\Desktop\BIM5D_Client.sln',
		},

		'path' : 
		[
			('GLDRS', r'E:\BIM5D\GLDRS'),
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\Qt5.1.1-vs2010-x64'),
			('GGPDIR', GGPProNDir),
			('Path', r'%QTDIR%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'BIM5D_V2.5',
			'dir' : BIM5DDir_V25,
			'sloution' : r'\BIM5D_Client.sln',
		},

		'path' : 
		[
			('GLDRS', r'E:\BIM5D\GLDRS'),
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\Qt5.1.1-vs2010-x64'),
			('GGPDIR', GGPProNDir),
			('Path', r'%QTDIR%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'GMB',
			'dir' : GMBDir,
			'sloution' : r'\source\GMJ+.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
            			('QTDIR_x64' , r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_64_opengl'),
			('Path', r'%QTDIR%\bin;%QTDIR_x64%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'GQI',
			'dir' : GQIDir,
			'sloution' : r'\GQI\src\GQIWithGMP.sln',
		},

		'path' : 
		[
			('GGPDIR', GGPProMDir),
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('Path', r'%QTDIR%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'GMPGGP',
			'dir' : GMPGGP,
			'sloution' : r'\Demos\ViewDemos\ViewDemos.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('QTDIR_x64' , r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_64_opengl'),
			('Path', r'%QTDIR%\bin;%QTDIR_x64%\bin;%Path%;'),
		],
	},


	{
		'setting' :
		{
			'name' : 'GMP',
			'dir' : GMPDir,
			'sloution' : r'\GMP\src\GMP.sln',
		},

		'path' : 
		[
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('Path', r'%QTDIR%\bin;%Path%;'),
		],
	},

	{
		'setting' :
		{
			'name' : 'TAS',
			'dir' : TASDir,
			'sloution' : r'\GCL\src\TAS.sln',
		},

		'path' : 
		[
			('GGPDIR', GGPProMDir),
			('QTDIR', r'E:\Qt\Qt5.1.1\5.1.1\msvc2010_opengl'),
			('Path', r'%QTDIR%\bin;%Path%;'),
		],
	},
]