import {BASE_URL, fetchData} from "@/api/index.js";

export const getProducts = async () =>
    await fetchData({url: `${BASE_URL}/product`})


export const getProductById = async (id) =>
    await fetchData({url: `${BASE_URL}/product/${id}`})


export const createProduct = async (data) =>
    await fetchData({
        url: `${BASE_URL}/product`, method: 'POST', body: data
    },)

