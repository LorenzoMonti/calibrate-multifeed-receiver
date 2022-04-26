from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

setup(
	name='calibrate-receiver',
	version='0.8.0',
	description='A graphic tool used to calibrate a multifeed receiver',
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/LorenzoMonti/calibrate-multifeed-receiver",
	author='Lorenzo Monti',
	author_email='lorenzo.monti@inaf.it',
	packages=['config', 'src', 'src/tabs', 'theme'],
	include_package_data=True,
	entry_points={
        'console_scripts': [
            'calibrate_receiver=src.gui:vp_start_gui',
        ]
    },
	license='MIT',
	platforms='all',
	install_requires=[
		'pyvisa',
		'pyvisa-py',
		'pyserial',
		'pyusb',
		'gpib-ctypes',
		'tk',
		'numpy',
		'pandas',
		'seaborn',
		'beepy',
		'importlib-resources',
		'wget',
	],
	classifiers=[
        'Programming Language :: Python :: 3.8',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
    ]
)