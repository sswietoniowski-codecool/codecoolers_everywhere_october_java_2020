# Codecoolers everywhere!!!

## Story

![Codecoolers, Codecoolers everywhere](https://i.imgflip.com/44j3vf.jpg)

It's 2120. Humanity is still okay. We survived COVID-19 and it's more dangerous predecessors as well a hundred years ago. People also started to realise back then, that things can't go the way it went before, so Earth and its climate has been saved as well.

One thing hasn't changed: the interest in programming and the need for programmers. Codecool became the biggest training center all over the world while companies like Apple, Google or Tesla are only foggy memories in the past.

Codecool spreaded all over the world. There's a school in nearly every city, with millions of active Codecoolers.

Another thing hasn't changed either: our backend systems. They are slow, buggy, moreover the sourcecode has been lost, and it can't be reverse engineered. It's a total mess!

There's something else which hasn't changed! SQL!!! SQL is still with us, and stores our data in a relational way. Although we don't have the source code of the office application, we have a database dump from our internal database. We also know the administrators' needs, so it's your job to rewrite and optimalize the queries retreiving the relevant data for them.

## What are you going to learn?

- repeat and practice joining tables
- repeat and practice SQL aggregate functions
- analyzing tables and query performance
- indexing tables

## Tasks

1. List all user stories on the opening page.
    - `database.sql` is generated with the provided script
    - `database.sql` is dumped into a database

2. Query Codecoolers having the same first and last names and the number of each identical names. Order the result by this number in descending order
    - `query-identical-names-with-counter.sql` contains a query which returns columns `last_name`, `first_name`, and a `counter`
    - The query gives back rows with unique first and last name pairs, and the counter shows the number of matches
    - The result is ordered based on the counter in descending order (largest first)

3. Give back all attributes (but only those) of Codecoolers who have applied to the school located in their hometown
    - `query-students-applying-in-hometown.sql` contains a query which returns `id`, `last_name`, `first_name`, `birth_year`, `birth_city_id` (and nothing else)
    - The returned students have an application to their hometown's school

4. Give back all attributes (but only those) of Codecoolers who have not applied to the existing school located in their hometown
    - `query-students-not-applying-in-hometown.sql` contains a query which returns `id`, `last_name`, `first_name`, `birth_year`, `birth_city_id` (and nothing else)
    - The returned students have no application to their hometown's existing school

5. One of the most used feature in the office system is to search for students based on their first and last names. This is an easy query right? Write one to select students called Ware Selena. It's a bit slow for a frequently used query, right? Check the reasons behind with analyzing the query. Based on the analysis, it's your job now to optimize the database to perform under this query better.
    - `query-students-name-with-optimisation.sql` contains a query which returns all Codecoolers called Ware Selena.
    - `query-students-name-with-optimisation.sql` contains a query which analyses the previous one, and its output shows the query plan and its run time
    - `query-students-name-with-optimisation.sql` contains an SQL statement which optimises the database to perform better on this query
    - `query-students-name-with-optimisation.sql` contains a query which analyses the previous one, and it's output showing the query plan and it's runtime

6. You optimised the query above and a lot of others. But as time running by, our database gets slower and slower, and its size increases in an unexpected way. Solve the problem!
    - `optimise-indices-after-modification.sql` contains an SQL statement which optimises the database and its storage page

## General requirements

None

## Hints

- Be aware that this task has a focus on SQL, so you shouldn't seek neither objects or classes nor for the famous main method to make the code work:).

- Since we didn't want to push a database with the size of about 1GB, we created a Python script which generates a database dump on your machine with random cities, Codecoolers, schools and connection between these entities. In order to create your database, run **only** the `db_generator.py` in the `db_generator` subfolder. This script creates a `database.sql`, which you can dump into PostgreSQL in the known way. Please be reminded that both of the tasks (generating the DB/dumping it to PostgreSQL) can take a serious amount of time (0.5h/1.5h) depending on your computer's performance
- for optimalisation, you should better read about indexes
- when coming to performance issues, query analisation `EXPLAIN (ANALYSE)` is your friend
- when dumping the data into the database, don't forget to set UTF-8 as an encoding (check the `PGCLIENTENCODING` environment variable)
- in case the dump process terminates with an error code, your machine may have less free memory what needed. In that case open `db_generator/db_generator.py`, and modify the `codecooler_num` variable to `500000` (five hundred thousand). Run the python and the sql dump processes again.



## Background materials

- <i class="far fa-exclamation"></i> [Efficient Use of PostgreSQL Indexes](https://devcenter.heroku.com/articles/postgresql-indexes)
- <i class="far fa-exclamation"></i> [Reading a Postgres EXPLAIN ANALYZE Query Plan](https://thoughtbot.com/blog/reading-an-explain-analyze-query-plan)
- <i class="far fa-exclamation"></i> [Optimize and Improve PostgreSQL Performance with VACUUM, ANALYZE, and REINDEX](https://confluence.atlassian.com/kb/optimize-and-improve-postgresql-performance-with-vacuum-analyze-and-reindex-885239781.html)


