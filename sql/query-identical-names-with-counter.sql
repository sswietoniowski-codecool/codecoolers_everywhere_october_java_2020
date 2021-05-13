SELECT
	last_name, first_name, COUNT(*) AS counter
FROM
	codecoolers
GROUP BY
	last_name, first_name
ORDER BY
	counter DESC;

	
