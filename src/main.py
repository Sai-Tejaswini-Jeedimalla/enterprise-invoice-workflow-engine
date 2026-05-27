# main.py

from pathlib import Path
from core.workflow_engine import WorkflowEngine


def main():
    root_dir = Path(__file__).resolve().parents[1]
    file_path = root_dir / "data" / "invoices.json"

    try:
        engine = WorkflowEngine(file_path=file_path)

        _, metrics = engine.run()

        print("\n" + "=" * 60)
        print("ENTERPRISE WORKFLOW EXECUTION COMPLETE")
        print("=" * 60)

        print(f"TOTAL INVOICES: {metrics['total_invoices']}")

        print("\nSTATUS METRICS:")
        for status, count in metrics["status_metrics"].items():
            print(f" -> {status}: {count}")

        print("\nCLASSIFICATION METRICS:")
        for classification, count in metrics["classification_metrics"].items():
            print(f" -> {classification}: {count}")

        print("=" * 60 + "\n")

    except Exception as e:
        print(f"Workflow Execution Failed: {e}")


if __name__ == "__main__":
    main()