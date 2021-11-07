import { createRouter, createWebHashHistory } from 'vue-router'
import Signup from '../views/Signup.vue'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: {
      requiresAuth: false,
      goToTeam: { methodName: "goToTeam" },
      goToRoadmap: { methodName: "goToRoadmap" }
    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path:'/:catchAll(.*)',
    name: 'Home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
