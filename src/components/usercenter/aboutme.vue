<template>
  <div class="about-me">
    <el-dialog title="关于我" :visible.sync="dialogVisible" @open="openDialog">
      <el-input v-model.trim.lazy="aboutMe"
                type="textarea"
                spellcheck="false" auto-complete="off"
                :autosize="{ minRows: 2, maxRows: 4}"
                placeholder="请输入自我介绍(不得超过50字)">
      </el-input>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveAboutMe">保 存</el-button>
      </div>
    </el-dialog>

    <div class="panel">
      <div class="panel-heading">
        <h3 class="panel-title">About Me</h3>
        <img src="static/modify.png" width="22" height="22" class="panel-title-img" @click="openAboutMeDialog">
      </div>
      <div class="panel-body">
        <p class="about-me-text">
          {{user.about_me}}</p>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { mapGetters, mapMutations } from 'vuex'
  import axios from 'axios'
  import { baseUrl, MSG_OK } from 'common/js/data'

  export default{
    data() {
      return {
        dialogVisible: false,
        aboutMe: ''
      }
    },
    methods: {
      openDialog() {
        this.aboutMe = this.user.about_me
      },
      saveAboutMe() {
        // 保存用户信息about_me 到服务器
        let url = `${baseUrl}/users/info`
        axios.put(url, {
          'about_me': this.aboutMe
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            // 保存用户信息到 vuex
            this.saveUserToVuex()
            // 关闭dialog
            this.dialogVisible = false
          }
        }, response => {
          this.saveAboutMe()
        })
      },
      openAboutMeDialog() {
        this.dialogVisible = true
      },
      saveUserToVuex() {
        let user = {}
        user.user_id = this.user.user_id
        user.username = this.user.username
        user.realname = this.user.realname
        user.profile = this.user.profile
        user.school = this.user.school
        user.about_me = this.aboutMe
        user.role = this.user.role
        user.accept_nums = this.user.accept_nums
        user.submit_nums = this.user.submit_nums
        user.tag = this.user.tag
        this.setUser(user)
      },
      ...mapMutations({
        setUser: 'SET_USER'
      })
    },
    computed: {
      ...mapGetters([
        'user'
      ])
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .about-me
    margin-top 20px
    .panel
      border-radius: 5px
      border 1px solid #ddd
      margin-bottom: 20px;
      background-color: #F5F5F5
      -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
      box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
    .panel-heading
      padding: 10px 15px;
      background-color: #ddd;
      border-bottom 1px solid #ddd;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      .panel-title
        display inline-block
        vertical-align bottom
        margin-top: 0;
        margin-bottom: 0;
        font-size: 16px;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.1
      .panel-title-img
        vertical-align bottom
        float right
        position: relative
        &:hover
          cursor pointer
        &:before
          content: ''
          position: absolute
          top: -10px
          left: -10px
          right: -10px
          bottom: -10px
    .panel-body
      padding: 15px;
      .about-me-text
        margin 5px 0
        font-size 16px
        word-wrap: break-word;
        word-break: normal;
</style>
