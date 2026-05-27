# services/validation.py

from models.invoice import Invoice
from services.logger_service import log_invoice_update

def validate_invoice_compliance(invoice: Invoice):
    #Checks an invoice against company rules and notes down any missing data.
    errors = []
    # Level 1 Check : Required Layout field
    if invoice.invoice_id is None:
        errors.append("Missing Invoice Id.")
    if not invoice.vendor and invoice.vendor.strip() == "":
        errors.append("Missing Vendor Name.")
    if invoice.date is None:
        errors.append("Missing date")
    if invoice.submitted_by is None:
        errors.append("Missing who submiteed the invoice")

    # Level 2 Check: Financial Audits
    if invoice.amount is None:
        errors.append("Missing Amount.")
    elif invoice.amount <= 0:
        errors.append(f"Amount (${invoice.amount}) is invalid. It must be greater than 0.")

    # we append the is_valid and reason to the invoice directly
    if errors:
        invoice.is_valid = False
        invoice.validation_reason = errors
        # LOG THE FAILURE: Record why this item was blocked
        log_invoice_update(
            invoice_id= invoice.invoice_id,
            vendor_name= invoice.vendor or "UNKNOWN",
            action= "VALIDATION_BLOCKED",
            details= f"Errors found: {errors}"
        )
    
    return invoice
    
    

