-- Select the database
USE hbtn_0c_0;
-- Selects the 'city' and the average 'temperature' from 'temperatures' table for the months 'July' and 'August'
-- Groups the result by 'city' and orders it by the average temperature in descending order
-- Limits the result to the top 3 cities with the highest average temperature
SELECT city, AVG(value) AS avg_temp
FROM temperatures -- Replace 'temperatures' with the actual name of your table
WHERE month IN (7, 8) -- Adjust this condition based on the format of your 'month' column
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;