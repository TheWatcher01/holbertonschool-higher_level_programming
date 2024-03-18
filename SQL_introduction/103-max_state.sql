-- Selects the 'hbtn_0c_0' database to use for the following queries
USE hbtn_0c_0;

-- Selects the 'state' and the maximum 'value' (interpreted as temperature) from 'temperatures' table
-- Groups the result by 'state' and orders it by 'state'
-- The maximum temperature for each state is aliased as 'max_temp'
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;