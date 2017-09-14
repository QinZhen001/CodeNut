import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home'
import ProblemDetail from 'components/problem-detail/problem-detail'
import UserCenter from 'components/usercenter/usercenter'
// import Login from 'components/login/login'
// import Register from 'components/register/register'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      component: Home
    },
    {
      path: '/home/problem',
      component: ProblemDetail
    },
    {
      path: '/home/usercenter',
      component: UserCenter
    }
  ]
})
