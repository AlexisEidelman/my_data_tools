# -*- coding: utf-8 -*-
"""

"""

from setuptools import setup, find_packages

import data_tools

setup(
    name = 'MyDataTools',
    version = '0.0.0.dev',
    url = 'https://github.com/AlexisEidelman/my_data_tools.git',
    license = 'http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    author='Alexis Eidelman',
    description='Répertoire pour déterminer les bâtiments insalubres.',
    #long_description=__doc__,
    #py_modules=['insalubrite'],
    packages=find_packages(), #['Apur', 'Sarah'],
    zip_safe=False,
    platforms='any',
    install_requires=['pandas'],
    include_package_data=True,
)
