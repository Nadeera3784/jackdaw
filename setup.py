from setuptools import setup, find_packages
import re
import platform

VERSIONFILE="jackdaw/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
	verstr = mo.group(1)
else:
	raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
	# Application name:
	name="jackdaw",

	# Version number (initial):
	version=verstr,

	# Application author details:
	author="Tamas Jos",
	author_email="info@skelsecprojects.com",

	# Packages
	packages=find_packages(),

	# Include additional files into the package
	include_package_data=True,
	
	# Details
	url="https://github.com/skelsec/jackdaw",

	zip_safe = False,
	#
	# license="LICENSE.txt",
	description="Gathering shiny things from your domain",

	# long_description=open("README.txt").read(),
	python_requires='>=3.6',
	classifiers=(
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Operating System :: OS Independent",
	),
	# manifest.in doesnt always work, but this one does
	data_files=[
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/bundle.js', 'jackdaw/nest/site/nui/dist/bundle.js']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/index.html', 'jackdaw/nest/site/nui/dist/index.html']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/vis-network.min.css', 'jackdaw/nest/site/nui/dist/vis-network.min.css']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/computer.png', 'jackdaw/nest/site/nui/dist/computer.png']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/group.png', 'jackdaw/nest/site/nui/dist/group.png']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/logo.png', 'jackdaw/nest/site/nui/dist/logo.png']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/organizational.png', 'jackdaw/nest/site/nui/dist/organizational.png']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/unknown.png', 'jackdaw/nest/site/nui/dist/unknown.png']),
		('jackdaw/nest/site/nui/dist', ['jackdaw/nest/site/nui/dist/user.png', 'jackdaw/nest/site/nui/dist/user.png']),		
	],
	install_requires=[
		'aiosmb>=0.3.4',
		'msldap>=0.3.37',
		'sqlalchemy>=1.4',
		'tqdm',
		'networkx',
		'itsdangerous<2.0,>=0.24',
		'werkzeug<2.0,>=1.0',
		'flask<2,>=1.0.4',
		'Jinja2<3.0,>=2.10.1',
		'connexion>=2.9.0',
		'flask-sqlalchemy>=2.5.1',
		'connexion[swagger-ui]',
		'websockets',
		'swagger-ui-bundle>=0.0.2',
		'colorama; platform_system=="Windows"',
		'winacl>=0.1.1',
		'python-igraph', #'python-igraph==0.8.3',
		'aiosqlite',
	],
	# 'aiohttp',
	#'p y p y k a t z>=0.4.8',
	entry_points={
		'console_scripts': [
			'jackdaw = jackdaw.__main__:main',
		],
	}
)
