-- Script qui crée un utilisateur user_0d_2 avec tous les privileges sur la bdd
CREATE USER 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
