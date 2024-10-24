SELECT r.contest_id, ROUND(COUNT(r.user_id) / (SELECT COUNT(user_id) FROM USERS) * 100, 2) as percentage
FROM
    Users as u
JOIN
    Register as r
ON
    r.user_id=u.user_id
GROUP BY
    r.contest_id
ORDER BY
    percentage DESC, contest_id ASC