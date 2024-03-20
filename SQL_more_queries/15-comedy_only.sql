-- Select 'title' column from 'tv_shows' table
SELECT tv_shows.title
    -- From 'tv_shows' table
FROM
    tv_shows
    /* Inner join 'tv_show_genres' table on 'id' in 'tv_shows' table &
    'show_id' in 'tv_show_genres' table */
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Inner join 'genres' table on 'genre_id' in 'tv_show_genres' table & 'id' in 'genres' table
    INNER JOIN genres ON tv_show_genres.genre_id = genres.id
    -- Where 'name' in 'genres' table is 'Comedy'
WHERE
    genres.name = 'Comedy'
    -- Order results by 'title' in 'tv_shows' table in ascending order
ORDER BY tv_shows.title ASC;