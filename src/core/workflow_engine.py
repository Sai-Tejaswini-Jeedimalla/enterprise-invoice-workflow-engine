# core/workflow_engine.py

from pathlib import Path
from collections import Counter
from services.validation_service import validate_invoice_compliance
from services.ingestion_service import load_invoices
from services.classification_service import classify_invoice
from services.routing_service import route_invoice_status


class WorkflowEngine:
    """
    Enterprise Workflow Engine responsible for:
    - pipeline orchestration
    - execution flow
    - workflow metrics
    - stage coordination
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def run(self):
        # Stage 1 - Ingestion + Validation
        clean_invoices = load_invoices(self.file_path)

        # Stage 2 - Classification
        classified_invoices = classify_invoice(clean_invoices)

        # Stage 3 - Routing
        routed_invoices = route_invoice_status(classified_invoices)

        # Stage 4 - Metrics
        metrics = self.generate_metrics(routed_invoices)

        return routed_invoices, metrics

    @staticmethod
    def generate_metrics(invoices: list):
        status_metrics = Counter([inv.status for inv in invoices])
        classification_metrics = Counter(
            [inv.classification for inv in invoices]
        )

        return {
            "total_invoices": len(invoices),
            "status_metrics": status_metrics,
            "classification_metrics": classification_metrics
        }