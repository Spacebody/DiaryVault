#!/usr/bin/env python3
from setuptools import setup

from myVault.config import version

setup(
    name='myVault',
    version=version,
    author='lightsing',
    url='https://github.com/lightsing/DiaryVault/',
    packages=['myVault', 'myVault.crypto'],
    entry_points="""
    [console_scripts]
    myVault = myVault.__main__:main
    """,
    install_requires=['pycrypto']
)


