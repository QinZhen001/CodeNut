<template>
  <div class="myhead">
    <div class="meun-wrapper">
      <img class="logo" width="146" height="38" src="static/logo.png" @click="LinkToHome">
      <el-menu class="menu" mode="horizontal" theme="dark" @select="handleSelect">
        <el-menu-item v-for="(item, index) in headrs" :key="index" :index=item>{{item}}
        </el-menu-item>
        <transition name="el-fade-in-linear">
          <el-dropdown @command="handleCommand" trigger="hover" v-show="showUserItem">
                <span class="el-dropdown-link">
                    <img class="user-logo" src="static/avatar.jpg">
                    <span class="user-name">{{user.username}}</span>
                </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="usercenter">用户中心</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </transition>
      </el-menu>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { clearToken } from 'common/js/cache'
  import axios from 'axios'
  import { mapMutations, mapGetters, mapActions } from 'vuex'
  import { baseUrl, MSG_OK } from 'common/js/data'

  export default {
    props: {
      datas: {
        type: Array,
        default: ['注册', '用户登录', '管理员登录']
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
        switch (key) {
          case '注册':
            this.$emit('register')
            break
          case '用户登录':
            this.$emit('login')
            break
          case '退出登录':
            this.quitUser()
            break
          case '管理员登录':
            this.LinkToMangerLogin()
            break
          case '自学资料':
            this.LinkToSelfstudy()
            break
          case '用户中心':
            this.LinkToUserCenter()
            break
        }
      },
      quitUser() {
        this.$confirm('是否要退出登录?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          //注销用户
          this._logoff()
        }).catch(() => {
        })
      },
      _logoff() {
        let url = `${baseUrl}/tokens`
        axios.delete(url).then(response => {
          if (response.data.msg === MSG_OK) {
            clearToken()
            this.clearOneUser()
            // 修改header的内容
            this.headrs = ['注册', '用户登录', '管理员登录']
            // 清空相关的 localstorage
            this.$notify({
              title: '退出登录',
              message: '注销用户成功!',
              type: 'success'
            })
            console.log('成功退出')
            this.$router.push('/home')
            //注销用户成功 修改 axios的 拦截器
            this._changeAxiosInterceptor()
          }
        }, response => {
          this._logoff()
        })
      },
      _changeAxiosInterceptor() {
        console.log('_changeAxiosInterceptor')
        axios.interceptors.request.use(
          config => {
            config.headers.token = ''
            config.auth = {}
            return config
          },
          err => {
            return Promise.reject(err)
          })
      },
      handleCommand(command) {
        console.log(command)
        if (command === 'usercenter') {
          this.LinkToUserCenter()
        }
      },
      LinkToUserCenter(){
        this.$router.push('/home/usercenter')
      },
      LinkToHome() {
        this.$router.push('/home')
      },
      LinkToMangerLogin() {
        this.$router.push('/home/managerlogin')
      },
      LinkToSelfstudy(){
        this.$router.push('/home/selfstudy')
      },
      ...mapMutations({
        setUser: 'SET_USER'
      }),
      ...mapGetters({
        getUser: 'user'
      }),
      ...mapActions([
        'clearOneUser'
      ])
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

<style scoped lang="stylus" rel="stylesheet/stylus">
  .myhead
    flex: 0 0 60px;
    width 100%
    max-width 100%
    margin-bottom: 8px;
    background-color #324157
    .meun-wrapper
      position relative
      width 100%
      height 60px
      .logo
        position absolute
        top 10px
        left 200px
        display inline-block
        vertical-align: sub
        &:hover
          cursor pointer
      .menu
        margin-left 60%
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

      .menu
        padding-left: 0

</style>
