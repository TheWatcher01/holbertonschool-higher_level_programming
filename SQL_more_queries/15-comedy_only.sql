-- Select the 'title' column from the 'tv_shows' table
SELECT tv_shows.title
    -- From the 'tv_shows' table
FROM
    tv_shows
    -- Inner join the 'tv_show_genres' table on the 'id' in the 'tv_shows' table and the 'show_id' in the 'tv_show_genres' table
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Inner join the 'genres' table on the 'genre_id' in the 'tv_show_genres' table and the 'id' in the 'genres' table
    INNER JOIN genres ON tv_show_genres.genre_id = genres.id
    -- Where the 'name' in the 'genres' table is 'Comedy'
WHERE
    genres.name = 'Comedy'
    -- Order the results by the 'title' in the 'tv_shows' table in ascending order
ORDER BY tv_shows.title ASC;