import {
    Target,
    BadgeCheck,
    BadgeX,
    Building2,
    CircleDollarSign,
    Users,
    BriefcaseBusiness
} from "lucide-react";

function MatchCard({

    title,

    value

}) {

    return (

        <div className="bg-slate-950 border border-slate-800 rounded-xl p-4">

            <p className="text-slate-400 text-sm">

                {title}

            </p>

            <p className="text-white font-semibold mt-2">

                {value}

            </p>

        </div>

    );

}

function ProgressBar({

    score

}) {

    return (

        <div>

            <div className="flex justify-between mb-2">

                <span className="text-slate-400">

                    Qualification Score

                </span>

                <span className="text-cyan-400 font-semibold">

                    {score}%

                </span>

            </div>

            <div className="w-full h-3 rounded-full bg-slate-800 overflow-hidden">

                <div

                    className="h-full bg-cyan-500 transition-all duration-700"

                    style={{

                        width: `${score}%`

                    }}

                />

            </div>

        </div>

    );

}

function ICPCard({

    data

}) {

    const icp = data?.icp || {};

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        ICP Qualification

                    </h2>

                    <p className="text-slate-400">

                        Ideal Customer Profile Analysis

                    </p>

                </div>

                <div className="text-right">

                    <h1 className="text-5xl font-bold text-cyan-400">

                        {icp.score ?? 0}%

                    </h1>

                </div>

            </div>

            <ProgressBar

                score={icp.score ?? 0}

            />

            <div className="mt-6">

                {

                    icp.qualified ?

                    (

                        <div className="flex items-center gap-3 bg-green-950 border border-green-700 rounded-xl p-4">

                            <BadgeCheck

                                className="text-green-400"

                            />

                            <div>

                                <p className="font-semibold text-green-400">

                                    Qualified Opportunity

                                </p>

                                <p className="text-green-200 text-sm">

                                    Customer matches the target ICP.

                                </p>

                            </div>

                        </div>

                    )

                    :

                    (

                        <div className="flex items-center gap-3 bg-red-950 border border-red-700 rounded-xl p-4">

                            <BadgeX

                                className="text-red-400"

                            />

                            <div>

                                <p className="font-semibold text-red-400">

                                    Not Qualified

                                </p>

                                <p className="text-red-200 text-sm">

                                    Customer does not fully satisfy ICP.

                                </p>

                            </div>

                        </div>

                    )

                }

            </div>

            <div className="grid grid-cols-2 gap-4 mt-6">

                <MatchCard

                    title="Industry"

                    value={icp.industry ?? "Unknown"}

                />

                <MatchCard

                    title="Company Size"

                    value={icp.company_size ?? "Unknown"}

                />

                <MatchCard

                    title="Budget"

                    value={icp.budget ?? "Unknown"}

                />

                <MatchCard

                    title="Decision Maker"

                    value={

                        icp.decision_maker ??

                        "Unknown"

                    }

                />

            </div>

            <div className="mt-6 bg-slate-950 border border-slate-800 rounded-xl p-5">

                <div className="flex items-center gap-2 mb-3">

                    <Target

                        className="text-cyan-400"

                    />

                    <h3 className="font-semibold text-white">

                        Qualification Summary

                    </h3>

                </div>

                <p className="text-slate-300 leading-7">

                    {

                        icp.reasoning ??

                        "No qualification reasoning available."

                    }

                </p>

            </div>

        </div>

    );

}

export default ICPCard;