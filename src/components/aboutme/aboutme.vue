<template>
  <div class="user">
    <div class="header-wraper">
      <div class="avatar-wrapper">
        <img class="avatar" width="50" height="50" src="../../common/image/default.png" @click.stop="login"/>
      </div>
      <div class="text-wrapper">
        <span @click.stop="login" class="text-login" v-show="!isLogin">请点击登录</span>
        <span class="text-login" v-show="isLogin">{{user.username}}</span>
      </div>
    </div>
    <div class="content-wrapper">
      <div class="item-wrapper">
        <span class="text">邮箱</span>
        <span class="value" v-show="isLogin">{{user.email}}</span>
      </div>
      <div class="item-wrapper">
        <span class="text">学校</span>
        <span class="value" v-show="isLogin">{{user.school}}</span>
      </div>
      <div class="item-wrapper">
        <span class="text">职业</span>
        <span class="value" v-show="isLogin">{{user.occupation}}</span>
      </div>
      <div class="item-wrapper">
        <span class="text">公司</span>
        <span class="value" v-show="isLogin">{{user.company}}</span>
      </div>
    </div>
    <div class="quit-wrapper" v-show="isLogin">
      <mt-button type="danger" class="btn-quit" @click.stop="onClickQuit">退出登录</mt-button>
    </div>
    <confirm ref="logoffDialog" text='是否注销该用户?' @confirm="quit"></confirm>
    <login-dialog ref="loginDialog" @loginsucceed="afterLogin" @register="registerUser"></login-dialog>
    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import axios from 'axios'
  import LoginDialog from 'components/login-dialog/login-dialog'
  import Register from 'components/register/register'
  import Split from 'base/split/split'
  import Confirm from 'base/confirm/confirm'
  import { getToken, clearToken, clearUserId } from 'common/js/cache'

  export default{
    data() {
      return {
        user: {},
        isLogin: false
      }
    },
    methods: {
      login() {
        if (this.isLogin) {
          return
        }
        this._showLoginDialog()
      },
      _showLoginDialog() {
        this.$refs.loginDialog.show()
      },
      afterLogin(user) {
        console.log(user)
        // 根据id获取用户的信息
        axios.interceptors.request.use(
          config => {
            config.headers.token = getToken()
            config.auth = {
              username: user.username,
              password: user.password
            }
            return config
          },
          err => {
            return Promise.reject(err)
          })

        let url = `https://api.txdna.cn/users/${user.id}`
        axios.get(url).then(response => {
          console.log(response)
          this.user.id = response.data.id
          this.user.username = response.data.username
          this.user.realname = response.data.realname
          this.user.email = response.data.email
          this.user.school = response.data.school
          this.user.occupation = response.data.occupation
          this.user.company = response.data.company
          this.user.profile = response.data.profile
          this.user.about_me = response.data.about_me
          console.log(this.user)
          this.isLogin = true
        }, response => {
          console.log(response)
        })
      },
      registerUser() {
        this.$router.push({
          path: `/register`
        })
      },
      onClickQuit() {
        this.$refs.logoffDialog.show()
      },
      quit() {
        // 先清空storage
        clearToken()
        clearUserId()
        // 再修改拦截器
        axios.interceptors.request.use(
          config => {
            config.headers.token = ''
            config.auth = {}
            return config
          },
          err => {
            return Promise.reject(err)
          })
        // 最后修改变量
        this.isLogin = false
      }
    },
    components: {
      LoginDialog,
      Register,
      Split,
      Confirm
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  @import "~common/stylus/mixin"

  .user
    position: fixed
    width: 100%
    top: 88px
    bottom: 0
    .header-wraper
      display: flex
      height 65px
      width 100%
      align-items: center
      background-color #27AE60
      border-bottom 1px solid #ddd
      .avatar-wrapper
        padding-left 20px
        padding-right 8px
        flex: 0 0 50px
        width: 50px
        .avatar
          border-radius 50%
      .text-wrapper
        display: flex
        flex-direction: column
        justify-content: center
        flex: 1
    .content-wrapper
      padding 0 5px
      .item-wrapper
        width 100%
        height 50px
        border-bottom 1px solid #ddd
        .text
          margin-left 8px
          display inline-block
          position: relative;
          top: 50%;
          transform: translateY(-50%);
        .value
          display inline-block
          position: relative;
          top: 50%;
          float right
          margin-right 5px
          transform: translateY(-50%);
    .quit-wrapper
      margin-top 40px
      width 100%
      text-align center
      .btn-quit
        width 80%


</style>
