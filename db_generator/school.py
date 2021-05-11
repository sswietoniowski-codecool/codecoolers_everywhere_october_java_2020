from city import City


class School():

    @classmethod
    def generate_random(cls):
        city = City.generate_random()

        return cls(
            "Codecool {location}".format(city.name),
            city.identifier
        )

    @classmethod
    def generate_randoms(cls, quantity):
        cities = City.generate_randoms(quantity)

        to_return = []
        for city in cities:
            to_return.append(
                cls(
                    "Codecool {location}".format(location=city.name),
                    city.identifier
                )
            )

        return to_return

    def __init__(self, name, city_id):
        self.name = name
        self.city_id = city_id
