-- Please write the task's solution below

SELECT
    c.id, c.last_name, c.first_name, c.birth_year, c.birth_city_id
FROM
    public.codecoolers AS c
    INNER JOIN
    public.codecoolers_schools AS cs
    ON (c.id = cs.codecooler_id)
    INNER JOIN
    public.schools AS s
    ON (s.id = cs.school_id)
WHERE
    c.birth_city_id = s.city_id;
