from models.invoice import Invoice
from models.constants import ClassificationTypeLst, InvoiceStatusLst
from services.logger_service import log_invoice_update

def route_invoice_status(invoices: list[Invoice]):
    for item in invoices:
        if item.classification == ClassificationTypeLst.high.value:
            value = InvoiceStatusLst.high.value
        elif item.classification == ClassificationTypeLst.mid.value:
            value = InvoiceStatusLst.mid.value
        else:
            value = InvoiceStatusLst.low.value
        item.status = value
        log_invoice_update(
            invoice_id= item.invoice_id,
            vendor_name= item.vendor or "UNKNOWN",
            action= "INVOICE_STATUS_UPDATE",
            details= f"Invoice status has been updated to {value}"
        )
    return invoices

