# Guide d'Installation MySQL + Plugin VS Code sur Linux

Ce guide fournit des instructions détaillées pour l'installation et la configuration de MySQL sur Linux. Il couvre également la modification de la méthode d'authentification pour l'utilisateur root de MySQL et l'installation du plugin MySQL pour Visual Studio Code sur un environnement WSL Ubuntu.

## Table des Matières

- [Guide d'Installation MySQL + Plugin VS Code sur Linux](#guide-dinstallation-mysql--plugin-vs-code-sur-linux)
  - [Table des Matières](#table-des-matières)
  - [Prérequis](#prérequis)
  - [Installation de MySQL](#installation-de-mysql)
  - [Configuration de MySQL](#configuration-de-mysql)
    - [Authentification par Mot de Passe](#authentification-par-mot-de-passe)
    - [Authentification par Socket](#authentification-par-socket)
    - [Changement de la Méthode d'Authentification pour l'Utilisateur Root](#changement-de-la-méthode-dauthentification-pour-lutilisateur-root)
  - [Configuration du Plugin MySQL pour Visual Studio Code](#configuration-du-plugin-mysql-pour-visual-studio-code)
    - [Authentification par Mot de Passe (Plugin MySQL)](#authentification-par-mot-de-passe-plugin-mysql)
    - [Authentification par Socket (Plugin MySQL)](#authentification-par-socket-plugin-mysql)
    - [Authentification par SSL (Plugin MySQL)](#authentification-par-ssl-plugin-mysql)
    - [Authentification par SSH (Plugin MySQL) sur WSL Ubuntu](#authentification-par-ssh-plugin-mysql-sur-wsl-ubuntu)
    - [Test de la Connexion](#test-de-la-connexion)
    - [Gestion des Erreurs](#gestion-des-erreurs)
    - [Utilisation du Plugin](#utilisation-du-plugin)
    - [Sécurité](#sécurité)
    - [Autres Fonctionnalités du Plugin](#autres-fonctionnalités-du-plugin)

## Prérequis

Avant de commencer l'installation de MySQL, il est nécessaire de mettre à jour la liste des paquets de votre système d'exploitation Linux. Pour cela, exécutez la commande suivante dans votre terminal :

```bash
sudo apt update
```

## Installation de MySQL

Pour installer le serveur MySQL, exécutez la commande suivante :

```bash
sudo apt install mysql-server
```

Une fois l'installation terminée, vous pouvez démarrer le serveur MySQL avec la commande suivante :

```bash
sudo systemctl start mysql
```

Pour configurer le démarrage automatique de MySQL, utilisez la commande suivante :

```bash
sudo systemctl enable mysql
```

## Configuration de MySQL

### Authentification par Mot de Passe

Pour configurer l'authentification par mot de passe, exécutez le script de sécurisation :

```bash
sudo mysql_secure_installation
```

Vous pouvez vérifier l'installation en vous connectant à MySQL avec l'utilisateur root :

```bash
mysql -u root -p
```

Saisissez le mot de passe de l'utilisateur root défini précédemment.

### Authentification par Socket

Pour vérifier que l'authentification par socket est configurée correctement, connectez-vous à MySQL et exécutez la requête suivante :

```sql
SELECT user,authentication_string,plugin,host FROM mysql.user WHERE user = 'root';
```

La colonne "plugin" doit indiquer "auth_socket".

### Changement de la Méthode d'Authentification pour l'Utilisateur Root

Pour changer la méthode d'authentification de l'utilisateur `root` :

- Pour `mysql_native_password` :

```sql


ALTER

 USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
```

- Pour `auth_socket` :

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
```

## Configuration du Plugin MySQL pour Visual Studio Code

Pour configurer le plugin MySQL dans VS Code, vous devez d'abord installer l'extension MySQL.
Dans VSCode extension/plugin rechercher "formulahendry.vscode-mysql"
Ensuite, vous pouvez configurer les connexions MySQL en ajoutant l'un des blocs suivants à votre fichier de configuration selon la configuration de votre serveur MySQL:

### Authentification par Mot de Passe (Plugin MySQL)

L'authentification par mot de passe est la méthode la plus courante pour se connecter à une base de données MySQL. Vous devez fournir le nom d'utilisateur et le mot de passe pour vous connecter.

```json
{
    "mysql.connections": [
        {
            "host": "localhost",
            "user": "your_username",
            "password": "your_password",
            "port": 3306,
            "database": "your_database"
        }
    ]
}
```

### Authentification par Socket (Plugin MySQL)

L'authentification par socket est une méthode d'authentification qui utilise le système de fichiers local pour l'authentification. C'est une méthode plus sécurisée car elle ne nécessite pas de mot de passe.

```json
{
    "mysql.connections": [
        {
            "host": "localhost",
            "user": "your_username",
            "socketPath": "/var/run/mysqld/mysqld.sock",
            "port": 3306,
            "database": "your_database"
        }
    ]
}
```

### Authentification par SSL (Plugin MySQL)

L'authentification par SSL est une méthode d'authentification qui utilise le protocole SSL pour sécuriser la connexion entre le client et le serveur. Vous devez fournir le chemin vers les fichiers de certificat SSL.

Pour configurer l'authentification SSL, suivez les étapes suivantes :

1. Générez les fichiers de certificat SSL. Vous pouvez utiliser OpenSSL pour cela. Voici une commande de base pour générer un certificat auto-signé :

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
```

1. Copiez les fichiers de certificat SSL dans un emplacement sûr sur votre système.

3. Dans votre fichier de configuration MySQL (généralement situé à `/etc/mysql/my.cnf`), ajoutez les lignes suivantes sous la section `[mysqld]` :

```bash
ssl-ca=/path/to/ca.pem
ssl-cert=/path/to/server-cert.pem
ssl-key=/path/to/server-key.pem
```

4. Redémarrez le serveur MySQL pour que les modifications prennent effet :

```bash
sudo systemctl restart mysql
```

5. Dans votre configuration de connexion MySQL pour le plugin MySQL dans Visual Studio Code, ajoutez les chemins vers vos fichiers de certificat SSL :

```json
{
    "mysql.connections": [
        {
            "host": "localhost",
           

 "

user": "your_username",
            "password": "your_password",
            "port": 3306,
            "database": "your_database",
            "ssl": {
                "ca": "/path/to/ca.pem",
                "key": "/path/to/client-key.pem",
                "cert": "/path/to/client-cert.pem"
            }
        }
    ]
}
```

6. Enregistrez vos modifications et redémarrez Visual Studio Code. Vous devriez maintenant être en mesure de vous connecter à votre base de données MySQL en utilisant l'authentification SSL.

### Authentification par SSH (Plugin MySQL) sur WSL Ubuntu

L'authentification par SSH est une méthode d'authentification qui utilise le protocole SSH pour sécuriser la connexion entre le client et le serveur. Vous devez fournir le chemin vers le fichier de clé privée SSH.

Pour configurer l'authentification SSH sur WSL Ubuntu, vous devez d'abord générer une paire de clés SSH sur votre système. Vous pouvez le faire en utilisant la commande `ssh-keygen`.

1. Générez une nouvelle paire de clés SSH en utilisant la commande suivante :

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Remplacez "your_email@example.com" par votre adresse e-mail.
L'adresse e-mail dans la commande ssh-keygen est utilisée comme un commentaire pour la clé. C'est une pratique courante pour identifier la clé, surtout si vous utilisez plusieurs clés SSH. Le commentaire, qui est généralement l'adresse e-mail de l'utilisateur, est ajouté à la fin de la clé publique. Cela n'affecte pas la fonctionnalité de la clé, c'est simplement pour vous aider à identifier la clé si vous en avez plusieurs.
Vous serez invité à entrer un mot de passe pour la clé.

2. Une fois que vous avez généré la paire de clés, vous devez ajouter la clé publique à votre serveur MySQL. Vous pouvez le faire en utilisant la commande `ssh-copy-id` :

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub your_username@your_server
```

Remplacez "your_username@your_server" par votre nom d'utilisateur et l'adresse de votre serveur MySQL.

3. Une fois que vous avez ajouté la clé publique à votre serveur, vous pouvez configurer l'authentification SSH dans le plugin MySQL pour Visual Studio Code. Remplacez "/path/to/private/key" par le chemin vers le fichier de clé privée que vous venez de générer (par défaut, il s'agit de `~/.ssh/id_rsa`).

```json
{
    "mysql.connections": [
        {
            "host": "localhost

",


            "user": "your_username",
            "password": "your_password",
            "port": 3306,
            "database": "your_database",
            "ssh": {
                "host": "ssh_host",
                "user": "ssh_user",
                "privateKey": "/path/to/private/key"
            }
        }
    ]
}
```

4. Enregistrez les modifications et redémarrez Visual Studio Code pour que les modifications prennent effet. Vous devriez maintenant être en mesure de vous connecter à votre base de données MySQL en utilisant l'authentification SSH.

Remplacez les valeurs par vos informations de connexion MySQL. Chaque méthode d'authentification a ses propres avantages et inconvénients. L'authentification par mot de passe est la plus simple à mettre en place, mais elle est moins sécurisée que les autres méthodes. L'authentification par socket est plus sécurisée, mais elle ne fonctionne que sur le système de fichiers local. L'authentification par SSL et SSH sont les plus sécurisées, mais elles nécessitent une configuration supplémentaire.

### Test de la Connexion

Après avoir configuré le plugin MySQL, vous pouvez tester la connexion à la base de données en exécutant une requête SQL de base. Par exemple :

```sql
SELECT DATABASE();
```

Si la connexion est correctement configurée, cette requête devrait retourner le nom de la base de données à laquelle vous êtes connecté.

### Gestion des Erreurs

Si vous rencontrez des erreurs lors de la configuration du plugin MySQL, voici quelques étapes de dépannage courantes :

- Vérifiez que vous avez correctement saisi les informations de connexion dans le fichier de configuration.
- Assurez-vous que le serveur MySQL est en cours d'exécution.
- Si vous recevez un message d'erreur indiquant que la connexion à la base de données a échoué, vérifiez que le serveur MySQL est accessible depuis votre machine et que les informations de connexion sont correctes.

### Utilisation du Plugin

Une fois que vous avez configuré le plugin MySQL, vous pouvez l'utiliser pour exécuter des requêtes SQL, visualiser les résultats, gérer plusieurs connexions, et plus encore. Pour exécuter une requête SQL, ouvrez une nouvelle fenêtre de requête SQL en cliquant sur le bouton "New Query" dans la vue MySQL, tapez votre requête, puis appuyez sur F5 pour l'exécuter.

### Sécurité

Lors de l'utilisation de MySQL, il est important de suivre les bonnes pratiques de sécurité. Utilisez toujours des mots de passe forts pour vos comptes d'utilisateur MySQL, limitez les privilèges de l'utilisateur de la base de données autant que possible, et assurez-vous de toujours garder votre serveur MySQL à jour avec les derniers correctifs de sécurité.

### Autres Fonctionnalités du Plugin

Le plugin MySQL pour Visual Studio Code offre également d'autres fonctionnalités utiles, comme le support de l'autocomplétion SQL, la coloration syntaxique, et le formatage du code SQL. Vous pouvez également explorer les bases de données et les tables, afficher les schémas de table, et plus encore directement depuis la vue MySQL.
