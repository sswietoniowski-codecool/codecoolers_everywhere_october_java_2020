from first_name import FirstName
from last_name import LastName
from city import City
import random


class Codecooler():

    @classmethod
    def generate_random(cls):
        return cls(
            FirstName.get_random(),
            LastName.get_random(),
            random.randint(2050, 2100),
            random.randint(1, len(City.data))
        )

    def __init__(self, first_name, last_name, birth_year, birth_city_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_city_id = birth_city_id
