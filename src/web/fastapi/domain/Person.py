from datetime import datetime

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    governmentId: str
    email: str
    debtAmount: float
    debtDueDate: str
    debtId: str
