-- This SQL script lists all genres of the show "Dexter"

-- Select the 'name' column from the 'tv_genres' table
SELECT tv_genres.name
FROM
    -- Join 'tv_genres' table with 'tv_show_genres' table on 'id' and 'genre_id' columns respectively
    tv_genres
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Further join the result with 'tv_shows' table on 'id' and 'show_id' columns respectively
    INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE
    -- Filter the results where the 'title' in the 'tv_shows' table is 'Dexter'
    tv_shows.title = "Dexter"
    -- Order the results by the 'name' column in the 'tv_genres' table in ascending order
ORDER BY tv_genres.name ASC;