-- Script qui liste les valeurs de la table first_table
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
