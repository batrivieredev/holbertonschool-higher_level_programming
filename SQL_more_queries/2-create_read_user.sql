-- Script qui crée la bdd hbtn_0d_2 et un utilisateur user_0d_2 avec les privilèges de lecture sur la bdd hbtn_0d_2 (si la bdd n'existe pas, elle doit être créée)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
