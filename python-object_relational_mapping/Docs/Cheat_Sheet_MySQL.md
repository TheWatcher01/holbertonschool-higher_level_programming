# Référence des Commandes MySQL

Ce document fournit une liste de référence pour les commandes MySQL les plus couramment utilisées. Chaque commande est accompagnée d'un exemple de syntaxe, où les valeurs spécifiques doivent remplacer les placeholders indiqués par `{}`.

## Table des Matières

- [Référence des Commandes MySQL](#référence-des-commandes-mysql)
  - [Table des Matières](#table-des-matières)
  - [Connexion à une Base de Données MySQL](#connexion-à-une-base-de-données-mysql)
  - [Gestion des Bases de Données](#gestion-des-bases-de-données)
  - [Gestion des Tables](#gestion-des-tables)
  - [Manipulation des Données](#manipulation-des-données)
  - [Requêtes Avancées](#requêtes-avancées)
  - [Gestion des Utilisateurs](#gestion-des-utilisateurs)
  - [Transactions](#transactions)
  - [Fonctions de Date et Heure](#fonctions-de-date-et-heure)
  - [Fonctions de Chaîne de Caractères](#fonctions-de-chaîne-de-caractères)
  - [Fonctions Mathématiques](#fonctions-mathématiques)
  - [Fonctions de Conversion](#fonctions-de-conversion)
  - [Gestion des Triggers](#gestion-des-triggers)
  - [Gestion des Procédures Stockées](#gestion-des-procédures-stockées)
  - [Fonctions d'agrégation](#fonctions-dagrégation)
  - [Gestion des Contraintes](#gestion-des-contraintes)
  - [Gestion des Séquences](#gestion-des-séquences)
  - [Gestion des Index](#gestion-des-index)
  - [Gestion des Vues](#gestion-des-vues)

## Connexion à une Base de Données MySQL

```bash
mysql -u {username} -p{password} -h {hostname} -P {port} -D {database}
```

## Gestion des Bases de Données

- Afficher toutes les bases de données :

```sql
SHOW DATABASES;
```

- Sélectionner une base de données :

```sql
USE {database};
```

- Créer une base de données :

```sql
CREATE DATABASE {database};
```

- Supprimer une base de données :

```sql
DROP DATABASE {database};
```

## Gestion des Tables

- Afficher toutes les tables d'une base de données :

```sql
SHOW TABLES;
```

- Afficher la structure d'une table :

```sql
DESCRIBE {table};
```

- Créer une table :

```sql
CREATE TABLE {table} ({column1} {type1}, {column2} {type2}, ...);
```

- Supprimer une table :

```sql
DROP TABLE {table};
```

## Manipulation des Données

- Sélectionner des données d'une table :

```sql
SELECT * FROM {table};
```

- Insérer des données dans une table :

```sql
INSERT INTO {table} ({column1}, {column2}, ...) VALUES ({value1}, {value2}, ...);
```

- Mettre à jour des données dans une table :

```sql
UPDATE {table} SET {column1} = {value1}, {column2} = {value2}, ... WHERE {condition};
```

- Supprimer des données d'une table :

```sql
DELETE FROM {table} WHERE {condition};
```

## Requêtes Avancées

- Sélectionner des données spécifiques d'une table :

```sql
SELECT {column1}, {column2}, ... FROM {table} WHERE {condition};
```

- Trier les résultats d'une requête :

```sql
SELECT * FROM {table} ORDER BY {column} ASC|DESC;
```

- Limiter le nombre de résultats retournés :

```sql
SELECT * FROM {table} LIMIT {number};
```

- Compter le nombre de lignes dans une table :

```sql
SELECT COUNT(*) FROM {table};
```

- Joindre deux tables :

```sql
SELECT * FROM {table1} JOIN {table2} ON {table1.column} = {table2.column};
```

- Sélectionner des données uniques d'une colonne :

```sql
SELECT DISTINCT {column} FROM {table};
```

- Compter le nombre de valeurs uniques dans une colonne :

```sql
SELECT COUNT(DISTINCT {column}) FROM {table};
```

- Grouper les résultats par colonne :

```sql
SELECT {column}, COUNT(*) FROM {table} GROUP BY {column};
```

- Utiliser une clause HAVING avec GROUP BY :

```sql
SELECT {column}, COUNT(*) FROM {table} GROUP BY {column} HAVING COUNT(*) > {number};
```

- Utiliser des fonctions d'agrégation comme SUM, AVG, MIN, MAX :

```sql
SELECT SUM({column}) FROM {table};
SELECT AVG({column}) FROM {table};
SELECT MIN({column}) FROM {table};
SELECT MAX({column}) FROM {table};
```

- Utiliser des sous-requêtes :

```sql
SELECT {column} FROM {table} WHERE {column} = (SELECT {column} FROM {table} WHERE {condition});
```

- Utiliser des requêtes UNION pour combiner les résultats de plusieurs SELECT :

```sql
SELECT {column} FROM {table1} UNION SELECT {column} FROM {table2};
```

## Gestion des Utilisateurs

- Créer un utilisateur :

```sql

CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';
```

- Donner des privilèges à un utilisateur :

```sql
GRANT ALL PRIVILEGES ON {database}.* TO '{username}'@'localhost';
```

- Recharger les privilèges :

```sql
FLUSH PRIVILEGES;
```

- Supprimer un utilisateur :

```sql
DROP USER '{username}'@'localhost';
```

- Modifier le mot de passe d'un utilisateur :

```sql
ALTER USER '{username}'@'localhost' IDENTIFIED BY '{new_password}';
```

## Transactions

Les transactions sont un moyen de regrouper plusieurs commandes SQL en une seule unité de travail. Si une commande échoue, toutes les autres commandes de la transaction sont annulées et la base de données reste inchangée.

- Commencer une transaction :

```sql
START TRANSACTION;
```

- Valider une transaction :

```sql
COMMIT;
```

- Annuler une transaction :

```sql
ROLLBACK;
```

## Fonctions de Date et Heure

MySQL fournit plusieurs fonctions pour travailler avec des dates et des heures.

- Obtenir la date et l'heure actuelles :

```sql
SELECT NOW();
```

- Extraire l'année d'une date :

```sql
SELECT YEAR(date_column) FROM table;
```

- Extraire le mois d'une date :

```sql
SELECT MONTH(date_column) FROM table;
```

- Extraire le jour d'une date :

```sql
SELECT DAY(date_column) FROM table;
```

## Fonctions de Chaîne de Caractères

MySQL fournit également plusieurs fonctions pour travailler avec des chaînes de caractères.

- Concaténer deux chaînes de caractères :

```sql
SELECT CONCAT(column1, column2) FROM table;
```

- Convertir une chaîne de caractères en majuscules :

```sql
SELECT UPPER(column) FROM table;
```

- Convertir une chaîne de caractères en minuscules :

```sql
SELECT LOWER(column) FROM table;
```

- Trouver la longueur d'une chaîne de caractères :

```sql
SELECT LENGTH(column) FROM table;
```

## Fonctions Mathématiques

MySQL fournit plusieurs fonctions mathématiques.

- Calculer la racine carrée d'un nombre :

```sql
SELECT SQRT(column) FROM table;
```

- Calculer le logarithme naturel d'un nombre :

```sql
SELECT LN(column) FROM table;
```

## Fonctions de Conversion

MySQL fournit des fonctions pour convertir des données d'un type à un autre.

- Convertir une chaîne de caractères en un nombre entier :

```sql
SELECT CAST(column AS INT) FROM table;
```

- Convertir une chaîne de caractères en un nombre à virgule flottante :

```sql
SELECT CAST(column AS FLOAT) FROM table;
```

## Gestion des Triggers

Les triggers sont des routines stockées qui sont exécutées automatiquement en réponse à certains événements sur une table spécifique.

- Créer un trigger :

```sql
CREATE TRIGGER trigger_name BEFORE|AFTER INSERT|UPDATE|DELETE ON table FOR EACH ROW trigger_body;
```

- Supprimer un trigger :

```sql
DROP TRIGGER trigger_name;
```

## Gestion des Procédures Stockées

Les procédures stockées sont des routines qui peuvent être enregistrées dans la base de données et réutilisées.

- Créer une procédure stockée :

```sql
CREATE PROCEDURE procedure_name() BEGIN procedure_body; END;
```

- Appeler une procédure stockée :

```sql
CALL procedure_name();
```

- Supprimer une procédure stockée :

```sql
DROP PROCEDURE procedure_name;
```

## Fonctions d'agrégation

- Trouver la valeur médiane :

```sql
SELECT column FROM table ORDER BY column LIMIT 1 OFFSET (SELECT COUNT(*) FROM table) / 2;
```

- Trouver la valeur la plus fréquente (mode) :

```sql
SELECT column, COUNT(column) AS frequency FROM table GROUP BY column ORDER BY frequency DESC LIMIT 1;
```

- Calculer la variance d'une colonne :

```sql
SELECT VARIANCE(column) FROM table
```

- Calculer la covariance de deux colonnes :

```sql
SELECT COVAR_POP(column1, column2) FROM table;
```

- Calculer la corrélation de deux colonnes :

```sql
SELECT CORR(column1, column2) FROM table;
```

- Calculer l'écart type d'une colonne :

```sql
SELECT STDDEV(column) FROM table;
```

## Gestion des Contraintes

- Ajouter une contrainte UNIQUE :

```sql
ALTER TABLE table ADD CONSTRAINT constraint_name UNIQUE (column);
```

- Ajouter une contrainte FOREIGN KEY :

```sql
ALTER TABLE table ADD CONSTRAINT constraint_name FOREIGN KEY (column) REFERENCES other_table(other_column);
```

- Ajouter une contrainte CHECK :

```sql
ALTER TABLE table ADD CONSTRAINT constraint_name CHECK (condition);
```

- Supprimer une contrainte :

```sql
ALTER TABLE table DROP CONSTRAINT constraint_name;
```

- Désactiver une contrainte :

```sql
ALTER TABLE table NOCHECK CONSTRAINT constraint_name;
```

- Activer une contrainte :

```sql
ALTER TABLE table CHECK CONSTRAINT constraint_name;
```

- Modifier une contrainte :

```sql
ALTER TABLE table MODIFY CONSTRAINT constraint_name CHECK (new_condition);
```

## Gestion des Séquences

- Créer une séquence :

```sql
CREATE SEQUENCE sequence_name;
```

- Obtenir la prochaine valeur d'une séquence :

```sql
SELECT NEXT VALUE FOR sequence_name;
```

- Supprimer une séquence :

```sql
DROP SEQUENCE sequence_name;
```

- Réinitialiser une séquence :

```sql
ALTER SEQUENCE sequence_name RESTART WITH 1;
```

- Obtenir la valeur actuelle d'une séquence :

```sql
SELECT LAST_VALUE FROM sequence_name;
```

- Modifier la valeur de départ d'une séquence :

```sql
ALTER SEQUENCE sequence_name START WITH value;
```

## Gestion des Index

- Créer un index sur une colonne :

```sql
CREATE INDEX {index_name} ON {table}({column});
```

- Afficher tous les index d'une table :

```sql
SHOW INDEX FROM {table};
```

- Afficher les statistiques d'un index :

```sql
SHOW INDEX FROM {table} WHERE Key_name = '{index_name}';
```

- Modifier un index :

```sql
ALTER TABLE {table} MODIFY INDEX {index_name}({column});
```

- Supprimer un index :

```sql
DROP INDEX {index_name} ON {table};
```

## Gestion des Vues

- Créer une vue :

```sql
CREATE VIEW {view_name} AS SELECT {column1}, {column2}, ... FROM {table} WHERE {condition};
```

- Afficher toutes les vues :

```sql
SHOW FULL TABLES IN {database} WHERE TABLE_TYPE LIKE 'VIEW';
```

- Afficher le code SQL d'une vue :

```sql
SHOW CREATE VIEW {view_name};
```

- Modifier une vue existante :

```sql
CREATE OR REPLACE VIEW {view_name} AS SELECT {column1}, {column2}, ... FROM {table} WHERE {condition};
```

- Supprimer une vue :

```sql
DROP VIEW {view_name};
```

Veuillez noter que `{username}`, `{password}`, `{hostname}`, `{port}`, `{database}`, `{table}`, `{column1}`, `{column2}`, `{value1}`, `{value2}`, `{condition}`, `{type1}`, `{type2}`, `{number}`, `{index_name}`, `{view_name}`, `{new_password}` doivent être remplacés par vos valeurs spécifiques lors de l'utilisation de ces commandes.
