-- Select the title of the show from the 'tv_shows' table
SELECT tv_shows.title
FROM tv_shows
-- Only select those shows whose 'id' is not in the following subquery
WHERE tv_shows.id NOT IN (
    -- This subquery selects the 'id' of shows from the 'tv_shows' table
    SELECT tv_shows.id
    -- It joins 'tv_shows' with 'show_genres' on the matching 'id' in 'tv_shows' and 'show_id' in 'show_genres'
    FROM tv_shows
    INNER JOIN show_genres ON tv_shows.id = show_genres.show_id
    -- It then joins the result with 'tv_genres' on the matching 'genre_id' in 'show_genres' and 'id' in 'tv_genres'
    INNER JOIN tv_genres ON show_genres.genre_id = tv_genres.id
    -- Only select those shows linked to the genre 'Comedy'
    WHERE tv_genres.name = 'Comedy'
)
-- Order the results by the show title in ascending order
ORDER BY tv_shows.title ASC;