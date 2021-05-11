DROP TABLE IF EXISTS codecoolers_schools;
DROP TABLE IF EXISTS schools;
DROP TABLE IF EXISTS codecoolers;
DROP TABLE IF EXISTS cities;

CREATE TABLE codecoolers
(
    id integer not null,
    last_name  varchar not null,
    first_name varchar not null,
    birth_year integer not null,
    birth_city_id integer not null
);

CREATE TABLE schools
(
    id integer not null,
    name varchar not null,
    city_id integer not null
);

CREATE TABLE cities
(
	id int not null,
	name varchar not null,
	country varchar not null
);

CREATE TABLE codecoolers_schools
(
    codecooler_id int not null,
    school_id int not null
);