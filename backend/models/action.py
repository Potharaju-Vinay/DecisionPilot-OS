from pydantic import BaseModel


class Action(BaseModel):

    id: str = ""

    description: str

    owner: str

    due_date: str

    status: str = "Pending"