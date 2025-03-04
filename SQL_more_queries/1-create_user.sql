-- Create l'utilisateur user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- lui ajouter tous les privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- verifier que les privileges sont bien pris en compte
FLUSH PRIVILEGES;
