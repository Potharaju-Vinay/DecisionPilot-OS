import {
    Brain,
    FileSearch,
    ShieldAlert,
    Scale,
    Network,
    ChevronRight
} from "lucide-react";

function Section({

    title,

    icon,

    content

}) {

    const Icon = icon;

    return (

        <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

            <div className="flex items-center gap-3 mb-4">

                <Icon

                    size={20}

                    className="text-cyan-400"

                />

                <h3 className="text-lg font-semibold text-white">

                    {title}

                </h3>

            </div>

            <p className="text-slate-300 leading-7 whitespace-pre-line">

                {

                    content ||

                    "No information available."

                }

            </p>

        </div>

    );

}

function ExplainabilityPanel({

    data

}) {

   const explanation = data?.explanation || {};
   
   const decision = data?.decision || {};
   
   const risk = data?.risk || {};
   
   const rules = data?.rule_result || {};
   
   const graph = data?.knowledge_graph || {};
   
   const summary = explanation.summary || "";

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        Explainable AI

                    </h2>

                    <p className="text-slate-400">

                        Transparent reasoning behind every AI decision

                    </p>

                </div>

                <Brain

                    size={40}

                    className="text-cyan-400"

                />

            </div>

            <div className="bg-gradient-to-r from-cyan-950 to-slate-900 border border-cyan-700 rounded-xl p-6 mb-6">

                <h3 className="text-lg font-semibold text-white mb-3">

                    Executive Summary

                </h3>

                <div className="flex gap-4 mt-4">

                    <div className="bg-cyan-600 rounded-lg px-4 py-2">

                        <p className="text-xs text-white">

                            Decision

                        </p>

                        <p className="font-bold text-white">

                            {decision.decision}

                        </p>

                    </div>

                    <div className="bg-green-600 rounded-lg px-4 py-2">

                        <p className="text-xs text-white">

                            Confidence

                        </p>

                        <p className="font-bold text-white">

                            {(decision.confidence * 100).toFixed(0)}%

                        </p>

                    </div>

                </div>

                <p className="text-slate-300 leading-7">

                    {

                        summary ||

                        "No executive summary available."

                    }

                </p>

            </div>

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">

                <Section
                
                    title="Why This Decision?"
                
                    icon={ChevronRight}
                
                    content={decision.reasoning}
                
                />

                <Section
                
                    title="Supporting Evidence"
                
                    icon={FileSearch}
                
                    content={
                    
                        decision.evidence?.length
                    
                            ? decision.evidence
                                .map(item => `• ${item}`)
                                .join("\n")
                            : ""
                        }
                />

                <Section
                    title="Business Rules"
                    icon={Scale}
                    content={
                        rules.triggered_rules?.length
                            ? rules.triggered_rules
                                .map(rule =>
                                    `• ${rule.name}\n${rule.description}`
                                )
                                .join("\n\n")
                            : ""
                    }
                />

                <Section
                    title="Risk Analysis"
                    icon={ShieldAlert}
                    content={`Overall Risk : ${risk.overall_risk}

                Business Score : ${risk.business_score}

                Risk Score : ${risk.overall_score}

                Compliance Score : ${risk.compliance_score}

                Summary :

                ${risk.summary}`}
                />

                <Section
                    title="Knowledge Graph Contribution"
                    icon={Network}
                    content={`Nodes : ${graph.nodes?.length || 0}

                Relationships : ${graph.edges?.length || 0}

                The knowledge graph helped identify business entities and their relationships.`}
                />


                <Section
                    title="Complete AI Explanation"
                    icon={Brain}
                    content={explanation.explanation}
                />

            </div>

        </div>

    );

}

export default ExplainabilityPanel;