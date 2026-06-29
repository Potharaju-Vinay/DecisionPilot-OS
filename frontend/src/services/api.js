import axios from "axios";

const api = axios.create({

    baseURL: "http://127.0.0.1:8000",

    timeout: 120000,
    
    headers: {

        "Content-Type": "application/json"

    }

});

api.interceptors.request.use(

    (config) => {

        console.log("REQUEST");

        console.log(config.method);

        console.log(config.url);

        return config;

    },

    (error) => Promise.reject(error)

);

api.interceptors.response.use(

    (response) => {

        console.log("SUCCESS");

        console.log(response.status);

        return response;

    },

    (error) => {

        console.log("AXIOS ERROR");

        console.log(error.response);

        return Promise.reject(error);

    }

);

export default api;