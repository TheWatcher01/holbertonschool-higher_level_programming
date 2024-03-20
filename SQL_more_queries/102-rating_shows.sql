-- Select the title of each show and the sum of its ratings
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating_sum
FROM
    tv_shows -- From the tv_shows table
    -- Join with the tv_show_ratings table where the show IDs match
    INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
    -- Group the results by the title of the show
GROUP BY
    tv_shows.title
    -- Order the results in descending order by the sum of the ratings
ORDER BY rating_sum DESC;