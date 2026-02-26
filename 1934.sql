# Write your MySQL query statement below
select Signups.user_id, 
    ROUND(IFNULL(SUM(
    CASE 
        WHEN Confirmations.action='timeout' THEN 0
        WHEN Confirmations.action='confirmed' then 1
    END )/ COUNT(Confirmations.user_id),0),2) AS confirmation_rate 
#(COUNT(Confirmations.user_id)/SUM(Confirmations.action))
FROM Signups LEFT JOIN Confirmations ON Signups.user_id=Confirmations.user_id GROUP BY Signups.user_id;