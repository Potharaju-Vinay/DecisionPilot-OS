import {
    ClipboardCheck,
    User,
    Calendar,
    Flag,
    CheckCircle2
} from "lucide-react";

function ActionCard({

    action

}) {

    return (

        <div className="bg-slate-950 border border-slate-800 rounded-xl p-5 hover:border-cyan-500 transition-all duration-300">

            <div className="flex justify-between items-start">

                <div>

                    <h3 className="text-lg font-semibold text-white">

                        {action.description}

                    </h3>

                    <p className="text-slate-500 text-sm mt-1">

                        {action.id}

                    </p>

                </div>

                <span className="px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400 text-xs">

                    {action.status}

                </span>

            </div>

            <div className="grid grid-cols-2 gap-4 mt-5">

                <div className="flex items-center gap-2">

                    <User

                        size={18}

                        className="text-cyan-400"

                    />

                    <div>

                        <p className="text-xs text-slate-500">

                            Owner

                        </p>

                        <p className="text-sm text-white">

                            {action.owner || "Not Assigned"}

                        </p>

                    </div>

                </div>

                <div className="flex items-center gap-2">

                    <Calendar

                        size={18}

                        className="text-cyan-400"

                    />

                    <div>

                        <p className="text-xs text-slate-500">

                            Due Date

                        </p>

                        <p className="text-sm text-white">

                            {action.due_date || "--"}

                        </p>

                    </div>

                </div>

            </div>

        </div>

    );

}

function RecommendationPanel({

    data

}) {

    const recommendation = data?.recommendation || {};

    const actions = recommendation.actions || [];

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        Recommendation Center

                    </h2>

                    <p className="text-slate-400">

                        AI-generated business recommendations and next actions

                    </p>

                </div>

                <ClipboardCheck

                    size={38}

                    className="text-cyan-400"

                />

            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-5 mb-6">

                <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

                    <div className="flex items-center gap-2">

                        <Flag

                            className="text-yellow-400"

                            size={18}

                        />

                        <span className="text-slate-400">

                            Priority

                        </span>

                    </div>

                    <h2 className="text-3xl font-bold text-yellow-400 mt-3">

                        {recommendation.priority || "--"}

                    </h2>

                </div>

                <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

                    <div className="flex items-center gap-2">

                        <User

                            className="text-cyan-400"

                            size={18}

                        />

                        <span className="text-slate-400">

                            Owner

                        </span>

                    </div>

                    <h2 className="text-xl font-semibold text-white mt-3">

                        {recommendation.owner || "--"}

                    </h2>

                </div>

                <div className="bg-slate-950 border border-slate-800 rounded-xl p-5">

                    <div className="flex items-center gap-2">

                        <Calendar

                            className="text-green-400"

                            size={18}

                        />

                        <span className="text-slate-400">

                            Timeline

                        </span>

                    </div>

                    <h2 className="text-xl font-semibold text-green-400 mt-3">

                        {recommendation.timeline || "--"}

                    </h2>

                </div>

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6 mb-6">

                <div className="flex items-center gap-2 mb-3">

                    <CheckCircle2

                        className="text-cyan-400"

                        size={20}

                    />

                    <h3 className="text-lg font-semibold text-white">

                        Executive Summary

                    </h3>

                </div>

                <p className="text-slate-300 leading-7">

                    {

                        recommendation.summary ||

                        "No recommendation summary available."

                    }

                </p>

            </div>

            <div>

                <h3 className="text-xl font-semibold text-white mb-5">

                    Recommended Action Plan

                </h3>

                <div className="grid grid-cols-1 xl:grid-cols-2 gap-5">

                    {

                        actions.length > 0 ?

                        (

                            actions.map((action)=>(

                                <ActionCard

                                    key={action.id}

                                    action={action}

                                />

                            ))

                        )

                        :

                        (

                            <p className="text-slate-500">

                                No recommended actions.

                            </p>

                        )

                    }

                </div>

            </div>

        </div>

    );

}

export default RecommendationPanel;