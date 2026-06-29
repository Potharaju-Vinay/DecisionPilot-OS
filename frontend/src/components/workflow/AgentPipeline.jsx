import {
    Database,
    Network,
    SearchCheck,
    Target,
    ShieldAlert,
    Brain,
    BookOpenCheck,
    Lightbulb,
    BarChart3
} from "lucide-react";

const pipeline = [

    {
        name: "Knowledge",
        agent: "KnowledgeAgent",
        icon: Database
    },

    {
        name: "Knowledge Graph",
        agent: "GraphAgent",
        icon: Network
    },

    {
        name: "Customer Discovery",
        agent: "CustomerDiscoveryAgent",
        icon: SearchCheck
    },

    {
        name: "ICP",
        agent: "ICPAgent",
        icon: Target
    },

    {
        name: "Risk",
        agent: "RiskAgent",
        icon: ShieldAlert
    },

    {
        name: "Decision",
        agent: "DecisionAgent",
        icon: Brain
    },

    {
        name: "Recommendation",
        agent: "RecommendationAgent",
        icon: BookOpenCheck
    },

    {
        name: "Explainability",
        agent: "ExplainabilityAgent",
        icon: Lightbulb
    },

    {
        name: "Analytics",
        agent: "AnalyticsAgent",
        icon: BarChart3
    }

];

function AgentCard({

    step,

    data

}) {

    const Icon = step.icon;

    const completed =
        data?.completed_agents?.includes(
            step.agent
        );

    const executionTime =
        data?.metrics?.[
            step.agent
        ] ?? "--";

    return (

        <div
            className={`min-w-[220px] rounded-2xl border p-5 transition-all duration-300
            ${
                completed
                    ? "bg-cyan-950 border-cyan-600"
                    : "bg-slate-900 border-slate-800"
            }`}
        >

            <div className="flex justify-between items-center">

                <Icon
                    size={28}
                    className={
                        completed
                            ? "text-cyan-400"
                            : "text-slate-500"
                    }
                />

                <span
                    className={`text-xs px-2 py-1 rounded-full
                    ${
                        completed
                            ? "bg-green-600 text-white"
                            : "bg-slate-700 text-slate-300"
                    }`}
                >
                    {completed ? "Completed" : "Pending"}
                </span>

            </div>

            <h3 className="text-white font-semibold mt-5">

                {step.name}

            </h3>

            <p className="text-slate-400 text-sm">

                {step.agent}

            </p>

            <div className="mt-5">

                <div className="flex justify-between text-sm">

                    <span className="text-slate-400">

                        Time

                    </span>

                    <span className="text-cyan-400">

                        {executionTime}s

                    </span>

                </div>

            </div>

        </div>

    );

}

function AgentPipeline({

    data

}) {

    return (

        <div className="bg-slate-900 rounded-2xl border border-slate-800 p-6">

            <div className="mb-6">

                <h2 className="text-2xl font-bold text-white">

                    Enterprise AI Workflow

                </h2>

                <p className="text-slate-400">

                    Multi-agent execution pipeline for enterprise decision intelligence

                </p>

            </div>

            <div className="flex gap-5 overflow-x-auto pb-3">

                {pipeline.map((step, index) => (

                    <div
                        key={step.agent}
                        className="flex items-center gap-5"
                    >

                        <AgentCard

                            step={step}

                            data={data}

                        />

                        {index !== pipeline.length - 1 && (

                            <div className="text-cyan-500 text-3xl font-bold">

                                →

                            </div>

                        )}

                    </div>

                ))}

            </div>

        </div>

    );

}

export default AgentPipeline;