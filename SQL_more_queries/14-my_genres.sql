-- Select 'name' column from 'tv_genres' table
SELECT tv_genres.name
    -- From 'tv_shows' table
FROM
    tv_shows
    /* Inner join 'tv_show_genres' table on 'id' in 'tv_shows' table and 'show_id'
    in 'tv_show_genres' table */
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Inner join 'tv_genres' table on 'genre_id' in 'tv_show_genres' table and 'id' in 'tv_genres' table
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Where 'title' in 'tv_shows' table is 'Dexter'
WHERE
    tv_shows.title = 'Dexter'
    -- Order results by 'name' in 'tv_genres' table in ascending order
ORDER BY tv_genres.name ASC;
