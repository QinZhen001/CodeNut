<template>
  <el-dialog title="用户登录" :visible.sync="visible" :before-close="handleBeforeClose">
    <el-form>
      <el-form-item label="账号:" :label-width="formLabelWidth">
        <el-input v-model.trim.lazy="username" placeholder="请输入账号" ref="username" spellcheck="false"></el-input>
      </el-form-item>
      <el-form-item label="密码:" :label-width="formLabelWidth">
        <el-input v-model.trim.lazy="password" type="password" placeholder="请输入密码"></el-input>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="clickCancel">取 消</el-button>
      <el-button type="primary" @click="clickConfirm">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script type="text/ecmascript-6">
  import axios from 'axios'
  import User from 'common/js/user'
  import { saveToken, getToken } from 'common/js/cache'
  import { baseUrl, MSG_OK } from 'common/js/data'
  import { mapMutations, mapActions } from 'vuex'

  export default {
    data() {
      return {
        username: '',
        password: '',
        formLabelWidth: '50px',
        visible: false
      }
    },
    mounted() {
      this.clearData()
    },
    methods: {
      show(){
        this.visible = true
      },
      hide(){
        this.visible = false
      },
      clearData(){
        this.username = ''
        this.password = ''
      },
      clickCancel() {
        this.clearData()
        this.hide()
      },
      clickConfirm() {
        let url = `${baseUrl}/tokens`
        axios.post(url, {'username': this.username, 'password': this.password}).then(response => {
          console.log(response)
          // 登录成功保存token到localStorage
          saveToken(response.data.result[0].token)
          this.afterLoginSuccess(response.data.result[0].id)
          this.$notify({
            title: '成功',
            message: '登录成功',
            type: 'success'
          })
        }, response => {
          console.log(response)
          this.$notify.error({
            title: '错误',
            message: '登录失败'
          })
          this.clearData()
        })
        console.log(this.username)
        console.log(this.password)
      },
      afterLoginSuccess(id) {
        // 登录后 修改axios的拦截器
        this._changeAxiosInterceptor()
        console.log(id)
        // 在这里 同时保存用户信息 到Vuex
        let url = `${baseUrl}/users/${id}`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.setHeaderData(['退出登录', '自学资料', '用户中心'])
            this.saveOneUser(new User(response.data.result[0]))
            this.linkToHome()
            this.clickCancel()
          }
        }, response => {
          console.log(response)
          this.afterLoginSuccess(id)
        })
      },
      linkToHome(){
        this.$router.replace('/home')
      },
      handleBeforeClose(done) {
        this.clickCancel()
      },
      _changeAxiosInterceptor() {
        axios.interceptors.request.use(
          config => {
            config.headers.token = getToken()
            config.auth = {
              username: this.username,
              password: this.password
            }
            return config
          },
          err => {
            return Promise.reject(err)
          })
      },
      ...mapMutations({
        setHeaderData: 'SET_HEADERDATA'
      }),
      ...mapActions([
        'saveOneUser',
        'clearOneUser'
      ])
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .el-dialog
    max-width 600px
</style>
