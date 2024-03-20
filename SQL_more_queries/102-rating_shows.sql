-- Lists all shows by their rating
SELECT tv_shows.title, -- Select the title from the 'tv_shows' table
    SUM(tv_show_ratings.rate) AS rating -- Calculate the sum of the 'rate' column in the 'tv_show_ratings' table and alias it as 'rating'
FROM
    tv_shows -- From the 'tv_shows' table
    -- Perform an INNER JOIN with the 'tv_show_ratings' table
    -- based on the matching 'id' in 'tv_shows' and 'show_id' in 'tv_show_ratings'
    JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY
    tv_shows.title -- Group the results by the title of the show
ORDER BY rating DESC;
-- Order the results by the sum of ratings in descending order