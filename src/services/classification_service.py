from models.invoice import Invoice
from services.logger_service import log_invoice_update
from models.constants import ClassificationTypeLst, HIGH_VALUE_THRESHOLD, MID_VALUE_THRESHOLD

def classify_invoice(invoices: list[Invoice]):
    for item in invoices:
        if item.amount > HIGH_VALUE_THRESHOLD:
            value = ClassificationTypeLst.high.value
        elif item.amount > MID_VALUE_THRESHOLD:
            value = ClassificationTypeLst.mid.value
        else:
            value = ClassificationTypeLst.low.value
        item.classification = value
        log_invoice_update(
            invoice_id= item.invoice_id,
            vendor_name= item.vendor or "UNKNOWN",
            action= "INVOICE_CLASSIFICATION",
            details= f"Invoice classification has been updated to {value}"
        )
    return invoices
