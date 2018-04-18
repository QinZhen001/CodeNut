<template>
  <div id="app">
    <m-header></m-header>
    <router-view></router-view>
    <m-footer></m-footer>
  </div>
</template>

<script>
  import MHeader from 'components/myheader/myheader'
  import Welcome from 'components/welcome/welcome'
  import axios from 'axios'
  import { mapMutations } from 'vuex'
  import MFooter from 'components/myfooter/myfooter'
  import User from 'common/js/user'
  import { baseUrl, MSG_OK } from 'common/js/data'

  export default {
    data() {
      return {
        headers: ['注册', '用户登录', '管理员登录']
      }
    },
    beforeDestory: function () {
      console.log('beforeDestory')
      this.clearOneUser()
    },
    methods: {
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
        this.$router.push('/selfstudy')
      },
      ...mapMutations({
        setUser: 'SET_USER'
      })
    },
    components: {
      MHeader,
      MFooter,
      Welcome
    }
  }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
  #app
    display: flex;
    flex-direction: column;
</style>
