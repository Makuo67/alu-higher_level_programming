-- A script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- Query to list all records of the table
SELECT name, score FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
