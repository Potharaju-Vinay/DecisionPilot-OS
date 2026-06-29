import {
    Handle,
    Position
} from "reactflow";

import {
    Building2,
    User,
    ShieldAlert,
    Target,
    CheckCircle2,
    Calendar,
    DollarSign,
    BrainCircuit,
    Sparkles,
    Flag
} from "lucide-react";

function CustomNode({ data }) {

    const config = {

        default: {
            color: "bg-slate-600",
            icon: BrainCircuit,
            width: "min-w-[180px]"
        },

        company: {
            color: "bg-blue-600",
            icon: Building2,
            width: "min-w-[210px]"
        },

        person: {
            color: "bg-green-600",
            icon: User,
            width: "min-w-[180px]"
        },

        industry: {
            color: "bg-purple-600",
            icon: Building2,
            width: "min-w-[170px]"
        },

        budget: {
            color: "bg-yellow-500",
            icon: DollarSign,
            width: "min-w-[190px]"
        },

        timeline: {
            color: "bg-orange-500",
            icon: Calendar,
            width: "min-w-[170px]"
        },

        goal: {
            color: "bg-pink-600",
            icon: Target,
            width: "min-w-[180px]"
        },

        signal: {
            color: "bg-cyan-600",
            icon: Sparkles,
            width: "min-w-[190px]"
        },

        risk: {
            color: "bg-red-600",
            icon: ShieldAlert,
            width: "min-w-[180px]"
        },

        decision: {
            color: "bg-emerald-600",
            icon: CheckCircle2,
            width: "min-w-[200px]"
        },

        action: {
            color: "bg-indigo-600",
            icon: Flag,
            width: "min-w-[190px]"
        }

    };

    const node = config[data.type] || {

        color: "bg-slate-600",

        icon: BrainCircuit,

        width: "min-w-[180px]"

    };

    const Icon = node.icon;

    return (

        <div className="relative">

            <Handle
                type="target"
                position={Position.Top}
            />

            <div
                className={`${node.color} ${node.width}
                rounded-2xl shadow-xl border border-white/20
                px-5 py-4 hover:scale-105
                transition-all duration-300`}
            >

                <div className="flex items-center gap-3">

                    <Icon
                        size={22}
                        className="text-white"
                    />

                    <div>

                        <div className="text-white font-bold">

                            {data.label}

                        </div>

                        <div className="text-white/70 text-xs uppercase">

                            {data.type}

                        </div>

                    </div>

                </div>

            </div>

            <Handle
                type="source"
                position={Position.Bottom}
            />

        </div>

    );

}

export default CustomNode;