import os
import json
from datetime import datetime


class FileStorage:
    """
    Serializes class object to a JSON
    file and deserializes JSON file to object.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Return the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add new object to __objects the
        obj with identifier <obj class name>.id.
        """
        identifier = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[identifier] = obj

    def save(self):
        """
        Write data from __objects to file.
        """
        with open(self.__file_path, "w") as file:

            objects = {}
            for identifier, data in self.__objects.items():
                objects[identifier] = data.to_dict()
            json.dump(objects, file, indent=4)
            return True

    def reload(self):
        """
        Load exiting data from file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_data = json.load(file)

                objects = {}
                for identifier, data in json_data.items():
                    objects[identifier] = self.convert_date_from_isoformat(data)

                self.__objects = objects
        return True

    def convert_date_from_isoformat(self, dict_data: dict):
        """
        convert datetime in isoformat to datetime object
        """

        if "created_at" in dict_data:
            dict_data["created_at"] = datetime.fromisoformat(dict_data["created_at"])
        if "updated_at" in dict_data:
            dict_data["updated_at"] = datetime.fromisoformat(dict_data["updated_at"])

        return dict_data
