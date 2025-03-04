-- Script qui liste les noms et scores des élèves de la table second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
