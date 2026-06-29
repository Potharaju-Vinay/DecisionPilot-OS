import {
    ShieldAlert,
    ShieldCheck,
    CircleDollarSign,
    Scale,
    CheckCircle2,
    AlertTriangle
} from "lucide-react";

function ScoreCard({

    title,

    value,

    color,

    icon

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

function RiskGauge({

    data

}) {

    const risk = data?.risk || {};

    console.log("Risk Object");
    console.log(risk);

    const rules = data?.rule_result?.triggered_rules || [];

    const audit = data?.rule_result?.audit_trail || [];

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        Enterprise Risk Assessment

                    </h2>

                    <p className="text-slate-400">

                        AI-powered business risk evaluation

                    </p>

                </div>

                <div className="text-right">

                    <p className="text-slate-400">

                        Overall Risk

                    </p>

                    <h1 className="text-4xl font-bold text-red-400">

                        {risk.overall_risk ?? "Unknown"}

                    </h1>

                </div>

            </div>

            <div className="grid grid-cols-2 gap-4">

                <ScoreCard

                    title="Business Score"

                    value={risk.business_score ?? 0}

                    color="text-green-400"

                    icon={CircleDollarSign}

                />

                <ScoreCard

                    title="Risk Score"

                    value={risk.overall_score ?? 0}

                    color="text-red-400"

                    icon={ShieldAlert}

                />

                <ScoreCard

                    title="Compliance Score"

                    value={risk.compliance_score ?? 0}

                    color="text-cyan-400"

                    icon={Scale}

                />

                <ScoreCard

                    title="Approval Score"

                    value={risk.approval_score ?? 0}

                    color="text-yellow-400"

                    icon={CheckCircle2}

                />

            </div>

            <div className="mt-8">

                <h3 className="text-xl font-semibold text-white mb-4">

                    Triggered Business Rules

                </h3>

                <div className="space-y-3">

                    {

                        rules.length > 0 ?

                        rules.map((rule) => (

                            <div

                                key={rule.id}

                                className="bg-slate-950 border border-slate-800 rounded-xl p-4"

                            >

                                <div className="flex justify-between">

                                    <div>

                                        <h4 className="text-white font-semibold">

                                            {rule.name}

                                        </h4>

                                        <p className="text-slate-400 text-sm mt-1">

                                            {rule.description}

                                        </p>

                                    </div>

                                    <span className="text-cyan-400 font-bold">

                                        {rule.score}

                                    </span>

                                </div>

                            </div>

                        ))

                        :

                        (

                            <p className="text-slate-500">

                                No business rules triggered.

                            </p>

                        )

                    }

                </div>

            </div>

            <div className="mt-8">

                <h3 className="text-xl font-semibold text-white mb-4">

                    Audit Trail

                </h3>

                <div className="space-y-3">

                    {

                        audit.length > 0 ?

                        audit.map((item,index)=>(

                            <div

                                key={index}

                                className="flex gap-3 bg-slate-950 border border-slate-800 rounded-xl p-4"

                            >

                                <AlertTriangle

                                    className="text-yellow-400 mt-1"

                                    size={18}

                                />

                                <div>

                                    <p className="text-white">

                                        {item.rule_name}

                                    </p>

                                    <p className="text-slate-400 text-sm">

                                        {item.reason}

                                    </p>

                                </div>

                            </div>

                        ))

                        :

                        (

                            <p className="text-slate-500">

                                No audit records available.

                            </p>

                        )

                    }

                </div>

            </div>

        </div>

    );

}

export default RiskGauge;