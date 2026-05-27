# models/invoice.py
from pydantic import BaseModel, Field
from typing import Optional, List

class Invoice(BaseModel):
    invoice_id: Optional[str] = None
    vendor: Optional[str] = None
    amount: Optional[float] = None
    submitted_by: Optional[str] = None
    date: Optional[str] = None
    is_valid: bool = True
    validation_reason: List[str] = Field(default_factory=list)
    classification: str = "low-value"
    status: str = "New"