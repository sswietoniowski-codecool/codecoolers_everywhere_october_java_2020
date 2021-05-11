-- Please write the task's solution below

-- przydatne materiały: https://confluence.atlassian.com/kb/optimize-and-improve-postgresql-performance-with-vacuum-analyze-and-reindex-885239781.html

-- teoretycznie można zrobić:

VACUUM FULL;

-- w praktyce w najnowszych wersjach PostgreSQL nie jest to ani konieczne, ani bardzo potrzebne, gdyż ten proces zachodzi automatycznie,
-- czy tak się faktycznie dzieje można sprawdzić poprzez:

select name, setting from pg_settings where name = 'autovacuum' ;

-- w ramach przydatnych zasobów nieco o indeksowaniu w PostgreSQL:

-- https://devcenter.heroku.com/articles/postgresql-indexes

-- to już domena administratorów BD a nie deweloperów, ale gdyby ktoś chciał...

-- nieco zaleceń dotyczących konfiguracji serwera BD dla zapewnienia jego odpowiedniej wydajności

-- https://stackify.com/postgresql-performance-tutorial/

-- uzupełnienie do EXPLAIN ANALYZE i jego wyników:

-- https://www.enterprisedb.com/blog/postgresql-query-optimization-performance-tuning-with-explain-analyze

