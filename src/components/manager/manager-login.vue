<template>
  <div class="manager-login">
    <div class="ms-title">CodeNut管理员后台</div>
    <div class="ms-login">
      <el-form :model="mangerLoginForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
        <el-form-item prop="username">
          <el-input v-model="mangerLoginForm.username" placeholder="请输入管理员账号"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" placeholder="请输入管理员密码" v-model="mangerLoginForm.password"
                    @keyup.enter.native="submitForm('ruleForm')"></el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
        </div>
        <!--<p style="font-size:12px;line-height:30px;color:#999;">Tips : 用户名和密码随便填。</p>-->
      </el-form>
    </div>

  </div>
</template>

<script type="text/ecmascript-6">
  // import { getToken } from 'common/js/cache'
  import axios from 'axios'
  import { saveToken, getToken } from 'common/js/cache'
  import { baseUrl, MSG_OK } from 'common/js/data'
  import { mapGetters, mapActions } from 'vuex'
  import User from 'common/js/user'

  export default {
    data: function () {
      return {
        mangerLoginForm: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            {required: true, message: '用户名不能为空', trigger: 'blur'},
            {min: 5, message: '用户名过短', trigger: 'blur'}
          ],
          password: [
            {required: true, message: '密码不能为空', trigger: 'blur'},
            {min: 5, message: '密码过短', trigger: 'blur'}
          ]
        }
      }
    },
    created() {
      this.mangerLoginForm.username = ''
      this.mangerLoginForm.password = ''
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this._loginManager()
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      _loginManager() {
        let url = `${baseUrl}/tokens`
        axios.post(url, {
          'username': this.mangerLoginForm.username,
          'password': this.mangerLoginForm.password
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            // 判断用户是否是管理员
            this.FindUserInfo(response.data.result[0].id)
            // 登录成功保存 token
            if (this.user.role !== 'user') {
              saveToken(response.data.result[0].token)
              // 登录后 修改axios的拦截器
              this._changeAxiosInterceptor()
              // 页面跳转
              this.$notify({
                title: '成功',
                message: '管理员登录成功',
                type: 'success'
              })
              this.$router.push('/home/manager')
            } else {
              this.$notify({
                title: '错误',
                message: '此用户不是管理员',
                type: 'error'
              })
            }
          }
        }, response => {
          console.log(response)
          this.$notify.error({
            title: '错误',
            message: '登录失败'
          })
          this.mangerLoginForm.username = ''
          this.mangerLoginForm.password = ''
        })
      },
      _changeAxiosInterceptor() {
        console.log(getToken())
        console.log(this.mangerLoginForm)
        axios.interceptors.request.use(
          config => {
            config.headers.token = getToken()
            config.auth = {
              username: this.mangerLoginForm.username,
              password: this.mangerLoginForm.password
            }
            return config
          },
          err => {
            return Promise.reject(err)
          })
      },
      FindUserInfo(id) {
        console.log(id)
        let url = `${baseUrl}/users/${id}`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            if (response.data.result[0].role !== 'user') {
              this.saveOneUser(new User(response.data.result[0]))
            }
          }
        }, response => {})
      },
      ...mapActions([
        'saveOneUser'
      ])

    },
    computed: {
      ...mapGetters([
        'user'
      ])
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manager-login
    position: fixed;
    width: 100%;
    height: 100%;
    z-index 300
    background-color #324157
    .ms-title
      position: absolute;
      top: 50%;
      width: 100%;
      margin-top: -230px;
      text-align: center;
      font-size: 30px;
      color: #fff;
    .ms-login
      position: absolute;
      left: 50%;
      top: 50%;
      width: 300px;
      height: 160px;
      margin: -150px 0 0 -190px;
      padding: 40px;
      border-radius: 5px;
      background: #fff;
      .el-form-item
        margin-bottom 20px
      .login-btn
        text-align: center;
        margin-top 5px
        button
          width: 100%;
          height: 36px;
</style>
