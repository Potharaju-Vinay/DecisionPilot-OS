import { Loader2, CheckCircle2 } from "lucide-react";
import { useEffect, useState } from "react";

const agents = [
    "Knowledge Agent",
    "Knowledge Graph",
    "Customer Discovery",
    "ICP Analysis",
    "Risk Assessment",
    "Decision Intelligence",
    "Recommendation",
    "Explainability",
    "Analytics"
];

function LoadingOverlay() {

    const [currentStep, setCurrentStep] = useState(0);

    useEffect(() => {

        const interval = setInterval(() => {

            setCurrentStep((prev) => {

                if (prev < agents.length - 1) {

                    return prev + 1;

                }

                return prev;

            });

        }, 700);

        return () => clearInterval(interval);

    }, []);

    return (

        <div className="fixed inset-0 bg-slate-950/90 backdrop-blur-sm z-50 flex items-center justify-center">

            <div className="bg-slate-900 border border-cyan-700 rounded-2xl p-10 w-[600px]">

                <h1 className="text-3xl font-bold text-white">

                    DecisionPilot AI

                </h1>

                <p className="text-slate-400 mt-2">

                    Analyzing Enterprise Document...

                </p>

                <div className="mt-8 space-y-4">

                    {

                        agents.map((agent, index) => (

                            <div
                                key={agent}
                                className="flex items-center gap-4"
                            >

                                {

                                    index < currentStep

                                    ?

                                    <CheckCircle2

                                        className="text-green-400"

                                        size={20}

                                    />

                                    :

                                    index === currentStep

                                    ?

                                    <Loader2

                                        className="animate-spin text-cyan-400"

                                        size={20}

                                    />

                                    :

                                    <div

                                        className="w-5 h-5 rounded-full bg-slate-700"

                                    />

                                }

                                <span
                                    className={
                                        index <= currentStep

                                        ? "text-white"

                                        : "text-slate-500"
                                    }
                                >

                                    {agent}

                                </span>

                            </div>

                        ))

                    }

                </div>

            </div>

        </div>

    );

}

export default LoadingOverlay;