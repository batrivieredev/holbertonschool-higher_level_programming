-- Script qui liste les noms et scores des élèves de la table second_table
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
