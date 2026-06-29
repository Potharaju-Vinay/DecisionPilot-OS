from backend.planner.tool_registry import ToolRegistry

from backend.services.llm import LLMService

from backend.engines.rule_engine import RuleEngine
from backend.engines.risk_engine import RiskEngine
from backend.engines.analytics_engine import AnalyticsEngine
from backend.engines.scenario_engine import ScenarioEngine
from backend.engines.learning_engine import LearningEngine

from backend.knowledge.vector_store import EnterpriseVectorStore
from backend.knowledge.chunker import EnterpriseChunker


tool_registry = ToolRegistry()


tool_registry.register(

    "llm",

    LLMService()

)

tool_registry.register(

    "rule_engine",

    RuleEngine()

)

tool_registry.register(

    "risk_engine",

    RiskEngine()

)

tool_registry.register(

    "analytics_engine",

    AnalyticsEngine()

)

tool_registry.register(

    "scenario_engine",

    ScenarioEngine()

)

tool_registry.register(

    "learning_engine",

    LearningEngine()

)

tool_registry.register(

    "vector_store",

    EnterpriseVectorStore()

)

tool_registry.register(

    "chunker",

    EnterpriseChunker()

)