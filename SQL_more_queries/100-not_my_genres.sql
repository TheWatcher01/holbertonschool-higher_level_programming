-- Select the name of the genre from the 'tv_genres' table
SELECT tv_genres.name
FROM tv_genres
    -- Only select those genres whose 'id' is not in the following subquery
WHERE
    tv_genres.id NOT IN(
        -- This subquery selects the 'genre_id' from the 'show_genres' table
        SELECT show_genres.genre_id
            -- It joins 'show_genres' with 'tv_shows' on the matching 'show_id' in 'show_genres' and 'id' in 'tv_shows'
        FROM show_genres
            INNER JOIN tv_shows ON show_genres.show_id = tv_shows.id
            -- Only select those genres linked to the show 'Dexter'
        WHERE
            tv_shows.title = 'Dexter'
    )
    -- Order the results by the genre name in ascending order
ORDER BY tv_genres.name ASC;