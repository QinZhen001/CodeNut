import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home'
import ProblemDetail from 'components/problem-detail/problem-detail'
import UserCenter from 'components/usercenter/usercenter'
import MangerLogin from 'components/manager/manager-login'
import MangerCenter from 'components/manager/manager-center'
//import TestCanvas from 'components/breakthrough/testcanvas'
import BreakThrough from 'components/breakthrough/breakthrough'
import ManageUsers from 'components/manager/manage-users'
import ManageProblems from 'components/manager/manage-problems'
import ManageContests from 'components/manager/manage-contests'

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
      component: ProblemDetail,
      meta: {scrollToTop: true}
    },
    {
      path: '/home/usercenter',
      component: UserCenter
    },
    {
      path: '/home/managerlogin',
      component: MangerLogin
    },
    {
      path: '/home/manager',
      redirect: '/home/manager/manageusers',
      component: MangerCenter,
      children: [
        {
          path: '/home/manager/manageusers',
          component: ManageUsers
        },
        {
          path: '/home/manager/manageproblems',
          component: ManageProblems
        },
        {
          path: '/home/manager/managecontests',
          component: ManageContests
        }
      ]
    },
    {
      path: '/home/breakthrough',
      component: BreakThrough
      //component: TestCanvas
    }
  ]
})

