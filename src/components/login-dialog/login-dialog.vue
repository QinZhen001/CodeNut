<template>
  <div>
  <transition name="dialog-fade">
    <div class="dialog" v-show="showFlag" @click.stop>
      <div class="dialog-wrapper">
        <div class="dialog-content">
          <div class="dialog-title">CodeNut</div>
          <div class="input-wrapper">
            <input class="text-input" type="text" placeholder="请输入用户名" v-model="username">
            <input class="text-input" type="password" placeholder="请输入密码" v-model="password">
          </div>
          <div class="operate">
            <div @click="confirm" class="operate-btn left">登录</div>
            <div @click="cancel" class="operate-btn">取消</div>
          </div>
          <div class="text-register" @click.stop="registerUser">去注册</div>
        </div>
      </div>
    </div>
  </transition>
    <transition name="fade">
      <div class="mask" v-show="showFlag"></div>
    </transition>
  </div>
</template>

<script type="text/ecmascript-6">
  import { saveToken, saveUserId } from 'common/js/cache'

  export default{
    data() {
      return {
        showFlag: false,
        username: '',
        password: ''
      }
    },
    methods: {
      show() {
        this.showFlag = true
      },
      hide() {
        this.showFlag = false
      },
      cancel() {
        this.hide()
      },
      confirm() {
        let url = 'https://api.txdna.cn/tokens'
        this.$http.post(url, {'username': this.username, 'password': this.password}).then(response => {
          console.log(response.body)
          // 登录成功保存 token 和 id
          saveToken(response.body.token)
          saveUserId(response.body.id)
          let user = {}
          user.id = response.body.id
          user.username = this.username
          user.password = this.password
          // 登录成功发送 loginsucceed 父组件接收
          this.$emit('loginsucceed', user)
          this.$toast({
            message: '登录成功',
            position: 'bottom',
            iconClass: 'icon icon-ok'
          })
        }, response => {
          console.log(response)
          this.$toast({
            message: '登录失败',
            position: 'bottom',
            iconClass: 'icon icon-delete'
          })
        })
        console.log(this.username)
        console.log(this.password)
        this.hide()
      },
      registerUser() {
        this.hide()
        this.$emit('register')
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .dialog
    position: fixed
    left: 0
    right: 0
    top: 0
    bottom: 0
    z-index: 998
    background-color: $color-background-d
    &.dialog-fade-enter-active
      animation: dialog-fadein 0.3s
    .dialog-content
      animation: dialog-zoom 0.3s
    .dialog-wrapper
      position: absolute
      top: 50%
      left: 50%
      transform: translate(-50%, -50%)
      z-index: 999
      .dialog-content
        width: 270px
        border-radius: 13px
        background: $color-highlight-background
        .dialog-title
          padding 10px 0 8px 0
          width 100%
          text-align center
          color $color-theme
          font-size $font-size-large-l
          border-bottom: 1px solid $color-background-d
        .input-wrapper
          width 270px
          .text-input
            height 32px
            width 100%
            background-color: $color-highlight-background
            color white
            border-bottom: 1px solid $color-background-d
            font-family: sans-serif;
        .operate
          display: flex
          align-items: center
          text-align: center
          font-size: $font-size-large
          .operate-btn
            flex: 1
            line-height: 22px
            padding: 10px 0
            border-bottom 1px solid $color-background-d
            color: $color-text-d
            &.left
              border-right: 1px solid $color-background-d
              color $color-theme
        .text-register
          padding 10px 0 8px 0
          width 100%
          text-align center

  .mask
    position: fixed
    top: 0
    left: 0
    width: 100%
    height: 100%
    z-index: 200
    backdrop-filter: blur(10px)
    opacity: 1
    background: rgba(7, 17, 27, 0.6)
    &.fade-enter-active, &.fade-leave-active
      transition: all 0.5s
    &.fade-enter, &.fade-leave-active
      opacity: 0
      background: rgba(7, 17, 27, 0)

  @keyframes dialog-fadein
    0%
      opacity: 0
    100%
      opacity: 1

  @keyframes dialog-zoom
    0%
      transform: scale(0)
    50%
      transform: scale(1.1)
    100%
      transform: scale(1)
</style>
