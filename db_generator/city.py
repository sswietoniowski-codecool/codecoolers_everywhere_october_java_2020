from file_resource import FileResource
import random


class City(FileResource):

    file_name = "cities.txt"

    @classmethod
    def generate_random(cls):
        return random.choice(cls.data)

    @classmethod
    def generate_randoms(cls, quantity):
        return random.sample(cls.data, quantity)

    def __init__(self, identifier, name, country):
        self.identifier = identifier
        self.name = name
        self.country = country

    @classmethod
    def load_data(cls):
        cls.data = []
        file_data = cls.load_file()

        for index, line in enumerate(file_data):
            line_data = line.split(",")
            cls.data.append(cls(
                index+1, 
                line_data[0].replace("'", ""), 
                line_data[1].replace("'", "")
            ))
