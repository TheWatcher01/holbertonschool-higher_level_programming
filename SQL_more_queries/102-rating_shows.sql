-- Select 'title' column from 'tv_shows' table & sum of 'rating' column from 'tv_show_ratings' table
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
    -- From 'tv_shows' table
FROM tv_shows
    /* Inner join 'tv_show_ratings' table on 'id' in 'tv_shows' table &
    'show_id' in 'tv_show_ratings' table */
    INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
    -- Group results by 'title' in 'tv_shows' table
GROUP BY
    tv_shows.title
    -- Order results by sum of 'rating' in descending order
ORDER BY rating_sum DESC;
