# Write your MySQL query statement below
SELECT uni.unique_id AS unique_id, e.name AS name
FROM Employees e
LEFT JOIN EmployeeUNI uni
ON e.id = uni.id