-- Select the 'id' and 'name' columns from the 'cities' table, and the 'name' column from the 'states' table
SELECT cities.id, cities.name, states.name
-- From the 'cities' and 'states' tables
FROM cities, states
-- Where the 'state_id' in the 'cities' table matches the 'id' in the 'states' table
WHERE cities.state_id = states.id
-- Order the results by the 'id' in the 'cities' table in ascending order
ORDER BY cities.id ASC;