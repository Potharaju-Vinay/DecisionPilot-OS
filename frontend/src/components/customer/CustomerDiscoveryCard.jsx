import {
    Building2,
    Target,
    TrendingUp,
    CircleDollarSign,
    Users,
    CalendarClock,
    TriangleAlert,
    BriefcaseBusiness
} from "lucide-react";

function Section({ title, items, icon }) {

    const Icon = icon;

    return (

        <div className="bg-slate-950 rounded-xl p-4 border border-slate-800">

            <div className="flex items-center gap-2 mb-3">

                <Icon
                    size={18}
                    className="text-cyan-400"
                />

                <h3 className="text-white font-semibold">

                    {title}

                </h3>

            </div>

            {items && items.length > 0 ? (

                <ul className="space-y-2">

                    {items.map((item, index) => (

                        <li
                            key={index}
                            className="text-slate-300 text-sm flex gap-2"
                        >

                            <span className="text-cyan-400">•</span>

                            <span>{item}</span>

                        </li>

                    ))}

                </ul>

            ) : (

                <p className="text-slate-500 text-sm">

                    No information available

                </p>

            )}

        </div>

    );

}

function CustomerDiscoveryCard({ data }) {

    const customer = data?.customer_discovery || {};

    return (

        <div className="bg-slate-900 rounded-2xl border border-slate-800 p-6">

            <div className="flex justify-between items-center mb-6">

                <div>

                    <h2 className="text-2xl font-bold text-white">

                        Customer Discovery

                    </h2>

                    <p className="text-slate-400">

                        AI-generated customer intelligence

                    </p>

                </div>

                <div className="bg-cyan-950 px-4 py-3 rounded-xl">

                    <p className="text-xs text-slate-400">

                        Opportunity Score

                    </p>

                    <h2 className="text-3xl font-bold text-cyan-400">

                        {customer.opportunity_score ?? 0}%

                    </h2>

                </div>

            </div>

            <div className="grid grid-cols-2 xl:grid-cols-4 gap-4 mb-6">

                <div className="bg-slate-950 rounded-xl p-4 border border-slate-800">

                    <div className="flex items-center gap-2 mb-2">

                        <Building2
                            size={18}
                            className="text-cyan-400"
                        />

                        <span className="text-slate-400 text-sm">

                            Company

                        </span>

                    </div>

                    <p className="text-white font-semibold">

                        {customer.company || "Unknown"}

                    </p>

                </div>

                <div className="bg-slate-950 rounded-xl p-4 border border-slate-800">

                    <div className="flex items-center gap-2 mb-2">

                        <BriefcaseBusiness
                            size={18}
                            className="text-cyan-400"
                        />

                        <span className="text-slate-400 text-sm">

                            Industry

                        </span>

                    </div>

                    <p className="text-white font-semibold">

                        {customer.industry || "Unknown"}

                    </p>

                </div>

                <div className="bg-slate-950 rounded-xl p-4 border border-slate-800">

                    <div className="flex items-center gap-2 mb-2">

                        <CircleDollarSign
                            size={18}
                            className="text-cyan-400"
                        />

                        <span className="text-slate-400 text-sm">

                            Budget

                        </span>

                    </div>

                    <p className="text-white font-semibold">

                        {customer.budget || "Unknown"}

                    </p>

                </div>

                <div className="bg-slate-950 rounded-xl p-4 border border-slate-800">

                    <div className="flex items-center gap-2 mb-2">

                        <CalendarClock
                            size={18}
                            className="text-cyan-400"
                        />

                        <span className="text-slate-400 text-sm">

                            Timeline

                        </span>

                    </div>

                    <p className="text-white font-semibold">

                        {customer.timeline || "Unknown"}

                    </p>

                </div>

            </div>

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-5">

                <Section

                    title="Business Goals"

                    items={customer.business_goals}

                    icon={Target}

                />

                <Section

                    title="Pain Points"

                    items={customer.pain_points}

                    icon={TriangleAlert}

                />

                <Section

                    title="Buying Signals"

                    items={customer.buying_signals}

                    icon={TrendingUp}

                />

                <Section

                    title="Decision Makers"

                    items={customer.decision_makers}

                    icon={Users}

                />

            </div>

        </div>

    );

}

export default CustomerDiscoveryCard;