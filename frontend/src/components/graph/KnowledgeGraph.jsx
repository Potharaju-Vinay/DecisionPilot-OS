import "reactflow/dist/style.css";
import { useState } from "react";
import {
    ReactFlow,
    Background,
    Controls,
    MiniMap,
    MarkerType
} from "reactflow";

import dagre from "dagre";

import CustomNode from "./CustomNode";

const nodeTypes = {
    default: CustomNode
};

const dagreGraph = new dagre.graphlib.Graph();

dagreGraph.setDefaultEdgeLabel(() => ({}));

const nodeWidth = 250;
const nodeHeight = 90;

function getLayoutedElements(nodes, edges) {

    dagreGraph.setGraph({
        rankdir: "TB",
        ranksep: 70,
        nodesep: 35,
        marginx: 20,
        marginy: 20
    });

    nodes.forEach((node) => {

        dagreGraph.setNode(node.id, {

            width: nodeWidth,

            height: nodeHeight

        });

    });

    edges.forEach((edge) => {

        dagreGraph.setEdge(

            edge.source,

            edge.target

        );

    });

    dagre.layout(dagreGraph);

    nodes.forEach((node) => {

        const pos = dagreGraph.node(node.id);

        node.position = {

            x: pos.x,

            y: pos.y

        };

    });

    return {

        nodes,

        edges

    };

}

function getTitle(type) {

    switch (type) {

        case "company":
            return "🏢 Company Intelligence";

        case "goal":
            return "🎯 Business Goal";

        case "signal":
            return "✨ Buying Signal";

        case "risk":
            return "⚠ Risk Intelligence";

        case "decision":
            return "🤖 AI Decision";

        case "action":
            return "🚀 Recommendation";

        case "budget":
            return "💰 Budget Information";

        case "timeline":
            return "📅 Implementation Timeline";

        case "person":
            return "👤 Decision Maker";

        case "industry":
            return "🏭 Industry Information";

        default:
            return "📌 Entity Information";

    }

}

function renderNodeDetails(selectedNode, data) {

    const type = selectedNode?.data?.type;

    const label = selectedNode?.data?.label;

    switch (type) {

        case "company":

            return (

                <div className="grid grid-cols-2 gap-6">

                    <div>

                        <p className="text-slate-400">Company</p>

                        <h3 className="text-white font-semibold">

                            {data?.customer_discovery?.company}

                        </h3>

                    </div>

                    <div>

                        <p className="text-slate-400">Industry</p>

                        <h3 className="text-cyan-400">

                            {data?.customer_discovery?.industry}

                        </h3>

                    </div>

                    <div>

                        <p className="text-slate-400">Budget</p>

                        <h3 className="text-green-400">

                            {data?.customer_discovery?.budget}

                        </h3>

                    </div>

                    <div>

                        <p className="text-slate-400">Timeline</p>

                        <h3 className="text-orange-400">

                            {data?.customer_discovery?.timeline}

                        </h3>

                    </div>

                </div>

            );

        case "goal":

            return (

                <div className="space-y-5">

                    <div>

                        <p className="text-slate-400">

                            Business Goal

                        </p>

                        <h3 className="text-2xl font-bold text-pink-400">

                            {label}

                        </h3>

                    </div>

                    <div className="grid grid-cols-2 gap-4">

                        <div className="bg-slate-900 rounded-xl p-4">

                            <p className="text-slate-500 text-sm">

                                Priority

                            </p>

                            <p className="text-green-400 font-semibold">

                                High

                            </p>

                        </div>

                        <div className="bg-slate-900 rounded-xl p-4">

                            <p className="text-slate-500 text-sm">

                                Business Area

                            </p>

                            <p className="text-cyan-400 font-semibold">

                                Enterprise Strategy

                            </p>

                        </div>

                    </div>

                    <div>

                        <p className="text-slate-500">

                            Business Impact

                        </p>

                        <p className="text-slate-300">

                            This goal contributes to enterprise growth, AI adoption,
                            operational efficiency and executive decision quality.

                        </p>

                    </div>

                </div>

            );

        case "signal":

    return (

        <div className="space-y-5">

            <div>

                <p className="text-slate-400">

                    Buying Signal

                </p>

                <h3 className="text-2xl font-bold text-cyan-400">

                    {label}

                </h3>

            </div>

            <div className="grid grid-cols-2 gap-4">

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Sales Stage

                    </p>

                    <p className="text-green-400">

                        Technical Evaluation

                    </p>

                </div>

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Confidence

                    </p>

                    <p className="text-cyan-400">

                        High

                    </p>

                </div>

            </div>

            <p className="text-slate-300">

                This buying signal indicates active customer engagement and
                movement toward enterprise adoption.

            </p>

        </div>

    );

        case "risk":

    return (

        <div className="space-y-5">

            <h3 className="text-2xl font-bold text-red-400">

                {data?.risk?.overall_risk}

            </h3>

            <div className="grid grid-cols-3 gap-4">

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Business

                    </p>

                    <p className="text-red-300">

                        {data?.risk?.business_risk}

                    </p>

                </div>

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Financial

                    </p>

                    <p className="text-red-300">

                        {data?.risk?.financial_risk}

                    </p>

                </div>

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Operational

                    </p>

                    <p className="text-red-300">

                        {data?.risk?.operational_risk}

                    </p>

                </div>

            </div>

        </div>

    );

        case "decision":

    return (

        <div className="space-y-5">

            <h3 className="text-2xl font-bold text-emerald-400">

                {data?.decision?.decision}

            </h3>

            <div className="grid grid-cols-2 gap-4">

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Confidence

                    </p>

                    <p className="text-green-400">

                        {Math.round((data?.decision?.confidence || 0)*100)}%

                    </p>

                </div>

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Opportunity

                    </p>

                    <p className="text-cyan-400">

                        {data?.customer_discovery?.opportunity_score}%

                    </p>

                </div>

            </div>

        </div>

    );

        case "action":

    return (

        <div className="space-y-5">

            <h3 className="text-2xl font-bold text-indigo-400">

                Recommended Action

            </h3>

            <div className="bg-slate-900 rounded-xl p-5">

                <p className="text-white">

                    {data?.recommendation?.summary || label}

                </p>

            </div>

            <div className="grid grid-cols-2 gap-4">

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Priority

                    </p>

                    <p className="text-green-400">

                        High

                    </p>

                </div>

                <div className="bg-slate-900 rounded-xl p-4">

                    <p className="text-slate-500">

                        Expected Outcome

                    </p>

                    <p className="text-cyan-400">

                        Faster Deployment

                    </p>

                </div>

            </div>

        </div>

    );

        case "budget":

    return (

        <div className="space-y-5">

            <h3 className="text-2xl text-yellow-400 font-bold">

                {label}

            </h3>

            <div className="grid grid-cols-2 gap-4">

                <div className="bg-slate-900 p-4 rounded-xl">

                    <p className="text-slate-500">

                        Status

                    </p>

                    <p className="text-green-400">

                        Approved

                    </p>

                </div>

                <div className="bg-slate-900 p-4 rounded-xl">

                    <p className="text-slate-500">

                        ROI

                    </p>

                    <p className="text-cyan-400">

                        High

                    </p>

                </div>

            </div>

        </div>

    );

        case "timeline":

    return (

        <div className="space-y-5">

            <h3 className="text-2xl font-bold text-orange-400">

                Implementation Timeline

            </h3>

            <div className="bg-slate-900 rounded-xl p-5">

                <p className="text-white whitespace-pre-line">

                    {label?.replace(/,/g, "\n") || "No timeline available"}

                </p>

            </div>

        </div>

    );

        default:

            return (

                <div>

                    <h3 className="text-xl text-white">

                        {label}

                    </h3>

                </div>

            );

    }

}

