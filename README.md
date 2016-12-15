# DiaryVault

[![Build Status](https://travis-ci.org/lightsing/myVault.svg)](https://travis-ci.org/lightsing/myVault) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/lightsing/myVault/master/LICENSE)

A RSA-AES Based Diary Vault

## Requirements

Python 3.5
MacOS

## Install
In your terminal:
```
pip install git+https://github.com/lightsing/myVault
```

It mights be `pip3` on your system if you still use python2 as default.

## How to Set before Use 
###Step 1
Enter the following command line in your terminal:
```
$ myVault
```

or

```
$ python -m myVault
```
It mights be `python3` on your system if you still use python2 as default.

###Step 2
Choose the RSA bits length you like or just leave blank for 2048 as default.

###Step 3
Insert a USB driver to store the key just generated in step 2.

Then you have finished settings.

##How to Use
Follow the step 1 in the setting process.

Then you will see the menu like the following:
```
-----------My Vault v0.0.2------------


1. New File
2. Load File
3. New KeyPair
4. Exit
```

PS: Insert a USB driver if you choose 2 or 3. And it can only load the files created by itself. Use the **GNU Nano** as default editor.


####Hope you can encrypt whatever files you like.


