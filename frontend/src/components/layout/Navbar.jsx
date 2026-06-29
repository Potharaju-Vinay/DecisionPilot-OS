import { useEffect, useState } from "react";
import {

    Bell,

    Upload,

    Play,

    Cpu,

    CalendarDays,

    UserCircle2

} from "lucide-react";

function Navbar({

    selectedFile,

    setSelectedFile,

    onAnalyze,

    loadingAnalysis

}) {
    const [time, setTime] = useState("");

    const handleFileChange = (event) => {

        const file = event.target.files[0];

            if (file) {

                setSelectedFile(file);

            }

    };

    useEffect(() => {

        const updateTime = () => {

            const now = new Date();

            setTime(

                now.toLocaleString()

            );

        };

        updateTime();

        const interval = setInterval(

            updateTime,

            1000

        );

        return () => clearInterval(interval);

    }, []);

    return (

        <header className="h-20 bg-slate-900 border-b border-slate-800 px-8 flex items-center justify-between">

            <div>

                <h1 className="text-2xl font-bold text-white">

                    DecisionPilot OS

                </h1>

                <div className="flex items-center gap-2 mt-1">

                    <CalendarDays

                        size={16}

                        className="text-slate-400"

                    />

                    <span className="text-sm text-slate-400">

                        {time}

                    </span>

                </div>

            </div>

            <div className="flex items-center gap-5">

                <div className="flex items-center gap-2 bg-green-900/30 border border-green-700 px-4 py-2 rounded-xl">

                    <Cpu

                        size={18}

                        className="text-green-400"

                    />

                    <span className="text-green-400 text-sm font-medium">

                        AI Workflow Online

                    </span>

                </div>

                <button className="relative p-3 rounded-xl bg-slate-800 hover:bg-slate-700 transition">

                    <Bell

                        size={20}

                        className="text-white"

                    />

                    <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">

                        3

                    </span>

                </button>

                <label className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 px-4 py-3 rounded-xl transition cursor-pointer">

                    <Upload size={18} />

                    <span>

                        {

                            selectedFile

                            ? selectedFile.name

                            : "Upload Document"

                        }

                    </span>

                    <input

                        type="file"

                        className="hidden"

                        accept=".pdf,.doc,.docx,.ppt,.pptx"

                        onChange={handleFileChange}

                    />

                </label>

                <button

                    onClick={onAnalyze}

                    disabled={loadingAnalysis}

                    className="flex items-center gap-2 bg-cyan-600 hover:bg-cyan-500 disabled:bg-slate-700 px-5 py-3 rounded-xl font-semibold transition"

                >

                    <Play size={18} />

                    <span>

                        {

                            loadingAnalysis

                            ? "Running..."

                            : "Run Analysis"

                        }

                    </span>

                </button>


                <div className="flex items-center gap-3">

                    <UserCircle2

                        size={38}

                        className="text-cyan-400"

                    />

                    <div>

                        <p className="text-white font-semibold">

                            Enterprise User

                        </p>

                        <p className="text-slate-400 text-sm">

                            Decision Analyst

                        </p>

                    </div>

                </div>

            </div>

        </header>

    );

}

export default Navbar;