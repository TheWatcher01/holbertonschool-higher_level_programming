-- Select the title of the show and the sum of its ratings
SELECT CONCAT(
        tv_shows.title, ' - ', SUM(tv_show_ratings.rating)
    ) AS `title - rating_sum` -- Concatenate the title and the sum of ratings
FROM
    tv_shows -- From the 'tv_shows' table
    -- Perform an INNER JOIN with the 'tv_show_ratings' table
    -- based on the matching 'id' in 'tv_shows' and 'show_id' in 'tv_show_ratings'
    INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY
    tv_shows.title -- Group the results by the title of the show
ORDER BY SUM(tv_show_ratings.rating) DESC;
-- Order the results by the sum of ratings in descending order