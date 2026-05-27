from models.invoice import Invoice
from services.validation_service import validate_invoice_compliance as vic
import json
from pathlib import Path
from services.logger_service import log_invoice_update

def load_invoices(file_path: Path):
    #Opens the file, maps to models, runs validation, and splits data into clean and invalid collections.
    if not file_path.exists():
        raise FileNotFoundError(f"Could not find file at: {file_path}")
        log_invoice_update(
            invoice_id= "UNKNOWN",
            vendor_name= "UNKNOWN",
            action= "INVOICE_FILE_NOT_FOUND",
            details=  f"Errors found: CRITICAL INGESTION FAILURE: The file layout path was not found at: {file_path}"
        )
    
    with open(file=file_path, mode="r", encoding= "utf-8") as f:
        invoices_data = json.loads(f.read())

    invalid_invoices= []
    clean_invoices = []
    
    for item in invoices_data:
        # Convert dictionary to Pydantic object
        invoice_instance = Invoice(**item)
         # Run validation immediately inside the ingestion loop
        audited_invoice = vic(invoice_instance)
        # Split the data into your separate streams right here
        if audited_invoice.is_valid:
            clean_invoices.append(audited_invoice)
        '''else:
            invalid_invoices.append(audited_invoice)''' #Commented invalid invoices because currently Im not working with invalid data
    return clean_invoices
