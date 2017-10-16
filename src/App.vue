<template>
  <div id="app">
    <el-row>
      <el-col :span="0" :sm="24" :lg="24" :md="24" :xs="24">
        <m-header @login="_login" @register="_register" :datas="headers"></m-header>
      </el-col>
    </el-row>
    <login :dialogVisible="showLoginDialog" @closeLoginDialog="_closeLoginDialog" v-show="showLoginDialog"
           @loginSuccess="loginSuccess" ref="login"></login>
    <register :dialogVisible="showRegisterDialog" @closeRegisterDialog="_closeRegisterDialog"></register>
    <router-view></router-view>
    <m-footer></m-footer>
  </div>
</template>

<script>
  import MHeader from 'components/myheader/myheader'
  import Login from 'components/login/login'
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
            this.headers = ['退出登录']
            let result = response.data.result[0]
//            let user = new User({
//              user_id: result.user_id,
//              username: result.username,
//              realname: result.realname,
//              school: result.school,
//              profile: result.profile,
//              about_me: result.about_me,
//              role: result.role,
//              accept_nums: result.accept_nums,
//              submit_nums: result.submit_nums,
//              tag: result.tag
//            })
//            this.setUser(user)
            this.saveOneUser(new User(result))
            // console.log(user)
          }
        }, response => {
          console.log(response)
          // 如果没有拿到数据 再次调用此方法
          this.loginSuccess()
        })
      },
      ...mapMutations({
        setUser: 'SET_USER'
      }),
      ...mapActions([
        'saveOneUser'
      ])

    },
    components: {
      MHeader,
      Login,
      Register,
      MFooter
    }
  }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
  #app
    display: flex;
    flex-direction: column;
    min-height: 100%;
</style>
