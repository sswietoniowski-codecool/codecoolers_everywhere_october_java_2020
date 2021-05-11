from codecooler import Codecooler
from city import City
from school import School
import os
import sys
import random


class DBGenerator():

    codecooler_num = 10000000
    percentage_to_log = 100
    school_num = 10000
    max_number_of_schools_per_codecooler = 5
    database_filename = "database.sql"

    @classmethod
    def log_percentage(cls, actual, all, message):
        if ((actual) % (all / cls.percentage_to_log)) == 0:
            percent = int(((actual) / all) * 100)
            print(" {percent}% {message} {ratio}".format(
                percent=percent,
                message=message,
                ratio="({actual}/{all})".format(actual=actual, all=all)
            ), end="\r", flush=True)
            if percent == 100:
                print()

    def log_start_and_end(message):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print("{message} started...".format(message=message))
                func(*args, **kwargs)
                print("{message} ended!".format(message=message))
            return wrapper
        return decorator

    def sql_generator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            args[0].save_sql()

        return wrapper

    def __init__(self):
        self.sql_string = ""
        if os.path.exists(self.database_filename):
            os.remove(self.database_filename)

    def generate_sql(self):
        self.generate_schema()
        self.sql_string += "BEGIN;\n"
        self.generate_cities()
        self.generate_schools(self.school_num)
        self.generate_codecoolers(self.codecooler_num)
        self.generate_codecoolers_schools()
        self.sql_string += "COMMIT;\n"
        self.generate_constraints()
        self.save_sql()

    def save_sql(self):
        with(open(os.path.join(sys.path[0], self.database_filename), 'a', encoding="utf-8")) as f:
            f.write(self.sql_string)

        self.sql_string = ""

    @log_start_and_end("Generating DB Schema")
    @sql_generator
    def generate_schema(self):
        with open(os.path.join(sys.path[0], "resources/", "schema.sql"), encoding="utf-8") as f:
            self.sql_string += f.read()

        self.generate_new_line()

    @log_start_and_end("Generating constraints")
    @sql_generator
    def generate_constraints(self):
        with open(os.path.join(sys.path[0], "resources/", "constraints.sql"), encoding="utf-8") as f:
            self.sql_string += f.read()

        self.generate_new_line()

    @log_start_and_end("Generating cities")
    @sql_generator
    def generate_cities(self):
        sql_parts = []
        City.load_data()
        cities = City.data
        number_of_cities = len(cities)
        for city in cities:
            sql_parts.append("({id}, '{name}', '{country}')".format(
                id=city.identifier,
                name=city.name,
                country=city.country
            ))
            self.log_percentage(city.identifier, number_of_cities, "of the Cities are generated")

        self.sql_string += "INSERT INTO public.cities (id, name, country) VALUES \n"
        self.sql_string += ", \n".join(sql_parts) + ";\n"
        self.generate_new_line()

    @log_start_and_end("Generating Codecoolers")
    @sql_generator
    def generate_codecoolers(self, number):
        sql_parts = []
        for i in range(0, number):
            codecooler = Codecooler.generate_random()
            sql_parts.append("({id}, '{last_name}', '{first_name}', {birth_year}, {birth_city_id})".format(
                id=i+1,
                last_name=codecooler.last_name,
                first_name=codecooler.first_name,
                birth_year=codecooler.birth_year,
                birth_city_id=codecooler.birth_city_id
            ))
            self.log_percentage(i+1, number, "of the Codecoolers are generated")
        self.sql_string += "INSERT INTO public.codecoolers (id, last_name, first_name, birth_year, birth_city_id) VALUES \n"
        self.sql_string += ", \n".join(sql_parts) + ";\n"
        self.generate_new_line()

    @log_start_and_end("Generating Schools")
    @sql_generator
    def generate_schools(self, number):
        sql_parts = []

        schools = School.generate_randoms(number)

        for i, school in enumerate(schools):
            sql_parts.append("({id}, '{name}', {city_id})".format(
                id=i+1,
                name=school.name,
                city_id=school.city_id
            ))
            self.log_percentage(i+1, number, "of the Schools are generated")
        self.sql_string += "INSERT INTO public.schools (id, name, city_id) VALUES \n"
        self.sql_string += ", \n".join(sql_parts) + ";\n"
        self.generate_new_line()

    @log_start_and_end("Generating connections between Codecoolers and Schools")
    @sql_generator
    def generate_codecoolers_schools(self):
        sql_parts = []

        codecooler_ids = range(1, self.codecooler_num+1)
        school_ids = list(range(1, self.school_num+1))
        for codecooler_id in codecooler_ids:
            random_school_ids = random.sample(school_ids, random.randint(1, self.max_number_of_schools_per_codecooler))
            for school_id in random_school_ids:
                sql_parts.append("({codecooler_id}, {school_id})".format(
                    codecooler_id=codecooler_id,
                    school_id=school_id
                ))
            self.log_percentage(codecooler_id, self.codecooler_num, "of the connections are generated")

        self.sql_string += "INSERT INTO public.codecoolers_schools (codecooler_id, school_id) VALUES \n"
        self.sql_string += ", \n".join(sql_parts) + ";\n"
        self.generate_new_line()

    def generate_new_line(self):
        self.sql_string += "\n"


if __name__ == '__main__':
    DBGenerator().generate_sql()
