/* Select 'title' column from 'tv_shows' table & 'name' column from 'tv_genres' table.
If genre is not available, display 'NULL'. */
SELECT tv_shows.title, tv_genres.name
    -- From 'tv_shows' table
FROM
    tv_shows
    /* Perform LEFT JOIN with 'tv_show_genres' table based on matching 'id' in 'tv_shows' table &
    'show_id' in 'tv_show_genres'. This ensures that all shows are included, even if they don't have a genre. */
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    /* Perform another LEFT JOIN with 'tv_genres' table based on matching 'genre_id' in 'tv_show_genres' table
    & 'id' in 'tv_genres'. This connects genre names to shows. */
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Order results first by title of show in ascending order, & then by genre name in ascending order.
ORDER BY tv_shows.title ASC, tv_genres.name ASC;