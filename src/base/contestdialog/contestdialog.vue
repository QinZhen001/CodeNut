<template>
  <el-dialog
    title="提示"
    :visible.sync="visible">
    <span class="contest-dialog-title">是否要加入{{contest.sponsor}}举办的 “{{contest.title}}” 比赛?</span>
    <div class="password-wrapper">
      <span class="password-text">密码:</span>
      <el-input class="password-input" v-model="password" placeholder="请输入比赛密码" size="small"></el-input>
    </div>
    <span slot="footer" class="dialog-footer">
    <el-button @click="hide">取 消</el-button>
    <el-button type="primary" @click="comfirmContest">确 定</el-button>
        </span>
  </el-dialog>
</template>

<script type="text/ecmascript-6">
  import { baseUrl, MSG_OK, MSG_NO } from 'common/js/data'
  import axios from 'axios'

  export default{
    props: {
      contest: {
        type: Object
      }
    },
    data(){
      return {
        visible: false,
        password: ''
      }
    },
    methods: {
      show(){
        this.visible = true
      },
      hide(){
        this.visible = false
        this.password = ''
      },
      clearData(){
        this.password = ''
      },
      comfirmContest(){
        let url = `${baseUrl}/contests/${this.chooseContest.id}/users`
        axios.post(url, {
          password: this.password
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.contestDialogVisible = false
            this.$notify({
              title: '成功',
              message: '参加比赛成功！',
              type: 'success'
            })
            this.password = ''
          } else if (response.data.msg === MSG_NO) {
            this.$notify({
              title: '失败',
              message: `${response.data.error}`,
              type: 'error'
            })
          }
        }, response => {})
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .el-dialog
    .el-dialog__body
      padding 10px 20px
      .contest-dialog-title
        font-size 18px
        font-weight 400
      .password-wrapper
        margin-top 15px
        .password-text
          font-size 16px
          font-weight 300
        .password-input
          margin-left 3px
          width 60%
</style>
