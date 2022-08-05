-- A script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Query to compute the average score of all records in the table
UPDATE second_table
ADD average
SET average = AVG(score);
