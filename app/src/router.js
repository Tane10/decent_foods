import { createMemoryHistory, createRouter } from 'vue-router'

import Profile from "@/components/Profile.vue";
import HomeView from "@/components/HomeView.vue";

const routes = [
    { path: '/', component: HomeView },
    // {path: '/user', component: Profile}
]

const router = createRouter({
    history: createMemoryHistory(),
    routes,
})

export default router