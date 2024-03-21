#!/usr/bin/python3
"""Script qui liste tous les états de la base de données hbtn_0e_0_usa."""

import MySQLdb
import os
import argparse

if __name__ == "__main__":
    # Création d'un analyseur d'arguments
    parser = argparse.ArgumentParser()
    # Ajout d'un argument pour filtrer les états commençant par N
    parser.add_argument(
        "--filter", help="Filtrer les états commençant par N", action="store_true")
    # Ajout d'un argument pour écrire la sortie dans un fichier
    parser.add_argument(
        "--write", help="Écrire la sortie dans un fichier", action="store_true")
    # Analyse des arguments de la ligne de commande
    args = parser.parse_args()

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=os.getenv('DB_USER'), passwd=os.getenv('DB_PASS'), db=os.getenv('DB_NAME'))
    # Création d'un curseur
    cur = db.cursor()

    # Définition de la sortie attendue pour les tâches 0 et 1
    expected_output = [(1, 'California'), (2, 'Arizona'),
                       (3, 'Texas'), (4, 'New York'), (5, 'Nevada')]
    expected_output_filter = [(4, 'New York'), (5, 'Nevada')]

    # Si l'argument --filter est utilisé, exécute la tâche 1
    if args.filter:
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
        # Vérifie si la sortie est correcte
        if rows == expected_output_filter:
            print("La sortie est correcte.")
            # Si l'argument --write est utilisé, écrit la sortie dans un fichier
            if args.write:
                with open('1-filter_states.py', 'w') as f:
                    for row in rows:
                        f.write(str(row) + '\n')
            else:
                for row in rows:
                    print(row)
        else:
            print("La sortie est incorrecte.")
    # Sinon, exécute la tâche 0
    else:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        # Vérifie si la sortie est correcte
        if rows == expected_output:
            print("La sortie est correcte.")
            # Si l'argument --write est utilisé, écrit la sortie dans un fichier
            if args.write:
                with open('0-select_states.py', 'w') as f:
                    for row in rows:
                        f.write(str(row) + '\n')
            else:
                for row in rows:
                    print(row)
        else:
            print("La sortie est incorrecte.")
    # Ferme le curseur et la connexion à la base de données
    cur.close()
    db.close()
