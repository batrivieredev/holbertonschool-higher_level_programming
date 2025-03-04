-- Lists tout les genres de la table tv_genres et le nombre de séries associées à chaque genre 
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
