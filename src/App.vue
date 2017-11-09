<template>
  <div id="app">
    <m-header @login="_login" @register="_register" :datas="headers"></m-header>
    <router-view></router-view>
    <m-footer></m-footer>
    <welcome ref="welcome" @clickLogin="_login" @clickRegister="_register" @linkToselfStudy="linkToselfStudy"></welcome>
    <login :dialogVisible="showLoginDialog" @closeLoginDialog="_closeLoginDialog" v-show="showLoginDialog"
           @loginSuccess="loginSuccess" ref="login"></login>
    <register :dialogVisible="showRegisterDialog" @closeRegisterDialog="_closeRegisterDialog"></register>
  </div>
</template>

<script>
  import MHeader from 'components/myheader/myheader'
  import Login from 'components/login/login'
  import Welcome from 'components/welcome/welcome'
  import axios from 'axios'
  import { mapMutations, mapActions } from 'vuex'
  import Register from 'components/register/register'
  import MFooter from 'components/myfooter/myfooter'
  import User from 'common/js/user'
  import { baseUrl, MSG_OK } from 'common/js/data'

  export default {
    data() {
      return {
        showLoginDialog: false,
        showRegisterDialog: false,
        headers: ['注册', '用户登录', '管理员登录']
      }
    },
    beforeDestory: function () {
      console.log('beforeDestory')
      this.clearOneUser()
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
      loginSuccess(id) {
        console.log(id)
        // 在这里 同时保存用户信息 到Vuex
        let url = `${baseUrl}/users/${id}`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.headers = ['退出登录', '自学资料', '用户中心']
            let result = response.data.result[0]
            this.saveOneUser(new User(result))
            this.$refs.welcome.linkToHome()
          }
        }, response => {
          console.log(response)
          // 如果没有拿到数据 再次调用此方法
          this.loginSuccess()
        })
      },
      linkToselfStudy(){
        this.$router.push('/home/selfstudy')
      },
      ...mapMutations({
        setUser: 'SET_USER'
      }),
      ...mapActions([
        'saveOneUser',
        'clearOneUser'
      ])

    },
    components: {
      MHeader,
      Login,
      Register,
      MFooter,
      Welcome
    }
  }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
  #app
    display: flex;
    flex-direction: column;
    min-height: 100%;
</style>
