import logging
from pathlib import Path

log_file_path = Path(__file__).resolve().parents[2]/"logs"/"app.log"

logging.basicConfig(
    filename= log_file_path,
    filemode= "a",
    format= "%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_invoice_update(invoice_id: int, vendor_name: str, action: str, details: str):
    """Writes a clean, auditable timeline row to the log file."""
    log_message = f"INV-{invoice_id} | {vendor_name} | ACTION: {action} | DETAILS: {details}"
    logging.info(log_message)