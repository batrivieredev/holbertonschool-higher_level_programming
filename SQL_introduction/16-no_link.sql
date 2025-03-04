-- List toutes les tables de la bdd
-- affiche le contenu de la table second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
