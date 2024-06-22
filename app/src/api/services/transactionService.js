import {BASE_URL, fetchData} from "@/api/index.js";

export const getTransactions = async () =>
    await fetchData({url: `${BASE_URL}/transactions`})


export const getTransactionById = async (id) =>
    await fetchData({url: `${BASE_URL}/transactions/${id}`})


export const createTransaction = async (data) =>
    await fetchData({
        url: `${BASE_URL}/transactions`, method: 'POST', body: data
    },)

