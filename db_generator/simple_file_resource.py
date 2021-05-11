from file_resource import FileResource

class SimpleFileResource(FileResource):

    @classmethod
    def load_data(cls):
        cls.data = []
        file_data = cls.load_file()

        for line in file_data:
            cls.data.append(line.strip())
