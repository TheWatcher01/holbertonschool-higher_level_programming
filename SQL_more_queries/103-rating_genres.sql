-- Selects the name of each genre and the sum of its ratings
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM
    tv_genres
    -- Joins with the 'tv_show_genres' table where the genre ids match
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Joins with the 'tv_show_ratings' table where the show ids match
    JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
    -- Groups the results by the genre name
GROUP BY
    tv_genres.name
    -- Orders the results in descending order by the sum of ratings
ORDER BY rating DESC;