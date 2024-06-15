import uuid
from datetime import datetime


class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return f"[{self.__class__}] (<{self.id}>) <{str(self.__dict__)}>"
