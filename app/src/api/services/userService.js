import {BASE_URL, fetchData} from "@/api/index.js";

export const getUsers = async () =>
    await fetchData({url: `${BASE_URL}/user`})


export const getUserById = async (id) =>
    await fetchData({url: `${BASE_URL}/user/${id}`})


export const createUser = async (data) =>
    await fetchData({
        url: `${BASE_URL}/user`, method: 'POST', body: data
    },)

