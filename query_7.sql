SELECT s.fullname , g.name , sb.name, r.rate, r.date_of 
FROM rates r
JOIN students s ON r.student_id = s.id
JOIN [groups] g ON s.group_id = g.id 
JOIN subjects sb ON sb.id = r.subject_id
WHERE g.id = 2 AND sb.id = 3
ORDER BY r.rate DESC, r.date_of DESC;