import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

//  可以用const Foo = () => import('./Foo.vue')
const Home = (resolve) => {
  import('components/home/home').then((moudle) => {
    resolve(moudle)
  })
}
const Welcome = (resolve) => {
  import('components/welcome/welcome').then((moudle) => {
    resolve(moudle)
  })
}
const ProblemDetail = (resolve) => {
  import('components/problem-detail/problem-detail').then((moudle) => {
    resolve(moudle)
  })
}
const BgAnimation = (resolve) => {
  import('components/breakthrough/bganimation').then((moudle) => {
    resolve(moudle)
  })
}
const SelfStudy = (resolve) => {
  import('components/selfstudy/selfstudy').then((moudle) => {
    resolve(moudle)
  })
}
const UserCenter = (resolve) => {
  import('components/usercenter/usercenter').then((moudle) => {
    resolve(moudle)
  })
}
const MangerLogin = (resolve) => {
  import('components/manager/manager-login').then((moudle) => {
    resolve(moudle)
  })
}
const MangerCenter = (resolve) => {
  import('components/manager/manager-center').then((moudle) => {
    resolve(moudle)
  })
}
const BreakThrough = (resolve) => {
  import('components/breakthrough/breakthrough').then((moudle) => {
    resolve(moudle)
  })
}
const ManageUsers = (resolve) => {
  import('components/manager/manage-users').then((moudle) => {
    resolve(moudle)
  })
}
const ManageProblems = (resolve) => {
  import('components/manager/manage-problems').then((moudle) => {
    resolve(moudle)
  })
}
const ManageContests = (resolve) => {
  import('components/manager/manage-contests').then((moudle) => {
    resolve(moudle)
  })
}

// 路径设置不是很好 懒得再调了
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Welcome
    },
    {
      path: '/home',
      component: Home
    },
    {
      path: '/problem',
      component: ProblemDetail,
      meta: {scrollToTop: true},
      children: [
        {
          path: '/problem/success-animation',
          component: BgAnimation
        }
      ]
    },
    {
      path: '/selfstudy',
      component: SelfStudy
    },
    {
      path: '/usercenter',
      component: UserCenter
    },
    {
      path: '/managerlogin',
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
      path: '/breakthrough',
      component: BreakThrough
    }
  ]
})

