#!/usr/bin/python3
from check_MySQL import check_mysql
import MySQLdb
import sys


def filter_states():
    # Récupération des arguments passés au script
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)

    # Création d'un objet cursor
    cur = db.cursor()

    # Exécution de la requête SQL
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupération et affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture de la connexion
    cur.close()
    db.close()


if __name__ == "__main__":
    check_mysql()
    filter_states()
