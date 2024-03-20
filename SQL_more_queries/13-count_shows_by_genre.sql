-- Select 'name' column from 'genres' table, & count 'show_id' column from 'tv_show_genres' table
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
    -- From 'genres' table
FROM genres
    -- Inner join 'tv_show_genres' table on 'id' in 'genres' table & 'genre_id' in 'tv_show_genres' table
    INNER JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
    -- Group results by 'name' in 'genres' table
GROUP BY
    genres.name
    -- Order results by count of 'show_id' in descending order
ORDER BY COUNT(tv_show_genres.show_id) DESC;