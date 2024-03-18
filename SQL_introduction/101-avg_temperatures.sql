-- Selects the DB to use
USE hbtn_0c_0;
-- Selects the 'city' and the average 'temperature' from 'temperatures_table', grouped by 'city' and ordered by the average temperature in descending order
SELECT city, AVG(value) AS avg_temp -- Replace with the actual name of the colonn of table
FROM temperatures -- Replace with the actual name of your table
GROUP BY city
ORDER BY avg_temp DESC;