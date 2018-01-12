#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importamos las bibliotecas
import time
import sys
import os

# Como se trata de una orden critica lo dormimos dos segundos para que podamos cancelar el script.
os.system("sudo lxc-attach -n nas1 -- gluster peer probe 10.1.4.22")
time.sleep(2)

os.system("sudo lxc-attach -n nas1 -- gluster peer probe 10.1.4.23")
time.sleep(2)

os.system("sudo lxc-attach -n nas1 -- gluster volume create nas replica 3 10.1.4.21:/nas 10.1.4.22:/nas 10.1.4.23:/nas force")
os.system("sudo lxc-attach -n nas1 -- gluster volume start nas")

time.sleep(7)


for i in range(1, 4):

    os.system("sudo lxc-attach -n s" + str(i) + " -- mkdir /mnt/nas")
    os.system("sudo lxc-attach -n s" + str(i) + " -- mount -t glusterfs 10.1.4." + str(i+20)+":/nas /mnt/nas")

print("Ejecutado con exito")


os.system("sudo lxc-attach --clear-env -n lb -- xr --verbose --server tcp:0:80 --backend 10.1.3.11:3030 --backendn10.1.3.12:3030 --backend 10.1.3.13:3030 --web-interface 0:8001 &")

## Instalación de base de datos

os.system("sudo lxc-attach")
