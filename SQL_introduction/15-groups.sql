-- Task 15
-- lists the number of records with the same score in the table second_table of the database
SELECT COUNT(score) AS number
FROM second_table
ORDER BY number DESC;