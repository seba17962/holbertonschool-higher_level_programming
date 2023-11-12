-- Task 14
-- computes the score average of all records in the table second_table of the database
SELECT SUM(score)/COUNT(score) as average
FROM second_table;
