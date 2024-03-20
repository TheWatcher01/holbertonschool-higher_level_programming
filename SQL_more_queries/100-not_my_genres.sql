-- Select the name of the genre from the 'tv_genres' table
SELECT tv_genres.name
FROM tv_genres
    -- Where the genre name is not in the list of genre names linked to the show 'Dexter'
WHERE
    tv_genres.name NOT IN(
        -- Subquery to get the list of genre names linked to the show 'Dexter'
        SELECT tv_genres.name
        FROM
            tv_genres
            INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
            INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
        WHERE
            tv_shows.title = 'Dexter'
    )
    -- Order the results by the name of the genre in ascending order
ORDER BY tv_genres.name ASC;