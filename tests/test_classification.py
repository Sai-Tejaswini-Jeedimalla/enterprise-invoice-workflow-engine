from models.invoice import Invoice
from services.classification_service import classify_invoice


def test_high_value_invoice_classification():
    invoice = Invoice(amount=25000)

    result = classify_invoice([invoice])

    assert result[0].classification == "high-value"