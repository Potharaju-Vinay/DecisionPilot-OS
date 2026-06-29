import { useState } from "react";
import {
    LayoutDashboard,
    Users,
    Network,
    Shield,
    Brain,
    BarChart3,
    UserSquare2,
    Settings,
    Cpu
} from "lucide-react";

const menu = [

    {
        title: "Dashboard",
        icon: LayoutDashboard,
        target: "dashboard"
    },

    {
        title: "Customer Discovery",
        icon: Users,
        target: "customer-discovery"
    },

    {
        title: "Knowledge Graph",
        icon: Network,
        target: "knowledge-graph"
    },

    {
        title: "Risk Assessment",
        icon: Shield,
        target: "risk"
    },

    {
        title: "Decision Intelligence",
        icon: Brain,
        target: "decision"
    },

    {
        title: "Analytics",
        icon: BarChart3,
        target: "analytics"
    },

    {
        title: "Personas",
        icon: UserSquare2,
        target: "personas"
    },

    {
        title: "Settings",
        icon: Settings,
        target: "settings"
    }

];

function Sidebar() {

    const [activeMenu, setActiveMenu] = useState("dashboard");

    function scrollToSection(id) {

        const section = document.getElementById(id);

        if (section) {

            section.scrollIntoView({
 
                behavior: "smooth",

                block: "start"

            });

        }

    }

    return (

        <aside className="w-72 bg-slate-900 border-r border-slate-800 flex flex-col">

            <div className="p-6 border-b border-slate-800">

                <div className="flex items-center gap-3">

                    <div className="bg-cyan-600 rounded-xl p-3">

                        <Cpu

                            size={26}

                            className="text-white"

                        />

                    </div>

                    <div>

                        <h1 className="text-white text-xl font-bold">

                            DecisionPilot

                        </h1>

                        <p className="text-slate-400 text-sm">

                            Enterprise AI OS

                        </p>

                    </div>

                </div>

            </div>

            <div className="flex-1 px-4 py-6">

                <p className="text-slate-500 text-xs uppercase mb-4">

                    Navigation

                </p>

                <div className="space-y-2">

                    {

                        menu.map((item, index) => {

                            const Icon = item.icon;

                            const active = activeMenu === item.target;

                            return (

                                <button
                                    key={item.title}
                                    onClick={() => {

                                        setActiveMenu(item.target);

                                        scrollToSection(item.target);

                                    }}
                                    
                                    className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300

                                    ${active

                                        ? "bg-cyan-600 text-white"

                                        : "text-slate-300 hover:bg-slate-800"

                                    }`}
                                >

                                    <Icon size={20} />

                                    <span>

                                        {item.title}

                                    </span>

                                </button>

                            );

                        })

                    }

                </div>

            </div>

            <div className="p-5 border-t border-slate-800">

                <div className="bg-slate-800 rounded-xl p-4">

                    <p className="text-slate-400 text-sm">

                        System Status

                    </p>

                    <div className="flex items-center gap-2 mt-3">

                        <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>

                        <span className="text-green-400 text-sm">

                            All AI Agents Online

                        </span>

                    </div>

                </div>

                <div className="mt-5 text-center">

                    <p className="text-slate-500 text-xs">

                        DecisionPilot OS

                    </p>

                    <p className="text-slate-600 text-xs">

                        Version 1.0
                    </p>

                </div>

            </div>

        </aside>

    );

}

export default Sidebar;