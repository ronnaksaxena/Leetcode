# Write your MySQL query statement below
SELECT class
FROM COURSES
GROUP BY class
HAVING COUNT(class) >= 5