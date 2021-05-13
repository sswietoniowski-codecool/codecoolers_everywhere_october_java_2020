SELECT
	c.id, last_name, first_name, birth_year, birth_city_id
FROM
	codecoolers AS c
	INNER JOIN
	codecoolers_schools
	ON (c.id = codecooler_id)
	INNER JOIN
	schools AS s
	ON (s.id = school_id)
WHERE
	birth_city_id = city_id;