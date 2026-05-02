from pydantic import BaseModel
from typing import Optional


class SummaryOutput(BaseModel):
    title: str
    summary: str
    category: str
    filename: str
    author: Optional[str] = "Unknown"
    date: Optional[str] = None
