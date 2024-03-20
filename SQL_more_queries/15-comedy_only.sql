SELECT tv_shows.title
FROM
    tv_shows_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE
    tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;