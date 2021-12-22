import { createRouter, createWebHashHistory } from 'vue-router'
import Signup from '../views/Signup.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Forgot from '../views/Forgot.vue'
import NotFound from '../views/NotFound.vue'
import Whitepaper from '../views/Whitepaper.vue'
import Terms from '../views/Terms.vue'
import Buy from '../views/Buy.vue'
import Orders from '../views/Orders.vue'
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    props: true,
    meta: {
      requiresAuth: false,
      goToTeam: { methodName: "goToTeam" },
      goToRoadmap: { methodName: "goToRoadmap" }
    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
    meta:{
      requires: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta:{
      requires: true
    }
  },
  {
    path: '/forgot',
    name: 'Forgot',
    component: Forgot
  },
  {
    path: '/whitepaper',
    name: 'Whitepaper',
    component: Whitepaper
  },
  {
    path: '/terms',
    name: 'Terms',
    component: Terms
  },
  {
    path: '/buy',
    name: 'Buy',
    component: Buy
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders
  },
  {
    path:'/:catchAll(.*)',
    name: 'NotFound',
    component: NotFound
  }
]


const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const currentUser = firebase.auth().currentUser
  const requires = to.matched.some(record => record.meta.requires)
  
  if(requires && currentUser) next('/')
  else next()
})


export default router
