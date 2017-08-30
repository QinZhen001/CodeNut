<template>
  <transition name="slide">
    <div class="register">
      <mt-header title="注册">
        <router-link to="/search" slot="left">
          <mt-button icon="back">返回</mt-button>
        </router-link>
      </mt-header>

      <div class="input-wrapper">
        <input class="input-item" placeholder="请输入用户名" type="text" v-model.trim.lazy="username" ref="username">
        <input class="input-item" placeholder="请输入密码" type="password" v-model.trim.lazy="password" ref="password">
        <input class="input-item" placeholder="请输入邮箱" type="text" v-model.trim.lazy="email" ref="email">
        <input class="input-item" placeholder="请输入学校" type="text" v-model.trim.lazy="school" ref="school">
        <input class="input-item" placeholder="请输入职业" type="text" v-model.trim.lazy="occupation" ref="occupation">
      </div>
      <mt-button type="primary" class="btn-register" @click.stop="register">注册</mt-button>
    </div>

  </transition>
</template>

<script type="text/ecmascript-6">
  const MSG_OK = 'ok'
  const MSG_NO = 'no'

  export default{
    data() {
      return {
        username: '',
        password: '',
        email: '',
        school: '',
        occupation: ''
      }
    },
    methods: {
      register() {
        // 暂时没有做正则表达式验证每一项数据是否正确
        let url = 'https://api.txdna.cn/users'
        this.$http.post(url, {
          'username': this.username,
          'password': this.password,
          'email': this.email,
          'school': this.school,
          'occupation': this.occupation
        }).then(response => {
          console.log(response.body)
          if (response.body.msg === MSG_OK) {
            this.$toast({
              message: '注册成功',
              position: 'bottom',
              iconClass: 'icon icon-ok'
            })
            this.$router.push({
              path: '/aboutme'
            })
          } else if (response.body.msg === MSG_NO) {
            this.$toast({
              message: '该用户已存在',
              position: 'bottom',
              iconClass: 'icon icon-delete'
            })
            this.username = ''
            this.$refs.username.focus()
          }
        }, response => {
          console.log(response)
          this.$toast({
            message: '注册失败',
            position: 'bottom',
            iconClass: 'icon icon-delete'
          })
        })
      }
    },
    watch: {
      username(newVal) {
        console.log(newVal)
        if (newVal.length < 6) {
          this.$toast({
            message: '用户名过短,请重新输入',
            position: 'bottom'
          })
          this.username = ''
          this.$refs.username.focus()
        }
      },
      password(newVal) {
        if (newVal.length < 6) {
          this.$toast({
            message: '密码过短,请重新输入',
            position: 'bottom'
          })
          this.password = ''
          this.$refs.password.focus()
        }
      },
      email(newVal) {
        let patt = new RegExp('([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+')
        if(!patt.test(newVal)) {
          this.$toast({
            message: '请输入正确的邮箱',
            position: 'bottom'
          })
          this.email = ''
          this.$refs.email.focus()
        }
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  @import "~common/stylus/mixin"

  .register
    position: fixed
    left: 0
    right: 0
    top: 0
    bottom: 0
    z-index: 1000
    background-color: $color-background
    text-align center
    .input-wrapper
      margin 30px 0 30px 0
      text-align center
      .input-item
        width: 80%;
        height: 40px;
        margin-bottom 15px
        padding-left 10px
        border: 1px solid white;
        border-radius: 4px;
        color: white;
        background-color $color-background
    .btn-register
      width 70%
      margin 0 auto

  .slide-enter-active, .slide-leave-active
    transition: all 0.3s

  .slide-enter, .slide-leave-to
    transform: translate3d(100%, 0, 0)

</style>
