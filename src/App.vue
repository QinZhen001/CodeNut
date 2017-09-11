<template>
  <div id="app">
    <m-header @login="_login" @register="_register" :datas="headers"></m-header>
    <login :dialogVisible="showLoginDialog" @closeLoginDialog="_closeLoginDialog" v-show="showLoginDialog"
           @loginSuccess="loginSuccess" ref="login"></login>
    <register :dialogVisible="showRegisterDialog" @closeRegisterDialog="_closeRegisterDialog"></register>
    <router-view></router-view>
  </div>
</template>

<script>
  import MHeader from 'components/m-header/m-header'
  import Login from 'components/login/login'
  import axios from 'axios'
  import { getUserId } from 'common/js/cache'
  import { mapMutations } from 'vuex'
  import Register from 'components/register/register'

  export default {
    data() {
      return {
        showLoginDialog: false,
        showRegisterDialog: false,
        headers: ['注册', '登录']
      }
    },
    methods: {
      _login() {
        this.showLoginDialog = true
      },
      _register() {
        this.showRegisterDialog = true
      },
      _closeRegisterDialog() {
        this.showRegisterDialog = false
      },
      _closeLoginDialog() {
        this.showLoginDialog = false
      },
      loginSuccess() {
        // 在这里 同时保存用户信息 到Vuex
        let url = 'https://api.txdna.cn/users/' + getUserId()
        axios.get(url).then(response => {
          console.log(response)
          let user = {}
          user.id = response.data.id
          user.username = response.data.username
          user.realname = response.data.realname
          user.email = response.data.email
          user.school = response.data.school
          user.occupation = response.data.occupation
          user.company = response.data.company
          user.profile = response.data.profile
          user.about_me = response.data.about_me
          console.log('user')
          console.log(user)
          this.headers = ['注册', '退出登录']
          this.setUser(user)
        }, response => {
          console.log(response)
          // 如果没有拿到数据 再次调用此方法
          this.loginSuccess()
        })
      },
      ...mapMutations({
        setUser: 'SET_USER'
      })
    },
    components: {
      MHeader,
      Login,
      Register
    }
  }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
</style>
