import os


class FileManager:

    @staticmethod
    def file_exists(path):

        return os.path.exists(path)

    @staticmethod
    def create_folder(path):

        if not os.path.exists(path):
            os.makedirs(path)