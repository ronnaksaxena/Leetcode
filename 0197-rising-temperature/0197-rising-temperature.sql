# Write your MySQL query statement below
SELECT
    next.id as id
FROM
    Weather AS prev
RIGHT JOIN
    Weather AS next
ON 
    DATEDIFF(next.recordDate, prev.recordDate) = 1
WHERE
    next.temperature > prev.temperature