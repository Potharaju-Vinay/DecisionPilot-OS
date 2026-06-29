import {
    TrendingUp,
    ShieldCheck,
    Brain,
    Target,
    Activity,
    Clock3
} from "lucide-react";

function MetricCard({

    title,

    value,

    subtitle,

    icon,

    color

}) {

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg hover:border-cyan-500 transition-all duration-300">

            <div className="flex justify-between items-start">

                <div>

                    <p className="text-slate-400 text-sm">

                        {title}

                    </p>

                    <h2 className={`text-3xl font-bold mt-2 ${color}`}>

                        {value}

                    </h2>

                    <p className="text-slate-500 text-sm mt-2">

                        {subtitle}

                    </p>

                </div>

                <div className="bg-slate-800 rounded-xl p-3">

                    {icon}

                </div>

            </div>

        </div>

    );

}

function ExecutiveCards({ data }) {

    return (

        <div>

            <div className="flex justify-between items-center mb-5">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        Executive Overview

                    </h2>

                    <p className="text-slate-400">

                        AI-powered enterprise decision intelligence summary

                    </p>

                </div>

            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                <MetricCard

                    title="Opportunity Score"

                    value={`${data.customer_discovery?.opportunity_score ?? 0}%`}

                    subtitle="Customer qualification"

                    color="text-green-400"

                    icon={

                        <TrendingUp

                            size={28}

                            className="text-green-400"

                        />

                    }

                />

                <MetricCard

                    title="ICP Score"

                    value={`${data.icp?.score ?? 0}%`}

                    subtitle="Ideal customer match"

                    color="text-cyan-400"

                    icon={

                        <Target

                            size={28}

                            className="text-cyan-400"

                        />

                    }

                />

                <MetricCard

                    title="Risk Level"

                    value={data.risk?.overall_risk ?? "Unknown"}

                    subtitle="Enterprise risk assessment"

                    color="text-red-400"

                    icon={

                        <ShieldCheck

                            size={28}

                            className="text-red-400"

                        />

                    }

                />

                <MetricCard

                    title="AI Decision"

                    value={data.decision?.decision ?? "--"}

                    subtitle="Decision Intelligence"

                    color="text-purple-400"

                    icon={

                        <Brain

                            size={28}

                            className="text-purple-400"

                        />

                    }

                />

                <MetricCard

                    title="Confidence"

                    value={`${Math.round((data.decision?.confidence ?? 0) * 100)}%`}

                    subtitle="AI confidence"

                    color="text-yellow-400"

                    icon={

                        <Activity

                            size={28}

                            className="text-yellow-400"

                        />

                    }

                />

                <MetricCard

                    title="Workflow Time"

                    value={`${data.analytics?.workflow_time ?? "--"} s`}

                    subtitle="Total processing time"

                    color="text-blue-400"

                    icon={

                        <Clock3

                            size={28}

                            className="text-blue-400"

                        />

                    }

                />

            </div>

        </div>

    );

}

export default ExecutiveCards;