# Gestion des bases de données

## Créer une base de données
```sql
CREATE DATABASE nom_de_la_bdd;
```

## Créer une base de données uniquement si elle n’existe pas
```sql
CREATE DATABASE IF NOT EXISTS nom_de_la_bdd;
```

## Utiliser une base de données
```sql
USE nom_de_la_bdd;
```

## Lister les bases de données
```sql
SHOW DATABASES;
```

## Supprimer une base de données
```sql
DROP DATABASE nom_de_la_bdd;
```

## Voir la base de données en cours d'utilisation
```sql
SELECT DATABASE();
```

# Gestion des tables

## Créer une table
```sql
CREATE TABLE nom_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    age INT CHECK (age > 0),
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Créer une table uniquement si elle n’existe pas
```sql
CREATE TABLE IF NOT EXISTS nom_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100)
);
```

## Afficher la structure d’une table
```sql
DESC nom_table;
```

## Lister les tables d’une base de données
```sql
SHOW TABLES;
```

## Afficher les colonnes d'une table
```sql
SHOW COLUMNS FROM nom_table;
```

## Renommer une table
```sql
RENAME TABLE ancienne_table TO nouvelle_table;
```

## Ajouter une colonne
```sql
ALTER TABLE nom_table ADD COLUMN email VARCHAR(255);
```

## Modifier une colonne
```sql
ALTER TABLE nom_table MODIFY COLUMN age SMALLINT;
```

## Supprimer une colonne
```sql
ALTER TABLE nom_table DROP COLUMN email;
```

## Supprimer une table
```sql
DROP TABLE nom_table;
```

## Vider une table (supprimer toutes les données sans supprimer la table)
```sql
TRUNCATE TABLE nom_table;
```

# Gestion des index (Optimisation)

## Créer un index pour accélérer les recherches
```sql
CREATE INDEX idx_nom ON nom_table(nom);
```

## Créer un index unique
```sql
CREATE UNIQUE INDEX idx_unique_email ON nom_table(email);
```

## Supprimer un index
```sql
DROP INDEX idx_nom ON nom_table;
```

## Voir les index d'une table
```sql
SHOW INDEX FROM nom_table;
```

# Gestion des données

## Insérer des données
```sql
INSERT INTO nom_table (nom, age) VALUES ('Alice', 25);
```

## Insérer plusieurs lignes à la fois
```sql
INSERT INTO nom_table (nom, age) VALUES
('Bob', 30),
('Charlie', 22);
```

## Afficher toutes les données d’une table
```sql
SELECT * FROM nom_table;
```

## Filtrer les données
```sql
SELECT * FROM nom_table WHERE age > 20;
```

## Trier les résultats
```sql
SELECT * FROM nom_table ORDER BY age DESC;
```

## Limiter le nombre de résultats
```sql
SELECT * FROM nom_table LIMIT 5;
```

## Mettre à jour des données
```sql
UPDATE nom_table SET age = 26 WHERE nom = 'Alice';
```

## Supprimer des données
```sql
DELETE FROM nom_table WHERE nom = 'Alice';
```

## Supprimer toutes les données d'une table
```sql
DELETE FROM nom_table;
```

## Vider une table sans journalisation (plus rapide)
```sql
TRUNCATE TABLE nom_table;
```

# Gestion des jointures

## Jointure interne (INNER JOIN)
```sql
SELECT utilisateurs.nom, commandes.total
FROM utilisateurs
INNER JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

## Jointure gauche (LEFT JOIN)
```sql
SELECT utilisateurs.nom, commandes.total
FROM utilisateurs
LEFT JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

## Jointure droite (RIGHT JOIN)
```sql
SELECT utilisateurs.nom, commandes.total
FROM utilisateurs
RIGHT JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

## Jointure complète (FULL JOIN) (nécessite UNION en MySQL)
```sql
SELECT utilisateurs.nom, commandes.total
FROM utilisateurs
LEFT JOIN commandes ON utilisateurs.id = commandes.utilisateur_id
UNION
SELECT utilisateurs.nom, commandes.total
FROM utilisateurs
RIGHT JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

# Gestion des utilisateurs et permissions

## Créer un utilisateur
```sql
CREATE USER 'nom_utilisateur'@'localhost' IDENTIFIED BY 'mot_de_passe';
```

## Accorder tous les privilèges sur une base de données
```sql
GRANT ALL PRIVILEGES ON nom_de_la_bdd.* TO 'nom_utilisateur'@'localhost';
```

## Accorder des privilèges spécifiques
```sql
GRANT SELECT, INSERT, UPDATE ON nom_de_la_bdd.* TO 'nom_utilisateur'@'localhost';
```

## Révoquer des permissions
```sql
REVOKE INSERT, UPDATE ON nom_de_la_bdd.* FROM 'nom_utilisateur'@'localhost';
```

## Voir les permissions d’un utilisateur
```sql
SHOW GRANTS FOR 'nom_utilisateur'@'localhost';
```

## Supprimer un utilisateur
```sql
DROP USER 'nom_utilisateur'@'localhost';
```

# Sauvegarde et restauration

## Exporter une base de données (dump SQL)
```sh
mysqldump -u utilisateur -p nom_de_la_bdd > sauvegarde.sql
```

## Importer une base de données
```sh
mysql -u utilisateur -p nom_de_la_bdd < sauvegarde.sql
```

## Vérifier l'intégrité d'une base de données
```sql
CHECK TABLE nom_table;
```

## Optimiser une table
```sql
OPTIMIZE TABLE nom_table;
```

# Transactions (Rollback & Commit)

## Démarrer une transaction
```sql
START TRANSACTION;
```

## Faire des modifications
```sql
UPDATE nom_table SET age = 30 WHERE nom = 'Alice';
```

## Valider les modifications (commit)
```sql
COMMIT;
```

## Annuler les modifications (rollback)
```sql
ROLLBACK;
```

