from enum import Enum
# --- 1. WORKFLOW Status & Classification CONSTANTS (Enums) ---
class InvoiceStatusLst(str, Enum):
    high = "Finance Team + MD Approval Needed"
    mid = "Finance Team"
    low = "Auto Approve Queue"


class ClassificationTypeLst(str, Enum):
    high = "High Value"
    mid = "Mid Value"
    low = "Standard"


# --- 2. BUSINESS RULE CONSTANT (Invoice Amount Limits)---
HIGH_VALUE_THRESHOLD = 5000.00
MID_VALUE_THRESHOLD = 2000.00