function KnowledgeGraph({ data }) {



    const [selectedNode, setSelectedNode] = useState(null);

    const graph = data?.knowledge_graph || {};

    const nodes = (graph.nodes || []).map((node, index) => ({

        id: node.id,

        type: "default",

        position: {

            x: 0,

            y: 0

        },

        data: {

            label: node.value,

            type: node.type.toLowerCase()

        }

    }));

const edges = (graph.edges || []).map((edge, index) => ({

    id: edge.id || `e${index}`,

    source: edge.source,

    target: edge.target,

    label:
        edge.relation === "Business Goal" ||
        edge.relation === "Buying Signal"
            ? ""
            : edge.relation,

    animated: true

}));

const layout = getLayoutedElements(

    [...nodes],

    [...edges]

);


    console.log("Selected Node:", selectedNode);

    

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

            <div className="mb-6">

                <h2 className="text-2xl font-bold text-white">

                    Enterprise Knowledge Graph

                </h2>

                <p className="text-slate-400">

                    AI-generated relationship graph extracted from the uploaded documents

                </p>

                <div className="flex flex-wrap gap-3 mt-5">
                    
                    <span className="px-3 py-1 rounded-full bg-blue-600 text-white text-sm">
                        Company
                    </span>

                    <span className="px-3 py-1 rounded-full bg-green-600 text-white text-sm">
                        Person
                    </span>

                    <span className="px-3 py-1 rounded-full bg-pink-600 text-white text-sm">
                        Goal
                    </span>

                    <span className="px-3 py-1 rounded-full bg-red-600 text-white text-sm">
                        Risk
                    </span>

                    <span className="px-3 py-1 rounded-full bg-emerald-600 text-white text-sm">
                        Decision
                    </span>

                </div>

            </div>

            <div className="h-[900px] rounded-xl overflow-hidden border border-slate-800">

                <ReactFlow

                    nodes={layout.nodes}

                    edges={layout.edges}

                    nodeTypes={nodeTypes}

                    fitView
                    fitViewOptions={{
                        padding: 0.4
                    }}
                    
                    defaultViewport={{
                        x: 0,
                        y: 0,
                        zoom: 0.6
                    }}

                    minZoom={0.15}

                    maxZoom={2}
                    
                    onNodeClick={(event, node) => {
                        
                        console.log("Node Clicked");

                        console.log(node);

                        setSelectedNode(node);

                    }}

                    defaultEdgeOptions={{
                        
                        type: "smoothstep",

                        animated: true,

                        markerEnd: {
                            type: MarkerType.ArrowClosed
                        },

                        style: {
                            stroke: "#22d3ee",
                            strokeWidth: 3
                        }
                    }}

                >

                    <MiniMap
                    
                        zoomable

                        pannable

                    />

                    <Controls />

                    <Background

                        gap={20}

                        size={1}

                    />

                </ReactFlow>

            </div>

            {selectedNode && (

                <div className="mt-6 rounded-2xl bg-slate-800 border border-cyan-600 p-6">

                    <h2 className="text-2xl font-bold text-white">
                        
                        {getTitle(selectedNode?.data?.type)}

                    </h2>

                    <div className="mt-6">

                        {renderNodeDetails(selectedNode, data)}

                    </div>
                
                </div>

                )}

        </div>

    );

}

export default KnowledgeGraph;