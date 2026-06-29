function KPICard({

    title,

    value,

    color

}){

    return(

        <div className="bg-slate-800 rounded-xl p-6 shadow-lg border border-slate-700">

            <p className="text-gray-400 text-sm">

                {title}

            </p>

            <h1

                className={`text-4xl font-bold mt-3 ${color}`}

            >

                {value}

            </h1>

        </div>

    )

}

export default KPICard;