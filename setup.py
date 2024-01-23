#!/usr/bin/python3
import codecs
from setuptools import setup, find_packages

RELOADED_VERSION = "0.1"
RELOADED_DOWNLOAD = ('https://github.com/blackleakz/reloaded/tarball/' + RELOADED_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()

def read_requirements():
    with open('requirements.txt') as f:
        return f.readlines()


setup(
	name='reloaded',
	packages=[
		'reloaded',
		'reloaded.farben',
		'reloaded.modules',
		'reloaded.kern',
		'reloaded.kern.basis',
		'reloaded.kern.dienste'],
	package_data={
          'reloaded.kern': [
              'dienste/*'
          ],
      },

	version=RELOADED_VERSION,
	description='reloaded is a high level MITM framework',
	long_description=read_file('README.md'),
	long_description_content_type='text/markdown',
    # packages = find_packages(),
    entry_points ={
            'console_scripts': [
                'reloaded = reloaded.reloaded:start_reloaded'
            ]
        },

	license='MIT',
	author='BlackLeakz',
	author_email='blackleakz@luxuzleakz.de',
	url='https://github.com/blackleakz/reloaded',
	download_url=RELOADED_DOWNLOAD,
	keywords=['python3', 'nemesis', 'shell', 'MITM', 'wifi', 'arp spoof'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Natural Language :: English',
	],

	install_requires= read_requirements(),

)
