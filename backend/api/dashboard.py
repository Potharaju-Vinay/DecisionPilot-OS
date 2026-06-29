from fastapi import APIRouter

latest_dashboard = {}
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
async def dashboard():

    if latest_dashboard:

        return latest_dashboard

    return {

        "customer_discovery": {

            "company": "ABC Technologies",

            "industry": "Technology",

            "budget": "Approved",

            "timeline": "Q3 2026",

            "opportunity_score": 88,

            "business_goals": [

                "Reduce operational costs",

                "Improve AI automation"

            ],

            "pain_points": [

                "Manual proposal review",

                "Slow approvals"

            ],

            "buying_signals": [

                "Budget approved",

                "CTO requested technical demo"

            ],

            "decision_makers": [

                "CTO",

                "Procurement Manager"

            ]

        },

        "icp": {

            "score": 91,

            "qualified": True,

            "industry": "Technology",

            "company_size": "Enterprise",

            "budget": "Approved",

            "decision_maker": "CTO",

            "reasoning": "Customer strongly matches the enterprise ICP."

        },

        "risk": {

            "overall_risk": "LOW",

            "business_score": 91,

            "risk_score": 12,

            "compliance_score": 96,

            "approval_score": 94,

            "summary": "Low overall business risk."

        },

        "rule_result": {

            "triggered_rules": [

                {

                    "id": "BR001",

                    "name": "Budget Approved",

                    "description": "Budget already approved.",

                    "score": 15

                },

                {

                    "id": "BR002",

                    "name": "Executive Sponsor",

                    "description": "CTO involved.",

                    "score": 20

                }

            ],

            "audit_trail": [

                {

                    "rule_name": "Budget Approved",

                    "reason": "Budget approval detected."

                },

                {

                    "rule_name": "Executive Sponsor",

                    "reason": "CTO identified."

                }

            ]

        },

        "decision": {

            "decision": "APPROVE",

            "confidence": 0.96,

            "reasoning": "Strong customer qualification with low business risk.",

            "evidence": [

                "Budget approved",

                "Technical demo requested",

                "High ICP score"

            ],

            "risks": [

                "Contract pending"

            ],

            "recommendations": [

                "Schedule technical demo",

                "Prepare commercial proposal"

            ]

        },

        "recommendation": {

            "priority": "High",

            "owner": "Sales Director",

            "timeline": "7 Days",

            "summary": "Proceed with technical validation.",

            "actions": [

                {

                    "id": "ACT001",

                    "description": "Schedule technical demo",

                    "owner": "Sales Engineer",

                    "due_date": "2026-06-30",

                    "status": "Pending"

                },

                {

                    "id": "ACT002",

                    "description": "Prepare proposal",

                    "owner": "Account Manager",

                    "due_date": "2026-07-01",

                    "status": "Pending"

                }

            ]

        },

        "explanation": {

            "summary": "Customer qualifies with low risk.",

            "explanation": "Decision based on ICP score, business rules and risk assessment."

        },

        "knowledge_graph": {

            "nodes": [

                {
                    "id": "1",
                    "type": "default",
                    "position": {"x": 300, "y": 40},
                    "data": {"label": "ABC Technologies", "type": "company"}
                },

                {
                    "id": "2",
                    "type": "default",
                    "position": {"x": 120, "y": 180},
                    "data": {"label": "Technology", "type": "industry"}
                },

                {
                    "id": "3",
                    "type": "default",
                    "position": {"x": 300, "y": 180},
                    "data": {"label": "CTO", "type": "person"}
                },

                {
                    "id": "4",
                    "type": "default",
                    "position": {"x": 500, "y": 180},
                    "data": {"label": "Budget Approved", "type": "budget"}
                },

                {
                    "id": "5",
                    "type": "default",
                    "position": {"x": 700, "y": 180},
                    "data": {"label": "Q3 2026", "type": "timeline"}
                },

                {
                    "id": "6",
                    "type": "default",
                    "position": {"x": 150, "y": 350},
                    "data": {"label": "Reduce Costs", "type": "goal"}
                },

                {
                    "id": "7",
                    "type": "default",
                    "position": {"x": 350, "y": 350},
                    "data": {"label": "AI Automation", "type": "goal"}
                },

                {
                    "id": "8",
                    "type": "default",
                    "position": {"x": 550, "y": 350},
                    "data": {"label": "Technical Demo", "type": "signal"}
                },

                {
                    "id": "9",
                    "type": "default",
                    "position": {"x": 750, "y": 350},
                    "data": {"label": "Procurement Manager", "type": "person"}
                },

                {
                    "id": "10",
                    "type": "default",
                    "position": {"x": 450, "y": 520},
                    "data": {"label": "LOW Risk", "type": "risk"}
                },

                {
                    "id": "11",
                    "type": "default",
                    "position": {"x": 450, "y": 690},
                    "data": {"label": "APPROVE", "type": "decision"}
                },

                {
                    "id": "12",
                    "type": "default",
                    "position": {"x": 450, "y": 860},
                    "data": {"label": "Schedule Demo", "type": "action"}
                }

            ],

            "edges": [

                {"id":"e1","source":"1","target":"2"},
                {"id":"e2","source":"1","target":"3"},
                {"id":"e3","source":"1","target":"4"},
                {"id":"e4","source":"4","target":"5"},
                {"id":"e5","source":"3","target":"8"},
                {"id":"e6","source":"2","target":"6"},
                {"id":"e7","source":"2","target":"7"},
                {"id":"e8","source":"8","target":"10"},
                {"id":"e9","source":"10","target":"11"},
                {"id":"e10","source":"11","target":"12"},
                {"id":"e11","source":"9","target":"3"}

            ]

        },

        "analytics": {

            "workflow_time": 2.14,

            "documents_processed": 1,

            "success_rate": 100

        },

        "metrics": {

            "KnowledgeAgent": 0.12,

            "GraphAgent": 0.05,

            "CustomerDiscoveryAgent": 0.08,

            "ICPAgent": 0.04,

            "RiskAgent": 0.05,

            "DecisionAgent": 0.91,

            "RecommendationAgent": 0.72,

            "ExplainabilityAgent": 0.81,

            "AnalyticsAgent": 0.03

        },

        "completed_agents": [

            "KnowledgeAgent",

            "GraphAgent",

            "CustomerDiscoveryAgent",

            "ICPAgent",

            "RiskAgent",

            "DecisionAgent",

            "RecommendationAgent",

            "ExplainabilityAgent",

            "AnalyticsAgent"

        ],

        "logs": [

            "Knowledge extracted.",

            "Knowledge graph generated.",

            "Customer discovery completed.",

            "ICP qualified.",

            "Risk calculated.",

            "Decision generated.",

            "Recommendation generated.",

            "Explanation generated."

        ],

        "personas": {

            "executive": {

                "summary": "Strong business opportunity.",

                "insights": [

                    "High ICP",

                    "Low Risk"

                ],

                "actions": [

                    "Approve Opportunity"

                ]

            },

            "sales": {

                "summary": "Customer ready for next engagement.",

                "insights": [

                    "Technical demo requested"

                ],

                "actions": [

                    "Schedule Demo"

                ]

            },

            "compliance": {

                "summary": "No compliance issues.",

                "insights": [

                    "Policy compliant"

                ],

                "actions": [

                    "Archive report"

                ]

            },

            "technical": {

                "summary": "Deployment feasible.",

                "insights": [

                    "Cloud ready"

                ],

                "actions": [

                    "Prepare architecture"

                ]

            }

        }

    }