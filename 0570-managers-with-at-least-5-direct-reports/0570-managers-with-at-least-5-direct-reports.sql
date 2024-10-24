# Write your MySQL query statement below
SELECT 
    Employee.name
FROM
    Employee
WHERE
    Employee.id IN
        (SELECT
            Employee.managerId
        FROM
            Employee
        GROUP BY
            managerId
        HAVING COUNT(*) >= 5
        );





