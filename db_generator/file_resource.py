import random
import os
import sys

class FileResource:

    data = []

    @classmethod
    def get_random(cls):
        if not cls.data:
            cls.load_data()

        return random.choice(cls.data)


    @classmethod
    def load_file(cls):
        with open(os.path.join(sys.path[0], "resources/", cls.file_name), encoding="utf-8") as f: 
            lines = f.readlines() 

        return lines