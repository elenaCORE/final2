#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importamos las bibliotecas
import time
import sys
import os
import subprocess

cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'listen_addresses='\\\"'10.1.4.31'\\\" ' '>> ./etc/postgresql/9.6/main/postgresql.conf\" "
subprocess.call(cmd, shell=True)



cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'host all all 10.1.4.0/24 trust '>> ./etc/postgresql/9.6/main/pg_hba.conf\" "
subprocess.call(cmd, shell=True)


//completar a partir de linea 4 la configuracion de la base de datos.
cmd = "sudo lxc-attach --clear-env -n bbdd -- bash -c \"echo 'CREATE USER crm with PASSWORD '\\\" 'xxxx' \\\" ';' | sudo -u postgres psql\" "
subprocess.call(cmd, shell=True)