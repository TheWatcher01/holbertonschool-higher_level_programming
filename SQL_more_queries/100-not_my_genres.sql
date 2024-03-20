-- Select 'name' column from 'tv_genres' table
SELECT tv_genres.name
    -- From 'tv_genres' table
FROM tv_genres
    -- Where 'id' in 'tv_genres' table is not in the following subquery
WHERE
    tv_genres.id NOT IN(
        -- This subquery selects 'genre_id' from 'tv_show_genres' table
        SELECT tv_show_genres.genre_id
            -- From 'tv_show_genres' table
        FROM tv_shows
            /* Inner join 'tv_shows' table on 'show_id' in 'tv_show_genres' table &
            'id' in 'tv_shows' table */
            JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
            -- Where 'title' in 'tv_shows' table is 'Dexter'
        WHERE
            tv_shows.title = 'Dexter'
    )
    -- Order results by 'name' in 'tv_genres' table in ascending order
ORDER BY tv_genres.name ASC;