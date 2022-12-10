#!/bin/python
"""
path to icons folder in xxxhdpi:
/res/mipmap-xxxhdpi-v4/

icons name:
ic_launcher_round.png
ic_launcher.png

path in folder:
icons/res/mipmap-xxxhdpi-v4/ic_launcher.png
icons/res/mipmap-xxxhdpi-v4/ic_launcher_round.png

How to use zipfile
https://docs.python.org/3/library/zipfile.html
"""

import zipfile
import shutil
import sys

#print(len(sys.argv[0]))

try:
	apk = str(sys.argv[1])
except:
	print("usage: python3 icon-tool.py file.apk")
	exit()





try:
	with zipfile.ZipFile(apk, mode="r") as archive:
		#archive.printdir()
		archive.extract("res/mipmap-xxxhdpi-v4/ic_launcher_round.png", path="icons/")
		archive.extract("res/mipmap-xxxhdpi-v4/ic_launcher.png", path="icons/")

		shutil.move("icons/res/mipmap-xxxhdpi-v4/ic_launcher.png", "ic_launcher.png")
		shutil.move("icons/res/mipmap-xxxhdpi-v4/ic_launcher_round.png", "ic_launcher_round.png")

		shutil.rmtree("icons/")

except zipfile.BadZipFile as error:
	print(error)

