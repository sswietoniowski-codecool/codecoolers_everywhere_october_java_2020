-- Please write the task's solution below

SELECT last_name, first_name, count(*) AS counter FROM public.codecoolers GROUP BY last_name, first_name ORDER BY counter DESC;