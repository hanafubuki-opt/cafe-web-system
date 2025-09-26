import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api", 
});

export default api;

export const getMenu = async () => {
  const response = await api.get("/menu");
  return response.data;
};

export const createOrder = async (orderData) => {
  const response = await api.post("/orders", orderData);
  return response.data;
};