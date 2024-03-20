-- Select title of show & name of genre. If genre is not available, display 'NULL'
SELECT tv_shows.title, tv_genres.name AS genre
    -- From table 'tv_shows'
FROM
    tv_shows
    /* Perform a LEFT JOIN with 'show_genres' table based on matching 'id' in 'tv_shows'
    & 'show_id' in 'show_genres'. This ensures that all shows are included,
    even if they don't have a genre. */
    LEFT JOIN show_genres ON tv_shows.id = show_genres.show_id
    /* Perform another LEFT JOIN with 'tv_genres' table based on matching 'genre_id'
    in 'show_genres' & 'id' in 'tv_genres' */
    This connects genre names to shows.LEFT JOIN tv_genres ON show_genres.genre_id = tv_genres.id
    -- Order results first by title of show in ascending order, & then by genre name in ascending order.
ORDER BY tv_shows.title ASC, genre ASC;