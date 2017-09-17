<template>
  <div class="head">
    <img class="logo" width="146" height="38" src="static/logo.png">
    <div class="head-wrapper">
      <el-menu theme="dark" class="menu" mode="horizontal" @select="handleSelect">
        <el-menu-item v-for="(item, idx) in headrs" :key="idx" :index=(item)>{{item}}
        </el-menu-item>
        <el-dropdown @command="handleCommand" trigger="hover" v-show="showUserItem">
                <span class="el-dropdown-link">
                    <img class="user-logo" src="static/avatar.jpg">
                    <span class="user-name">{{user.username}}</span>
                </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="usercenter">用户中心</el-dropdown-item>
            <el-dropdown-item command="loginout">退出</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-menu>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { clearToken, clearUserId } from 'common/js/cache'
  import axios from 'axios'
  import { mapMutations, mapGetters } from 'vuex'

  export default {
    props: {
      datas: {
        type: Array,
        default: ['注册', '登录']
      }
    },
    data() {
      return {
        headrs: this.datas,
        user: {}
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key)
        if (key === '注册') {
          // 注册
          console.log('111')
          this.$emit('register')
        } else if (key === '登录') {
          // 登录
          console.log('222')
          this.$emit('login')
        } else if (key === '退出登录') {
          this.quitUser()
        }
      },
      quitUser() {
        this.$confirm('是否要退出登录?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$notify({
            title: '成功',
            message: '退出登录成功!',
            type: 'success'
          })
          // 修改header的内容
          this.headrs = ['注册', '登录']
          // 清空相关的 localstorage
          clearToken()
          clearUserId()
          // 修改 axios的 拦截器
          axios.interceptors.request.use(
            config => {
              config.headers.token = ''
              config.auth = {}
              return config
            },
            err => {
              return Promise.reject(err)
            })
          // 成功退出后 才修改vuex 中的 user 数据
          this.user = {}
          this.setUser(this.user)
          console.log('成功退出')
          console.log(this.getUser())
        }).catch(() => {
        })
      },
      handleCommand(command) {
        console.log(command)
        if (command === 'loginout') {
          this.quitUser()
        } else if (command === 'usercenter') {
          this.$router.push('/home/usercenter')
        }
      },
      ...mapMutations({
        setUser: 'SET_USER'
      }),
      ...mapGetters({
        getUser: 'user'
      }),
      calcIndex(item) {
        return item.toString()
      }
    },
    watch: {
      datas(newVal) {
        this.headrs = newVal
      }
    },
    computed: {
      showUserItem() {
        if (this.headrs.indexOf('退出登录') !== -1) {
          // 证明已经登录 那么显示用户
          this.user = this.getUser()
          console.log(this.user)
          return true
        } else {
          return false
        }
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .head
    width 100%
    position relative
    margin-bottom: 8px;
    background-color #324157
    .logo
      z-index 100
      position absolute
      top 11px
      left 200px
      vertical-align: sub
    .head-wrapper
      .menu
        margin-left: 1000px;
        max-height 60px
        min-width 350px
        .el-dropdown-link
          position: relative;
          display: inline-block;
          width 80px
          height 60px
          padding-left: 20px;
          color: #fff;
          &:hover
            cursor: pointer
          .user-logo
            position: absolute;
            left: 0;
            top 9px
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border 1px solid #fff
          .user-name
            position: absolute;
            display: inline-block;
            right: 0;
            font-size: 16px;
            color: whitesmoke
            line-height 60px
        .el-dropdown-menu
          padding: 1px 0;
          .el-dropdown-menu__item
            text-align: center;

  @media screen and (max-width: 1330px)
    .el-menu
      position relative
      transform: translateX(-180px);

  @media screen and (max-width: 1150px)
    .el-menu
      position relative
      transform: translateX(-300px);

  @media screen and (max-width: 1050px)
    .el-menu
      position relative
      transform: translateX(-450px);

  @media screen and (max-width: 890px)
    .el-menu
      position relative
      transform: translateX(-600px);

    @media screen and (max-width: 800px)
      .logo
        display none

      .menu
        padding-left: 0

</style>
