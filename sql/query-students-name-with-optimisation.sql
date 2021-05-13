-- Please write the task's solutions below

-- query

SELECT last_name, first_name FROM public.codecoolers WHERE last_name = 'Ware' AND first_name = 'Selena';

-- query plan

EXPLAIN ANALYZE SELECT last_name, first_name FROM public.codecoolers WHERE last_name = 'Ware' AND first_name = 'Selena';

/*

Gather  (cost=1000.00..7701.10 rows=1 width=13) (actual time=120.167..212.546 rows=1 loops=1)
  Workers Planned: 2
  Workers Launched: 2
  ->  Parallel Seq Scan on codecoolers  (cost=0.00..6701.00 rows=1 width=13) (actual time=39.560..44.517 rows=0 loops=3)
        Filter: (((last_name)::text = 'Ware'::text) AND ((first_name)::text = 'Selena'::text))
        Rows Removed by Filter: 166666
Planning Time: 0.153 ms
Execution Time: 212.580 ms

*/

-- optimalisation

create index ix_codecoolers_last_name_first_name on public.codecoolers (last_name, first_name);

-- query plan

/*

Index Only Scan using ix_codecoolers_last_name_first_name on codecoolers  (cost=0.42..4.44 rows=1 width=13) (actual time=0.322..0.325 rows=1 loops=1)
  Index Cond: ((last_name = 'Ware'::text) AND (first_name = 'Selena'::text))
  Heap Fetches: 0
Planning Time: 0.806 ms
Execution Time: 0.352 ms

*/

