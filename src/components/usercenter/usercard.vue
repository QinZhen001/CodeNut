<template>
  <div>
    <el-dialog title="修改信息" :visible.sync="dialogFormVisible" @open="openDialog">
      <el-form>
        <el-form-item label="真实姓名:" label-width="80px">
          <el-input v-model.trim.lazy="realname" auto-complete="off" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="所在学校:" label-width="80px">
          <el-input v-model.trim.lazy="school" auto-complete="off" spellcheck="false"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveUserInfoToServer">保 存</el-button>
      </div>
    </el-dialog>
    <div class="panel">
      <div class="panel-heading">
        <h3 class="panel-title">Basic profile</h3>
        <img src="static/modify.png" width="22" height="22" class="panel-title-img" @click="showDialog">
      </div>
      <div class="panel-body">
        <img width="77" height="77" src="static/avatar.jpg" class="avatar">
        <P class="username">{{user.username}}</P>
        <p class="realname">真实姓名: {{user.realname}}</p>
        <p class="school">毕业学校: {{user.school}}</p>
        <div class="panel-body-left">
          <el-rate v-model="score" :disabled=true disabled-void-color="#ddd">
          </el-rate>
          <el-tag type="warning" v-text="calcGrade"></el-tag>
        </div>
        <div class="panel-body-bottom">
          <el-tag :key="tag" v-for="(tag,index) in dynamicTags" :closable="true" @close="closeTag(tag)"
                  :hit=true :type="calcType(index)">{{tag}}
          </el-tag>
          <el-input
            class="input-tag"
            v-if="inputVisible"
            v-model="inputValue"
            ref="saveTagInput"
            size="mini"
            @keyup.enter.native="inputConfirm"
            @blur="inputConfirm">
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
  import { baseUrl, MSG_OK } from 'common/js/data'
  import User from 'common/js/user'

  export default {
    data() {
      return {
        score: 3,
        inputValue: '',
        //dynamicTags: ['阳光', '帅气', '完美主义者', '自信'],
        dynamicTags: [],
        inputVisible: false,
        dialogFormVisible: false,
        school: '',
        realname: ''
      }
    },
    created() {
      this.dynamicTags = this.StringToArray(this.user.tag)
    },
    methods: {
      closeTag(tag) {
        this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1)
        // 保存到服务器
        this._saveUserTagToServer()
      },
      inputConfirm() {
        let inputValue = this.inputValue
        if (inputValue) {
          this.dynamicTags.push(inputValue)
          // 保存到服务器
          this._saveUserTagToServer()
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
        this.realname = this.user.realname
        this.school = this.user.school
      },
      saveUserInfoToServer() {
        // 保存用户信息到服务器
        let url = `${baseUrl}/users/info`
        axios.put(url, {
          'realname': this.realname,
          'school': this.school
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            // 成功
            console.log(response)
            // 同时保存用户信息到 vuex
            this._saveUserToVuex()
            // 关闭dialog
            this.dialogFormVisible = false
          }
        }, response => {
          this.saveUserInfoToServer()
        })
      },
      _saveUserTagToServer() {
        // 保存用户标签到服务器
        let url = `${baseUrl}/users/info`
        axios.put(url, {
          'tag': this._arrayToString(this.dynamicTags)
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            // 成功
            console.log(response)
            // 同时用户信息到 vuex
            this._saveUserToVuex()
            // 关闭dialog
            this.dialogFormVisible = false
          }
        }, response => {
          this._saveUserTagToServer()
        })
      },
      _saveUserToVuex() {
        let user = new User({
          realname: this.realname,
          school: this.school,
          tag: this._arrayToString(this.dynamicTags),
          user_id: this.user.user_id,
          username: this.user.username,
          profile: this.user.profile,
          about_me: this.user.about_me,
          role: this.user.role,
          accept_nums: this.user.accept_nums,
          submit_nums: this.user.submit_nums
        })
        this.setUser(user)
      },
      _arrayToString(arr) {
        let str = ''
        for (let item of arr) {
          console.log(item)
          str = str + item + ','
        }//结果：1,2,234,sdf,-2 遍历了数组arr的值
        str = str.substring(0, str.length - 1)
        console.log(str)
        return str
      },
      StringToArray(str) {
        let arr = []
        arr = str.split(',')
        // 在每个逗号(,)处进行分解。
        return arr
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
    },
    watch: {
      user: function (newUser) {
        if (newUser.user_id == null) {
          this.$router.push('/home')
        }
      }
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
      p
        margin 6px 0
      .avatar
        float: left;
        margin-right: 15px;
        margin-top: 5px;
        border-radius: 6px;
      .username
        margin 0 0
        max-width: 240px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: middle;
        font-size: 22px;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.2;
        color: inherit;
      .realname school
        margin: 0 0 10px;
        vertical-align: middle;
        max-width: 240px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        font-weight: 500;
      .panel-body-left
        padding-left 50px
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
