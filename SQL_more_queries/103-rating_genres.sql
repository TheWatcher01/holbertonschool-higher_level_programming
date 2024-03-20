-- Select the name of each genre and the sum of its ratings
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating_sum
FROM
    tv_genres
    -- Join with the tv_show_genres table where the genre IDs match
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Join with the tv_show_ratings table where the show IDs match
    INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
    -- Group the results by the name of the genre
GROUP BY
    tv_genres.name
    -- Order the results in descending order by the sum of the ratings
ORDER BY rating_sum DESC;