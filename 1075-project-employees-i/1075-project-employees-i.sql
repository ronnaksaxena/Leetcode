# Write your MySQL query statement below
SELECT p.project_id as project_id, IFNULL(ROUND(AVG(e.experience_years), 2), 0) as average_years
FROM Project p
Left JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY project_id