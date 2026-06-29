import api from "./api";

export async function getDashboard() {

    const response = await api.get("/dashboard");

    return response.data;

}

export async function analyzeDocument(file) {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(

        "/analyze",

        formData,

        {

            headers: {

                "Content-Type": "multipart/form-data"

            }

        }

    );

    return response.data;

}