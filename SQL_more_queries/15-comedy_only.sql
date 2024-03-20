SELECT tv_shows.title
FROM
    tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE
    genres.name = "Comedy"
ORDER BY tv_shows.title ASC;