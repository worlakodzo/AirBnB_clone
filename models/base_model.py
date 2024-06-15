import uuid
from datetime import datetime


class BaseModel:
    """
    A base class models.
    """

    def __init__(self) -> None:
        self.my_number = 0
        self.name = None
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        Return a string representation of the BaseModel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the BaseModel.
        """
        return {
            "my_number": self.my_number,
            "name": self.name,
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
