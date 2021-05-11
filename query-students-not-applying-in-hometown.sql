-- Please write the task's solutions below

SELECT
    c.id, c.last_name, c.first_name, c.birth_year, c.birth_city_id
FROM
    public.codecoolers AS c
WHERE
    NOT EXISTS
    (
        SELECT
            cc.id
        FROM
            public.codecoolers AS cc
            INNER JOIN
            public.codecoolers_schools AS cs
            ON (cc.id = cs.codecooler_id)
            INNER JOIN
            public.schools AS s
            ON (s.id = cs.school_id)
        WHERE
            cc.birth_city_id = s.city_id
            AND
            c.id = cc.id
    );