-- Select the 'name' column from the 'genres' table, and count the 'show_id' column from the 'tv_show_genres' table
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
-- From the 'genres' table
FROM genres
-- Inner join the 'tv_show_genres' table on the 'id' in the 'genres' table and the 'genre_id' in the 'tv_show_genres' table
INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
-- Group the results by the 'name' in the 'genres' table
GROUP BY genres.name
-- Order the results by the count of 'show_id' in descending order
ORDER BY COUNT(tv_show_genres.show_id) DESC;