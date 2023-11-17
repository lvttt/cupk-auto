// router.js

import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    meta: {
      title: '登录'
    },
    component: () => import('../components/Login.vue'),
  },
  {
    path: '/sis/home',
    name: 'SisHome',
    component: () => import('../components/SisHome.vue'),
    children:[
      {path: 'qk', component: () => import('../components/SIS/SisSelectCourse.vue'),meta:{title:'抢课助手'}},
      {path: 'pj', component: () => import('../components/SIS/SisAutoRate.vue'),meta:{title:'自动评教'}},
      {path: 'cj', component: () => import('../components/SIS/SisGrade.vue'),meta:{title:'成绩查询'}},
    ]
  },
  {
    path: '/fp/home',
    name: 'FpHome',
    component: () => import('../components/FpHome.vue'),
    children:[
      {path: 'main', component: () => import('../components/FusionPortal/FpMain.vue'),meta:{title:'首页'}},
    ]
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

// 路由前置导航守卫
router.beforeEach((to,from,next)=>{
  // 根据路由元信息设置文档标题
  window.document.title = to.meta.title || 'cupk-auto'
  next()
})

export default router;
