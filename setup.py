# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnextgreek_chd/__init__.py
from erpnextgreek_chd import __version__ as version

setup(
	name='erpnextgreek_chd',
	version=version,
	description='Greek support for ERPnext',
	author='ChD Computers',
	author_email='chdcomputers@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
