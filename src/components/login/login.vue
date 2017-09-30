<template>
  <el-dialog title="用户登录" :visible.sync="dialogShow" :before-close="handleBeforeClose">
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
  import { saveToken, getToken } from 'common/js/cache'
  import { baseUrl } from 'common/js/data'

  export default {
    props: {
      dialogVisible: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        username: '',
        password: '',
        formLabelWidth: '50px',
        dialogShow: false
      }
    },
    mounted() {
      this.username = ''
      this.password = ''
    },
    methods: {
      clickCancel() {
        this.dialogShow = false
        this.$emit('closeLoginDialog')
        this.username = ''
        this.password = ''
      },
      clickConfirm() {
        let url = `${baseUrl}/tokens`
        axios.post(url, {'username': this.username, 'password': this.password}).then(response => {
          console.log(response)
          // 登录成功保存token到localStorage
          saveToken(response.data.result[0].token)
          console.log(response.data.result[0].token)
          // 登录后 修改axios的拦截器
          this._changeAxiosInterceptor()
          this.$emit('closeLoginDialog')
          this.$emit('loginSuccess', response.data.result[0].id)
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
          this.username = ''
          this.password = ''
        })
        console.log(this.username)
        console.log(this.password)
      },
      handleBeforeClose(done) {
        this.$emit('closeLoginDialog')
        this.username = ''
        this.password = ''
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
      }
    },
    watch: {
      dialogVisible(newVal) {
        this.dialogShow = newVal
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .el-dialog
    max-width 600px
</style>
