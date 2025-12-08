import os
import logging
import functools
import json

mode = "file"

class FileNotFound(OSError):
    pass

class FileCorrupted(OSError):
    pass

def logged(exception, mode):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(f"Logged Error: {e}")
                elif mode == "file":
                    logging.basicConfig(filename='logs.txt', level=logging.ERROR, format='%(asctime)s %(message)s')
                    logging.exception(f"Exception occurred: {e}")
                raise 
        return wrapper
    return inner

class Changer:
    """Клас для роботи з JSON файлом"""
    
    @logged(FileNotFound, mode)
    def __init__(self, file_name, path_to_file):
        self.file_name = file_name
        self.path_to_file = path_to_file
        self.full_path = os.path.join(self.path_to_file, self.file_name)

        if not os.path.exists(self.full_path):
            raise FileNotFound(f"File '{self.file_name}' not found")

    @logged(FileCorrupted, mode)
    def write_to_file(self, data):
        try:
            with open(self.full_path, "r") as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []

            if not isinstance(existing_data, list):
                existing_data = [existing_data]

            existing_data.append(data)
            with open(self.full_path, "w") as f:
                json.dump(existing_data, f, indent=4)

        except OSError as e:
            raise FileCorrupted(f"Failed to write to '{self.file_name}'") from e

    @logged(FileCorrupted, mode)
    def read_from_file(self):
        try:
            with open(self.full_path, "r") as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            raise FileCorrupted(f"Failed to read '{self.file_name}'") from e


file1 = Changer("lab5file.json", "")

file1.write_to_file({"id": 22, "test": "data"})