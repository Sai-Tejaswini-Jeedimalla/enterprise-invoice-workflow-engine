from models.invoice import Invoice
from services.routing_service import route_invoice_status


def test_high_value_routing():
    invoice = Invoice(classification="high-value")

    result = route_invoice_status([invoice])

    assert result[0].status == "Finance Team + MD Approval Needed"