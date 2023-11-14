// router.js

import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('../components/Login.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../components/Login.vue')
  },
  {
    path: '/sis/home',
    name: 'SisHome',
    component: () => import('../components/SisHome.vue'),
    children:[
      {path: 'qk', component: () => import('../components/SIS/SisSelectCourse.vue')},
      {path: 'pj', component: () => import('../components/SIS/SisAutoRate.vue')}
    ]
  },
  {
    path: '/fp/home',
    name: 'FpHome',
    component: () => import('../components/FpHome.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
