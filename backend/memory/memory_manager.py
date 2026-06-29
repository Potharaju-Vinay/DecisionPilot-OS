import json

from collections import defaultdict

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.database.models import WorkflowMemory

from backend.models.memory_record import MemoryRecord


class MemoryManager:

    def __init__(self):

        self.short_memory = []

        self.long_memory = []

        self.customer_memory = defaultdict(list)

    def add(
        self,
        record: MemoryRecord
    ):

        self.short_memory.append(record)

        self.long_memory.append(record)

        customer = record.metadata.get(
            "customer"
        )

        if customer:

            self.customer_memory[
                customer
            ].append(record)

        self._persist(record)

    def _persist(
        self,
        record: MemoryRecord
    ):

        db: Session = SessionLocal()

        try:

            value = record.value

            workflow = WorkflowMemory(

                workflow_id=record.id,

                customer=record.metadata.get(
                    "customer"
                ),

                query=value.get(
                    "query"
                ),

                document_source=record.metadata.get(
                    "document_source"
                ),

                fingerprint=record.metadata.get(
                    "document_fingerprint"
                ),

                decision=json.dumps(
                    value.get("decision")
                ),

                recommendation=json.dumps(
                    value.get("recommendation")
                ),

                explanation=json.dumps(
                    value.get("explanation")
                ),

                business_score=record.metadata.get(
                    "business_score"
                ),

                risk_score=record.metadata.get(
                    "risk_score"
                ),

                confidence=record.metadata.get(
                    "confidence"
                ),

                created_at=record.metadata.get(
                    "timestamp"
                )

            )

            db.add(workflow)

            db.commit()

        finally:

            db.close()

    def get(
        self,
        key: str
    ):

        for record in reversed(
            self.short_memory
        ):

            if record.key == key:

                return record

        return None

    def get_latest(self):

        if not self.short_memory:

            return None

        return self.short_memory[-1]

    def get_recent(
        self,
        limit=10
    ):

        return self.short_memory[-limit:]

    def get_customer_history(
        self,
        customer: str
    ):

        db = SessionLocal()

        try:

            return db.query(

                WorkflowMemory

            ).filter(

                WorkflowMemory.customer == customer

            ).all()

        finally:

            db.close()

    def search(
        self,
        keyword: str
    ):

        keyword = keyword.lower()

        results = []

        for record in self.long_memory:

            if keyword in str(
                record.value
            ).lower():

                results.append(record)

        return results

    def statistics(self):

        db = SessionLocal()

        try:

            workflow_count = db.query(
                WorkflowMemory
            ).count()

        finally:

            db.close()

        return {

            "short_memory": len(self.short_memory),

            "long_memory": len(self.long_memory),

            "persistent_workflows": workflow_count,

            "customers": len(self.customer_memory)

        }

    def clear(self):

        self.short_memory.clear()

        self.long_memory.clear()

        self.customer_memory.clear()

    def all(self):

        return self.short_memory