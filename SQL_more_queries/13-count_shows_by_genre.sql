-- Select 'name' column from 'tv_genres' table, & count 'show_id' column from 'tv_show_genres' table
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
    -- From 'tv_genres' table
FROM tv_genres
    -- Inner join 'tv_show_genres' table on 'id' in 'tv_genres' table & 'genre_id' in 'tv_show_genres' table
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Group results by 'name' in 'tv_genres' table
GROUP BY
    tv_genres.name
    -- Order results by count of 'show_id' in descending order
ORDER BY COUNT(tv_show_genres.show_id) DESC;