-- Select the 'title' column from the 'tv_shows' table, and the 'genre_id' column from the 'tv_show_genres' table
SELECT tv_shows.title, tv_show_genres.genre_id
-- From the 'tv_shows' table
FROM tv_shows
-- Left join the 'tv_show_genres' table on the 'id' in the 'tv_shows' table and the 'show_id' in the 'tv_show_genres' table
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results by the 'title' in the 'tv_shows' table and the 'genre_id' in the 'tv_show_genres' table in ascending order
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;