"""Laboratory work 6"""
import os
import logging
import functools
import json

mode = "console"


class FileNotFound(OSError):
    """
    Exception class for file not found.
    """


class FileCorrupted(OSError):
    """
    Exception class for corrupted file.
    """


def logged(exception, report_mode):
    """
    Decorator function that accepts 2 arguments and adds logging functionality.
    """
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if report_mode == "console":
                    logging.error(f"Logged Error: {e}")
                elif report_mode == "file":
                    logging.basicConfig(
                        filename='logs.txt', 
                        level=logging.ERROR,
                        format='%(asctime)s %(message)s'
                    )
                    logging.exception(f"Exception occurred: {e}")
                raise
        return wrapper
    return inner


class Changer:
    """
    Class for working with JSON files.
    """

    @logged(FileNotFound, mode)
    def __init__(self, file_name, path_to_file):
        self.file_name = file_name
        self.path_to_file = path_to_file
        self.full_path = os.path.join(self.path_to_file, self.file_name)

        if not os.path.exists(self.full_path):
            raise FileNotFound(f"File '{self.file_name}' not found")

    @logged(FileCorrupted, mode)  # adds logging in method
    def write_to_file(self, data):
        """
        Method to append data to the file.
        """
        try:
            with open(self.full_path, "r", encoding='utf-8') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []

            if not isinstance(existing_data, list):
                existing_data = [existing_data]

            existing_data.append(data)
            with open(self.full_path, "w", encoding='utf-8') as f:
                json.dump(existing_data, f, indent=4)

        except OSError as e:
            raise FileCorrupted(f"Failed to write to '{self.file_name}'") from e

    @logged(FileCorrupted, mode)  # adds logging in method
    def read_from_file(self):
        """
        Method to read from the file.
        """
        try:
            with open(self.full_path, "r", encoding='utf-8') as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            raise FileCorrupted(f"Failed to read '{self.file_name}'") from e


if __name__ == "__main__":
    file1 = Changer("lab6file.json", "")
    file1.write_to_file({"id": 22, "test": "data"})
