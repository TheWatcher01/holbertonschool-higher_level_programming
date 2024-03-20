-- Select the name of the genre from the 'tv_genres' table
SELECT name
FROM tv_genres
WHERE
    -- Only select those genres whose name is not in the following subquery
    name NOT IN(
        -- This subquery selects the name of the genre from the 'tv_genres' table
        SELECT tv_genres.name
        FROM
            -- It joins 'tv_genres' with 'tv_show_genres' on the matching 'genre_id' in 'tv_show_genres' & 'id' in 'tv_genres'
            tv_genres
            JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
            -- It further joins the result with 'tv_shows' on the matching 'show_id' in 'tv_show_genres' & 'id' in 'tv_shows'
            JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
        WHERE
            -- Only select those genres linked to the show 'Dexter'
            tv_shows.title = 'Dexter'
    )
    -- Order the results by the genre name in ascending order
ORDER BY name ASC;