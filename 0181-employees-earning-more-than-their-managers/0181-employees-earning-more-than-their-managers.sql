# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee as e
LEFT JOIN Employee as m
ON e.managerId = m.id
WHERE e.salary > m.salary