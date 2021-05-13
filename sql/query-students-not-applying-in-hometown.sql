SELECT
	c.id, last_name, first_name, birth_year, birth_city_id
FROM
	codecoolers AS c
WHERE
	NOT EXISTS
	(
		SELECT
			cc.id
		FROM
			codecoolers AS cc
			INNER JOIN
			codecoolers_schools AS cs
			ON (cc.id = cs.codecooler_id)
			INNER JOIN
			schools AS s
			ON (s.id = cs.school_id)
		WHERE
			cc.birth_city_id = s.city_id
			AND
			c.id = cc.id
	);