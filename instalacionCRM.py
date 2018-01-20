#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importamos las bibliotecas
import time
import sys
import os
import subprocess

# Como se trata de una orden critica lo dormimos dos segundos para que podamos cancelar el script.
for i in range (1,4): 
	os.system("sudo lxc-attach --clear-env -n s" + str(i) + " -- sudo apt-get update")
	os.system("sudo lxc-attach --clear-env -n s" + str(i) + " -- sudo apt-get install nodejs")
	os.system("sudo lxc-attach --clear-env -n s" + str(i) + " -- sudo apt-get install npm")
	
