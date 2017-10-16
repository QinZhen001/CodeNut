import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const Home = (resolve) => {
  import('components/home/home').then((moudle) => {
    resolve(moudle)
  })
}
const ProblemDetail = (resolve) => {
  import('components/problem-detail/problem-detail').then((moudle) => {
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
// const ManageProblemEdit = (resolve) => {
//   import('components/manager/manage-problem-edit').then((moudle) => {
//     resolve(moudle)
//   })
// }

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
          // children: [
          //   {
          //     path: '/home/manager/manageproblems/edit',
          //     component: ManageProblemEdit
          //   }
          // ]
        }
      ]
    }, {
      path: '/home/breakthrough',
      component: BreakThrough
      //component: TestCanvas
    }
  ]
})

