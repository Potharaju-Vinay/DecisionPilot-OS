from pathlib import Path
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from backend.execution.workflow_context import WorkflowContext
from backend.services.input_engine import UniversalInputEngine
from backend.planner.router import PlannerRouter
from backend.builders.dashboard_builder import DashboardBuilder
from backend.api.dashboard import (
    router as dashboard_router,
    latest_dashboard
)


app = FastAPI(
    title="DecisionPilot OS",
    version="1.0.0"
)
app.include_router(dashboard_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():

    return {
        "message": "DecisionPilot OS Backend Running"
    }



@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    upload_path = upload_dir / file.filename

    with open(upload_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    engine = UniversalInputEngine()

    document = engine.parse(
        str(upload_path)
    )

    print("\n========== PARSED DOCUMENT ==========\n")
    print(document)
    print("\n=====================================\n")

    context = WorkflowContext()

    context.set(
        "parsed_document",
        document
    )

    context.set(
        "query",
        "Analyze this business opportunity."
    )

    planner = PlannerRouter()

    context = await planner.execute(
        context
    )

    analytics = context.get("analytics")
    decision = context.get("decision")
    recommendation = context.get("recommendation")
    explanation = context.get("explanation")
    dashboard = DashboardBuilder.build(context)
    print("========== DASHBOARD BUILDER ==========")
    print(dashboard)
    print("=======================================")

    latest_dashboard.clear()

    
    latest_dashboard.update(dashboard)

    print("========== LATEST DASHBOARD ==========")
    print(latest_dashboard)
    print("======================================")
    
    return {

        "business_score": analytics.business_score,

        "risk_score": analytics.risk_score,

        "confidence": round(
            analytics.decision_confidence * 100,
            2
        ),

        "health": analytics.overall_health,

        "decision": decision.decision,

        "reasoning": decision.reasoning,

        "recommendation": recommendation.summary,

        "explanation": explanation.explanation

    }