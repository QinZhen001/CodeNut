<template>
  <div>
    <el-dialog title="修改信息" :visible.sync="dialogFormVisible" @open="openDialog">
      <el-form>
        <el-form-item label="邮箱:" label-width="80px">
          <el-input v-model.trim.lazy="email" auto-complete="off" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="职业:" label-width="80px">
          <el-input v-model.trim.lazy="occupation" auto-complete="off" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="公司:" label-width="80px">
          <el-input v-model.trim.lazy="company" auto-complete="off" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="毕业学校:" label-width="80px">
          <el-input v-model.trim.lazy="school" auto-complete="off" spellcheck="false"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveUserInfo">保 存</el-button>
      </div>
    </el-dialog>
    <div class="panel">
      <div class="panel-heading">
        <h3 class="panel-title">Basic profile</h3>
        <img src="static/modify.png" width="22" height="22" class="panel-title-img" @click="showDialog">
      </div>
      <div class="panel-body">
        <img width="77" height="77" src="static/avatar.jpg" class="avatar">
        <h4 class="username">{{user.username}}</h4>
        <p class="email">邮箱: {{user.email}}</p>
        <p class="occupation">职业: {{user.occupation}}</p>
        <div class="panel-body-left">
          <p class="company">公司: {{user.company}}</p>
          <p class="school">毕业学校: {{user.school}}</p>
          <el-rate v-model="score" :disabled=true disabled-void-color="#ddd">
          </el-rate>
          <el-tag type="warning" v-text="calcGrade"></el-tag>
        </div>
        <div class="panel-body-bottom">
          <el-tag :key="tag" v-for="(tag,index) in dynamicTags" :closable="true" @close="handleCloseTag(tag)"
                  :hit=true :type="calcType(index)">{{tag}}
          </el-tag>
          <el-input
            class="input-tag"
            v-if="inputVisible"
            v-model="inputValue"
            ref="saveTagInput"
            size="mini"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm">
          </el-input>
          <el-button v-else class="button-tag" size="small" @click="showInput">+ 标签</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { mapGetters, mapMutations } from 'vuex'
  import axios from 'axios'

  export default {
    data() {
      return {
        score: 3,
        inputValue: '',
        dynamicTags: ['阳光', '帅气', '完美主义者', '自信'],
        inputVisible: false,
        dialogFormVisible: false,
        email: '',
        occupation: '',
        company: '',
        school: ''
      }
    },
    methods: {
      handleCloseTag(tag) {
        this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1)
      },
      handleInputConfirm() {
        let inputValue = this.inputValue
        if (inputValue) {
          this.dynamicTags.push(inputValue)
        }
        this.inputVisible = false
        this.inputValue = ''
      },
      showInput() {
        this.inputVisible = true
        this.$nextTick(() => {
          this.$refs.saveTagInput.$refs.input.focus()
        })
      },
      calcType(index) {
        if (index % 3 === 0) {
          return 'primary'
        } else if (index % 3 === 1) {
          return 'success'
        } else if (index % 3 === 2) {
          return 'danger'
        }
      },
      showDialog() {
        this.dialogFormVisible = true
      },
      openDialog() {
        this.email = this.user.email
        this.occupation = this.user.occupation
        this.company = this.user.company
        this.school = this.user.school
      },
      saveUserInfo() {
        // 保存用户信息到服务器
        let url = `https://api.txdna.cn/users/${this.user.id}`
        axios.put(url, {
          'email': this.email,
          'occupation': this.occupation,
          'company': this.company,
          'school': this.school
        }).then(response => {
          if (response.data.msg === 'ok') {
            // 成功
            console.log(response)
            // 保存用户信息到 vuex
            this.saveUserToVuex()
            // 关闭dialog
            this.dialogFormVisible = false
          }
        }, response => {
          this.saveUserInfo()
        })
      },
      saveUserToVuex() {
        let user = {}
        user.id = this.user.id
        user.username = this.user.username
        user.realname = this.user.realname
        user.about_me = this.user.about_me
        user.profile = this.user.profile

        user.email = this.email
        user.school = this.school
        user.occupation = this.occupation
        user.company = this.company
        this.setUser(user)
      },
      ...mapMutations({
        setUser: 'SET_USER'
      })
    },
    computed: {
      calcGrade() {
        return `等级${this.score}`
      },
      ...mapGetters([
        'user'
      ])
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">

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
        vertical-align: bottom;
        margin-top: 0;
        margin-bottom: 0;
        font-size: 16px;
        color: inherit;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.1;
      .panel-title-img
        vertical-align bottom
        float right
        position: relative
        &:before
          content: ''
          position: absolute
          top: -10px
          left: -10px
          right: -10px
          bottom: -10px
    .panel-body
      padding: 15px;
      p
        margin 6px 0
      .avatar
        float: left;
        margin-right: 15px;
        margin-top: 5px;
        border-radius: 6px;
      .username
        max-width: 240px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: middle;
        font-size: 20px;
        margin-bottom: 5px;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.1;
        color: inherit;
      .email occupation
        max-width: 240px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: middle;
        margin: 0 0 10px;
      .panel-body-left
        padding-left 90px
        .company school
          max-width: 240px;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          vertical-align: middle;
          margin: 0 0 10px;
        .el-rate
          display inline-block
      .panel-body-bottom
        padding: 0 12px 12px 12px;
        .el-tag
          margin-top 12px
          margin-right 8px
        .button-tag
          height: 25px;
          line-height: 22px;
          padding-top: 0;
          padding-bottom: 0;
        .input-tag
          position: relative;
          font-size: 10px;
          height: 30px;
          line-height: 22px;
          display: inline-block;
          width 54px
          white-space: nowrap;

</style>
