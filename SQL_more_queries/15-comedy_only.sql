-- This SQL script lists all shows of the genre "Comedy"

-- Select the 'title' column from the 'tv_shows' table
SELECT tv_shows.title
FROM
    -- From the 'tv_shows' table
    tv_shows
    /* Inner join 'tv_show_genres' table on 'id' in 'tv_shows' table & 'show_id'
    in 'tv_show_genres' table */
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Inner join 'tv_genres' table on 'genre_id' in 'tv_show_genres' table & 'id' in 'tv_genres' table
    INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE
    -- Filter the results where the 'name' in the 'tv_genres' table is 'Comedy'
    tv_genres.name = "Comedy"
    -- Order the results by the 'title' in the 'tv_shows' table in ascending order
ORDER BY tv_shows.title ASC;