# Write your MySQL query statement below
SELECT
    Weather.id AS 'id'
FROM
    Weather
JOIN
    Weather AS w
ON 
    DATEDIFF(Weather.recordDate, w.recordDate) = 1
AND
    Weather.Temperature > w.Temperature

    