import {
    Activity,
    Clock3,
    Cpu,
    Database,
    CheckCircle2,
    Brain,
    BarChart3,
    ShieldCheck
} from "lucide-react";

function Metric({

    title,

    value,

    icon,

    color

}) {

    const Icon = icon;

    return (

        <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

            <div className="flex justify-between items-center">

                <div>

                    <p className="text-slate-400 text-sm">

                        {title}

                    </p>

                    <h2 className={`text-3xl font-bold mt-2 ${color}`}>

                        {value}

                    </h2>

                </div>

                <Icon

                    size={28}

                    className={color}

                />

            </div>

        </div>

    );

}

function AnalyticsPanel({

    data

}) {

    const analytics = data?.analytics || {};

    const metrics = data?.metrics || {};

    const completed = data?.completed_agents || [];

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        Enterprise Analytics

                    </h2>

                    <p className="text-slate-400">

                        Performance metrics of the DecisionPilot AI workflow

                    </p>

                </div>

                <BarChart3

                    className="text-cyan-400"

                    size={40}

                />

            </div>

            <div className="grid grid-cols-2 xl:grid-cols-4 gap-5 mb-8">

                <Metric

                    title="Workflow Time"

                    value={`${analytics.workflow_time ?? "--"} s`}

                    color="text-cyan-400"

                    icon={Clock3}

                />

                <Metric

                    title="Agents Executed"

                    value={completed.length}

                    color="text-green-400"

                    icon={Cpu}

                />

                <Metric

                    title="Documents"

                    value={analytics.documents_processed ?? 1}

                    color="text-yellow-400"

                    icon={Database}

                />

                <Metric

                    title="Success Rate"

                    value={`${analytics.success_rate ?? 100}%`}

                    color="text-purple-400"

                    icon={CheckCircle2}

                />

            </div>

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">

                <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

                    <h3 className="text-lg font-semibold text-white mb-4">

                        Agent Execution Time

                    </h3>

                    <div className="space-y-3">

                        {

                            Object.entries(metrics).map(

                                ([agent,time])=>(

                                    <div

                                        key={agent}

                                        className="flex justify-between"

                                    >

                                        <span className="text-slate-300">

                                            {agent}

                                        </span>

                                        <span className="text-cyan-400 font-semibold">

                                            {time}s

                                        </span>

                                    </div>

                                )

                            )

                        }

                    </div>

                </div>

                <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

                    <h3 className="text-lg font-semibold text-white mb-4">

                        AI Workflow Summary

                    </h3>

                    <div className="space-y-4">

                        <div className="flex items-center gap-3">

                            <Brain

                                size={20}

                                className="text-cyan-400"

                            />

                            <span className="text-slate-300">

                                Decision generated successfully

                            </span>

                        </div>

                        <div className="flex items-center gap-3">

                            <ShieldCheck

                                size={20}

                                className="text-green-400"

                            />

                            <span className="text-slate-300">

                                Risk assessment completed

                            </span>

                        </div>

                        <div className="flex items-center gap-3">

                            <Activity

                                size={20}

                                className="text-yellow-400"

                            />

                            <span className="text-slate-300">

                                Customer qualification completed

                            </span>

                        </div>

                        <div className="flex items-center gap-3">

                            <Database

                                size={20}

                                className="text-purple-400"

                            />

                            <span className="text-slate-300">

                                Knowledge graph generated

                            </span>

                        </div>

                    </div>

                </div>

            </div>

            <div className="mt-8 bg-slate-950 border border-slate-800 rounded-xl p-5">

                <h3 className="text-lg font-semibold text-white mb-4">

                    Workflow Logs

                </h3>

                <div className="space-y-2 max-h-72 overflow-y-auto">

                    {

                        data?.logs?.length ?

                        (

                            data.logs.map(

                                (log,index)=>(

                                    <div

                                        key={index}

                                        className="text-sm text-slate-300 border-l-2 border-cyan-500 pl-4 py-2"

                                    >

                                        {log}

                                    </div>

                                )

                            )

                        )

                        :

                        (

                            <p className="text-slate-500">

                                No workflow logs available.

                            </p>

                        )

                    }

                </div>

            </div>

        </div>

    );

}

export default AnalyticsPanel;