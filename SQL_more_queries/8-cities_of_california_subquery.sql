-- Select the 'id' and 'name' columns from the 'cities' table
SELECT id, name FROM cities
-- Filter the results where the 'state_id' matches the 'id' of the state named 'California'
WHERE state_id = (
  -- Subquery to get the 'id' of the state named 'California'
  SELECT id FROM states WHERE name = 'California'
)
-- Order the results by the 'id' in ascending order
ORDER BY id ASC;