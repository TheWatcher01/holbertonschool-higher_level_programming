-- Select 'title' column from 'tv_shows' table
SELECT tv_shows.title
-- From 'tv_shows' table
FROM tv_shows
-- Where 'id' in 'tv_shows' table is not in the following subquery
WHERE
tv_shows.id NOT IN(
-- This subquery selects 'show_id' from 'tv_show_genres' table
SELECT tv_show_genres.show_id
-- From 'tv_show_genres' table
FROM tv_show_genres
-- Inner join 'tv_genres' table on 'genre_id' in 'tv_show_genres' table & 'id' in 'tv_genres' table
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Where 'name' in 'tv_genres' table is 'Comedy'
WHERE
tv_genres.name = 'Comedy'
)
-- Order results by 'title' in 'tv_shows' table in ascending order
ORDER BY tv_shows.title ASC;