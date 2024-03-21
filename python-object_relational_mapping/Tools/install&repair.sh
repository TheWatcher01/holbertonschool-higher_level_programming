#!/bin/bash

# Demander le mot de passe sudo à l'utilisateur
echo "Veuillez entrer votre mot de passe sudo : "
read -s sudo_password

# Variable pour suivre si une erreur s'est produite
error_occurred=false

# Fonction pour vérifier si la commande a réussi
check_command() {
    if [ $? -eq 0 ]; then
        echo "Commande réussie : $1"
    else
        echo "Erreur lors de l'exécution de la commande : $1"
        error_occurred=true
        handle_error "$1"
    fi
}

# Fonction pour gérer les erreurs
handle_error() {
    case $1 in
        "Installation de mysql-server")
            echo "MySQL n'a pas pu démarrer. Tentative de résolution..."
            fix_mysql_installation
            ;;
        *)
            echo "Une erreur inconnue s'est produite."
            fix_installation
            ;;
    esac
}

# Fonction pour corriger l'installation de MySQL
fix_mysql_installation() {
    echo "Reinstalling MySQL..."
    echo $sudo_password | sudo -S systemctl stop mysql
    echo $sudo_password | sudo -S apt-get purge mysql-server mysql-client mysql-common
    echo $sudo_password | sudo -S apt-get autoremove
    echo $sudo_password | sudo -S apt-get autoclean
    if [ ! -f /var/lib/mysql/ibdata1 ]; then
        echo "Le fichier ibdata1 est manquant. Tentative de restauration..."
        # Supposons que votre fichier de sauvegarde soit /mnt/c/backups/ibdata1
        backup_file="/mnt/c/backups/ibdata1"
        if [ -f $backup_file ]; then
            echo $sudo_password | sudo -S cp $backup_file /var/lib/mysql/ibdata1
            echo "Le fichier ibdata1 a été restauré à partir de la sauvegarde."
        else
            echo "Erreur : Le fichier de sauvegarde $backup_file n'existe pas."
        fi
    fi
    echo $sudo_password | sudo -S dpkg --configure mysql-server-8.0
    echo $sudo_password | sudo -S apt install mysql-server-8.0
    check_command "Reinstallation de mysql-server"
}

# Fonction pour corriger l'installation
fix_installation() {
    echo "Nettoyage des paquets problématiques et réinstallation..."
    echo $sudo_password | sudo -S apt-get autoremove
    echo $sudo_password | sudo -S apt-get autoclean
    echo $sudo_password | sudo -S apt update && sudo apt upgrade
    check_command "Mise à jour des paquets"
    if ! command -v pip3 &> /dev/null
    then
        echo $sudo_password | sudo -S apt install python3-pip
        check_command "Installation de python3-pip"
    fi
    echo $sudo_password | sudo -S apt install pkg-config
    check_command "Installation de pkg-config"
    echo $sudo_password | sudo -S apt install mysql-server-8.0
    check_command "Installation de mysql-server"
    echo $sudo_password | sudo -S apt-get install python3-dev libmysqlclient-dev zlib1g-dev
    check_command "Installation des dépendances pour mysqlclient"
    echo $sudo_password | sudo -S pip3 install mysqlclient SQLAlchemy
    check_command "Installation de mysqlclient et SQLAlchemy"
}

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo $sudo_password | sudo -S apt install python3-pip
    check_command "Installation de python3-pip"
fi

# Installer pkg-config
echo $sudo_password | sudo -S apt install pkg-config
check_command "Installation de pkg-config"

# Installer mysql-server
echo $sudo_password | sudo -S apt install mysql-server-8.0
check_command "Installation de mysql-server"

# Installer les dépendances pour mysqlclient
echo $sudo_password | sudo -S apt-get install python3-dev libmysqlclient-dev zlib1g-dev
check_command "Installation des dépendances pour mysqlclient"

# Installer mysqlclient et SQLAlchemy avec pip
echo $sudo_password | sudo -S pip3 install mysqlclient SQLAlchemy
check_command "Installation de mysqlclient et SQLAlchemy"

# Si aucune erreur ne s'est produite, aucune réparation n'est nécessaire
if [ "$error_occurred" = false ] ; then
    echo "Toutes les installations ont réussi, aucune réparation n'est nécessaire."
fi