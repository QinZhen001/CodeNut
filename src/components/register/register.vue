<template>
  <el-dialog title="注册用户" :visible.sync="dialogShow" :before-close="handleBeforeClose">
    <el-form>
      <el-form-item label="账号:" :label-width="formLabelWidth">
        <el-input v-model.trim.lazy="username" placeholder="请输入用户名" ref="username"
                  spellcheck="false" @change="onUsernameChange"></el-input>
        <span class="prompt prompt-username" :class="showUserPrompt">*用户名过短</span>
      </el-form-item>
      <el-form-item label="密码:" :label-width="formLabelWidth">
        <el-input v-model.trim.lazy="password" type="password" placeholder="请输入密码"></el-input>
        <span class="prompt prompt-password" :class="showPasswordPrompt">*密码过短</span>
      </el-form-item>
      <el-form-item label="邮箱" :label-width="formLabelWidth">
        <el-input class="input-item" placeholder="请输入邮箱"
                  spellcheck="false" v-model.trim.lazy="email" ref="email"></el-input>
        <span class="prompt prompt-email" :class="showEmailPrompt">*邮箱格式错误</span>
      </el-form-item>
      <!--<el-form-item label="学校" :label-width="formLabelWidth">-->
        <!--<el-input class="input-item" placeholder="请输入学校"-->
                  <!--type="text" v-model.trim.lazy="school" ref="school"></el-input>-->
        <!--<span class="prompt prompt-school" :class="showSchoolPrompt">*请输入正确的学校名字</span>-->
      <!--</el-form-item>-->
      <!--<el-form-item label="职业" :label-width="formLabelWidth">-->
        <!--<el-input class="input-item" placeholder="请输入职业" type="text"-->
                  <!--v-model.trim.lazy="occupation" ref="occupation"></el-input>-->
        <!--<span class="prompt prompt-occupation" :class="showOccupationPrompt">*请输入正确的职业</span>-->
      <!--</el-form-item>-->
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="clickCancel">取 消</el-button>
      <el-button type="primary" @click="clickConfirm">确 定</el-button>
    </div>
  </el-dialog>
</template>

<script type="text/ecmascript-6">
  import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
  import axios from 'axios'

  const MSG_OK = 'ok'
  const MSG_NO = 'no'

  export default {
    components: {ElFormItem},
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
        email: '',
//        school: '',
//        occupation: '',
        formLabelWidth: '50px',
        dialogShow: false
      }
    },
    methods: {
      clickCancel() {
        this.$emit('closeRegisterDialog')
        this._clearData()
      },
      clickConfirm() {
        let url = 'https://api.txdna.cn/users'
        console.log(this.school)
        console.log(this.occupation)
        axios.post(url, {
          'username': this.username,
          'password': this.password,
          'email': this.email
        }).then(response => {
          console.log(response)
          if (response.data.msg === MSG_OK) {
            this.$notify({
              title: '成功',
              message: '注册成功!',
              type: 'success'
            })
            // 只有注册成功才关闭dialog
            this.$emit('closeRegisterDialog')
            this._clearData()
          } else if (response.data.msg === MSG_NO) {
            // 该用户已存在
            this.$notify({
              title: '警告',
              message: '用户名或邮箱已被使用!',
              type: 'warning'
            })
          }
        }, response => {
          console.log(response)
          // 注册失败
          this.$notify.error({
            title: '错误',
            message: '注册失败!'
          })
        })
      },
      handleBeforeClose(done) {
        this.$emit('closeRegisterDialog')
        this._clearData()
      },
      onUsernameChange() {
        console.log(this.username)
      },
      _clearData() {
        this.username = ''
        this.password = ''
        this.email = ''
//        this.school = ''
//        this.occupation = ''
      }
    },
    watch: {
      dialogVisible(newVal) {
        this.dialogShow = newVal
      }
    },
    computed: {
      showUserPrompt: function () {
        if (this.username.length < 6 && this.username.length !== 0) {
          return 'show-username'
        } else {
          return 'hide-username'
        }
      },
      showPasswordPrompt() {
        if (this.password.length < 6 && this.password.length !== 0) {
          return 'show-password'
        } else {
          return 'hide-password'
        }
      },
      showEmailPrompt() {
        let patt = new RegExp('([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+')
        if (!patt.test(this.email) && this.email.length !== 0) {
          return 'show-email'
        } else {
          return 'hide-email'
        }
      },
      showSchoolPrompt() {
        if (this.school.length < 2 && this.school.length !== 0) {
          return 'show-school'
        } else {
          return 'hide-school'
        }
      },
      showOccupationPrompt() {
        if (this.occupation.length < 2 && this.occupation.length !== 0) {
          return 'show-occupation'
        } else {
          return 'hide-occupation'
        }
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .prompt
    margin-left 10px
    color #FF4949

  .el-form-item
    margin-bottom 10px

  .el-form-item__content
    line-height 22px

  .prompt-username
    &.show-username
      visibility visible
    &.hide-username
      visibility hidden

  .prompt-password
    &.show-password
      visibility visible
    &.hide-password
      visibility hidden

  .prompt-email
    &.show-email
      visibility visible
    &.hide-email
      visibility hidden

  .prompt-school
    &.show-school
      visibility visible
    &.hide-school
      visibility hidden

  .prompt-occupation
    &.show-occupation
      visibility visible
    &.hide-occupation
      visibility hidden

</style>
