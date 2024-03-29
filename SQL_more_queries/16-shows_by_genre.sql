-- Select the title of the show and the name of the genre. 
-- If the genre is not available, display 'NULL'.
SELECT tv_shows.title, tv_genres.name
    -- From the table 'tv_shows'
FROM
    tv_shows
    -- Perform a LEFT JOIN with the 'show_genres' table
    -- based on the matching 'id' in 'tv_shows' and 'show_id' in 'show_genres'.
    -- This ensures that all shows are included, even if they don't have a genre.
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Perform another LEFT JOIN with the 'tv_genres' table
    -- based on the matching 'genre_id' in 'show_genres' and 'id' in 'tv_genres'.
    -- This connects the genre names to the shows.
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Order the results first by the title of the show in ascending order,
    -- and then by the genre name in ascending order.
ORDER BY tv_shows.title ASC, tv_genres.name ASC;