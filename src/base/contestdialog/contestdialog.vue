<template>
  <el-dialog
    title="提示"
    :visible.sync="visible">
    <el-form>
      <el-form-item class="dialog-item">
        <p class="text">是否要加入{{contest.sponsor}}举办的  “{{contest.title}}”  比赛?</p>
      </el-form-item>
      <el-form-item class="dialog-item" label="密码:" :label-width="formLabelWidth">
        <el-input class="password-input" v-model="password" placeholder="请输入比赛密码(可以为空)" size="small"></el-input>
      </el-form-item>
    </el-form>
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
        password: '',
        formLabelWidth: '50px'
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
        let url = `${baseUrl}/contests/${this.contest.id}/users`
        axios.post(url, {
          password: this.password
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.$notify({
              title: '成功',
              message: '参加比赛成功！',
              type: 'success'
            })
            this.hide()
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
  .dialog-item
    margin-bottom 10px
    .text
      margin 0 0 0 5px
      font-size 20px
      line-height 20px
</style>
