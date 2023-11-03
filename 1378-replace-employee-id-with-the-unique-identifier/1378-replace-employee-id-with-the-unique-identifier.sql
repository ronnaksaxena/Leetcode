# Write your MySQL query statement below
SELECT
    eui.unique_id, e.name
FROM
    Employees as e
LEFT JOIN
    EmployeeUNI as eui
ON
    e.id = eui.id