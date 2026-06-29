import { useEffect, useState } from "react";

import { getDashboard } from "../services/dashboardService";

import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

import ExecutiveCards from "../components/dashboard/ExecutiveCards";
import AgentPipeline from "../components/workflow/AgentPipeline";
import CustomerDiscoveryCard from "../components/customer/CustomerDiscoveryCard";
import ICPCard from "../components/icp/ICPCard";
import RiskGauge from "../components/risk/RiskGauge";
import DecisionCard from "../components/decision/DecisionCard";
import RecommendationPanel from "../components/recommendation/RecommendationPanel";
import ExplainabilityPanel from "../components/explainability/ExplainabilityPanel";
import KnowledgeGraph from "../components/graph/KnowledgeGraph";
import AnalyticsPanel from "../components/analytics/AnalyticsPanel";
import PersonaTabs from "../components/personas/PersonaTabs";
import { analyzeDocument } from "../services/analysisService";
import LoadingOverlay from "../components/common/LoadingOverlay";
import toast from "react-hot-toast";
import FadeIn from "../components/common/FadeIn";

function Dashboard() {

    const [data, setData] = useState(null);

    const [selectedFile, setSelectedFile] = useState(null);

    const [loadingAnalysis, setLoadingAnalysis] = useState(false);

    useEffect(() => {

        loadDashboard();

    }, []);

    async function loadDashboard() {

        try {

            const dashboard = await getDashboard();

            console.log("Dashboard API Response:");
            console.log(dashboard);
            console.log("PERSONAS");

            console.log(data?.personas);

            setData(dashboard);

        }

        catch (err) {

            console.error(err);

        }

    }

    async function runAnalysis() {

        if (!selectedFile) {

            toast.error(
                "Please upload a document first."
            );

            return;

        }

        try {

            setLoadingAnalysis(true);

            await analyzeDocument(selectedFile);

            await loadDashboard();

            toast.success(
                "Enterprise Intelligence Generated Successfully!",
                {
                    duration: 3000,
                    style: {
                        background: "#0f172a",
                        color: "#fff",
                        border: "1px solid #06b6d4"
                    }
                }
            );
            

        }

        catch (error) {

            console.error(error);

            toast.error(
                "Analysis failed."
            );

        }

        finally {

            setLoadingAnalysis(false);

        }

    }

    if (!data) {

        return <LoadingOverlay />;

    }

    return (
        
        <>

            {loadingAnalysis && <LoadingOverlay />}

            <div className="flex bg-slate-950 min-h-screen">

                <Sidebar />

            <div className="flex-1 flex flex-col">

                <Navbar
                    selectedFile={selectedFile}
                    setSelectedFile={setSelectedFile}
                    onAnalyze={runAnalysis}
                    loadingAnalysis={loadingAnalysis}
                />

                <div className="p-8">
                    
                    <h1 className="text-white text-5xl mb-8">
                        
                        Dashboard

                    </h1>

                    <FadeIn delay={0}>

                        <section id="dashboard">

                            <ExecutiveCards data={data}/>

                        </section>

                    </FadeIn>

                    <div className="mt-8">

                        <AgentPipeline data={data} />

                    </div>

                    <FadeIn delay={0.1}>

                    <section
                        id="customer-discovery"
                        className="mt-8"
                    >

                        <CustomerDiscoveryCard data={data}/>

                    </section>

                    </FadeIn>


                    <FadeIn delay={0.2}>

                    <section
                        id="icp"
                        className="mt-8"
                    >

                        <ICPCard data={data}/>

                    </section>

                    </FadeIn>

                    <FadeIn delay={0.3}>

                    <section
                        id="risk"
                        className="mt-8"
                    >

                        <RiskGauge data={data}/>
 
                    </section>

                    </FadeIn>

                    <FadeIn delay={0.4}>

                    <section
                        id="decision"
                        className="mt-8"
                    >

                        <DecisionCard data={data}/>

                    </section>

                    </FadeIn>

                    <FadeIn delay={0.5}>

                    <section
                        id="recommendation"
                        className="mt-8"
                    >

                        <RecommendationPanel data={data}/>

                    </section>

                    </FadeIn>

                    <FadeIn delay={0.6}>

                    <section
                        id="explainability"
                        className="mt-8"
                    >

                        <ExplainabilityPanel data={data}/>

                    </section>

                    </FadeIn>

                    <FadeIn delay={0.7}>

                    <section
                    
                        id="knowledge-graph"
                        className="mt-8"
                    >

                        <KnowledgeGraph
                            data={data}
                        />

                    </section>

                    </FadeIn>


                    <FadeIn delay={0.8}>

                    <section
                        id="analytics"
                        className="mt-8"
                    >

                        <AnalyticsPanel data={data}/>

                    </section>

                    </FadeIn>

                    <FadeIn delay={0.9}>

                    <section
                        id="personas"
                        className="mt-8"
                    >

                        <PersonaTabs data={data}/>

                    </section>

                    </FadeIn>


                </div>
            </div>

        </div>
        </>
    
    );


}

export default Dashboard;