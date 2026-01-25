# Write your MySQL query statement below
SELECT E.name AS "Employee" from Employee E INNER JOIN Employee M WHERE E.managerId=M.id AND E.salary > M.salary; 