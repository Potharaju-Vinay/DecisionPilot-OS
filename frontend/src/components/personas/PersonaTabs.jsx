import { useState } from "react";

import {
    Briefcase,
    Scale,
    Users,
    Cpu
} from "lucide-react";

const tabs = [

    {
        id: "executive",
        title: "Executive",
        icon: Briefcase
    },

    {
        id: "sales",
        title: "Sales",
        icon: Users
    },

    {
        id: "compliance",
        title: "Compliance",
        icon: Scale
    },

    {
        id: "technical",
        title: "Technical",
        icon: Cpu
    }

];

function PersonaTabs({ data }) {

    const personas = data?.personas || {};

    const [active, setActive] = useState("executive");

    const persona = personas[active] || {};

    console.log("Active Tab:", active);

    console.log("All Personas:", personas);

    console.log("Selected Persona:", persona);

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="mb-6">

                <h2 className="text-2xl font-bold text-white">

                    AI Personas

                </h2>

                <p className="text-slate-400">

                    Personalized insights for different enterprise stakeholders

                </p>

            </div>

            <div className="flex flex-wrap gap-3 mb-6">

                {

                    tabs.map((tab) => {

                        const Icon = tab.icon;

                        const selected = active === tab.id;

                        return (

                            <button

                                key={tab.id}

                                onClick={() => setActive(tab.id)}

                                className={`flex items-center gap-2 px-5 py-3 rounded-xl transition-all duration-300

                                ${selected

                                    ? "bg-cyan-600 text-white"

                                    : "bg-slate-800 text-slate-300 hover:bg-slate-700"

                                }`}

                            >

                                <Icon size={18} />

                                {tab.title}

                            </button>

                        );

                    })

                }

            </div>

            <div className="bg-slate-950 border border-slate-800 rounded-xl p-6">

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                    <div>

                        <h3 className="text-lg font-semibold text-cyan-400 mb-3">

                            Summary

                        </h3>

                        <p className="text-slate-300 leading-7">

                            {

                                persona.summary ||

                                "No summary available."

                            }

                        </p>

                    </div>

                    <div>

                        <h3 className="text-lg font-semibold text-cyan-400 mb-3">

                            Key Insights

                        </h3>

                        {

                            persona.insights?.length ?

                            (

                                <ul className="space-y-2">

                                    {

                                        persona.insights.map(

                                            (item,index)=>(

                                                <li

                                                    key={index}

                                                    className="text-slate-300 flex gap-2"

                                                >

                                                    <span className="text-cyan-400">

                                                        •

                                                    </span>

                                                    <span>

                                                        {item}

                                                    </span>

                                                </li>

                                            )

                                        )

                                    }

                                </ul>

                            )

                            :

                            (

                                <p className="text-slate-500">

                                    No insights available.

                                </p>

                            )

                        }

                    </div>

                </div>

                <div className="mt-6">

                    <h3 className="text-lg font-semibold text-cyan-400 mb-3">

                        Recommended Actions

                    </h3>

                    {

                        persona.actions?.length ?

                        (

                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

                                {

                                    persona.actions.map(

                                        (action,index)=>(

                                            <div

                                                key={index}

                                                className="bg-slate-900 border border-slate-800 rounded-lg p-4"

                                            >

                                                <p className="text-slate-300">

                                                    {action}

                                                </p>

                                            </div>

                                        )

                                    )

                                }

                            </div>

                        )

                        :

                        (

                            <p className="text-slate-500">

                                No actions available.

                            </p>

                        )

                    }

                </div>

            </div>

        </div>

    );

}

export default PersonaTabs;