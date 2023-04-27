SELECT Employee.id, Employee.name,
	   COUNT(Sales.price) AS sales_c,
	   RANK() OVER(ORDER BY COUNT(Sales.price) DESC) AS sales_rank_c,
	   SUM(Sales.price) AS sales_s,
	   RANK() OVER(ORDER BY SUM(Sales.price) DESC) AS sales_rank_s
FROM Employee LEFT JOIN Sales ON Employee.id = Sales.employee_id
GROUP BY Employee.id