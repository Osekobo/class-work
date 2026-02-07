import axios from "axios";

//create an instance of axios with base URL

const api = axios.create({
  baseURL: "http://localhost:8000"
});

//Export the Axios instance

export default api; 