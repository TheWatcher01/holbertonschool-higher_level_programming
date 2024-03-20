-- Select the title of the show and the sum of its ratings
SELECT CONCAT(
        tv_shows.title, ' - ', SUM(tv_show_ratings.rating)
    ) AS `title - rating_sum`
FROM tv_shows
    INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY
    tv_shows.title
ORDER BY SUM(tv_show_ratings.rating) DESC;