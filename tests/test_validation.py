from models.invoice import Invoice
from services.validation_service import validate_invoice_compliance


def test_valid_invoice():
    invoice = Invoice(
        invoice_id="INV-100",
        vendor="Microsoft",
        amount=1000,
        submitted_by="John",
        date="2025-01-01"
    )

    validated = validate_invoice_compliance(invoice)

    assert validated.is_valid is True


def test_invalid_invoice_missing_amount():
    invoice = Invoice(
        invoice_id="INV-101",
        vendor="Google",
        submitted_by="John",
        date="2025-01-01"
    )

    validated = validate_invoice_compliance(invoice)

    assert validated.is_valid is False
    assert "Missing Amount." in validated.validation_reason