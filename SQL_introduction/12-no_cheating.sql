-- A script that updates the score of Bob to 10 in the table second_table
-- Query to update the score of BOB to 10
SELECT score, name FROM second_table
WHERE name='Bob'
UPDATE score = 10;
