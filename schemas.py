from pydantic import BaseModel

class Item(BaseModel):
    file: str
    correlationId: str | None
    decoded: str | None
    src: str | None