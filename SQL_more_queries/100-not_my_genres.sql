-- Select the name of the genre from the 'tv_genres' table
SELECT tv_genres.name
FROM tv_genres
-- Only select those genres whose 'id' is not in the following subquery
WHERE tv_genres.id NOT IN (
    -- This subquery selects the 'id' of genres from the 'tv_genres' table
    SELECT tv_genres.id
    -- It joins 'tv_genres' with 'show_genres' on the matching 'id' in 'tv_genres' and 'genre_id' in 'show_genres'
    FROM tv_genres
    INNER JOIN show_genres ON tv_genres.id = show_genres.genre_id
    -- It then joins the result with 'tv_shows' on the matching 'show_id' in 'show_genres' and 'id' in 'tv_shows'
    INNER JOIN tv_shows ON show_genres.show_id = tv_shows.id
    -- Only select those genres linked to the show 'Dexter'
    WHERE tv_shows.title = 'Dexter'
)
-- Order the results by the genre name in ascending order
ORDER BY tv_genres.name ASC;