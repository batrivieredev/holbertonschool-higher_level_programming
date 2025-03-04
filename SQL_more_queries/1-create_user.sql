-- Script qui creer un fichier de configuration pour le serveur de base de donnees MySQL et un utilisateur user_0d_1 avec tous les privileges 
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
