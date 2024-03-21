#!/usr/bin/python3
"""
File: check_MySQL.py
Author: TM_FULLNAME
Date: 2024-03-21
Description:
"""

import os
import sys
import subprocess


def check_mysql():
    try:
        # Vérifie si le service MySQL est en cours d'exécution
        subprocess.check_output('service mysql status', shell=True)
    except subprocess.CalledProcessError:
        # Si le service MySQL n'est pas en cours d'exécution, le démarrer
        print("MySQL n'est pas en cours d'exécution. Démarrage de MySQL...")
        subprocess.run('service mysql start', shell=True)
