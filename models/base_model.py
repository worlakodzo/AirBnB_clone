import uuid
from datetime import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return f"[{self.__class__}] (<{self.id}>) <{str(self.__dict__)}>"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "__class__": str(self.__class__),
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
