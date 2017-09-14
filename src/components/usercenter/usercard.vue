<template>
  <div>
    <div class="panel">
      <div class="panel-heading">
        <h3 class="panel-title">Basic profile</h3>
      </div>
      <div class="panel-body">
        <img width="77" height="77" src="static/avatar.jpg" class="avatar">
        <h4 class="username">username</h4>
        <p class="email">邮箱: qz519189636@qq.com</p>
        <p class="occupation">职业: 码农</p>
        <div class="panel-body-left">
          <p class="company">公司: 广东XX科技有限公司</p>
          <p class="school">毕业学校: 五邑大学</p>
          <el-rate v-model="score" disabled=true disabled-void-color='#ddd'>
          </el-rate>
          <el-tag type="warning" v-text="calcGrade"></el-tag>
        </div>
        <div class="panel-body-bottom">
          <el-tag :key="tag" v-for="(tag,index) in dynamicTags" :closable="true" @close="handleCloseTag(tag)"
                  hit=true :type="calcType(index)">{{tag}}
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
  export default {
    data() {
      return {
        score: 3,
        inputValue: '',
        dynamicTags: ['阳光', '帅气', '完美主义者', '自信'],
        inputVisible: false
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
      }
    },
    computed: {
      calcGrade() {
        return `等级${this.score}`
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
        margin-top: 0;
        margin-bottom: 0;
        font-size: 16px;
        color: inherit;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.1;
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
        font-size: 18px;
        margin-top: 10px;
        margin-bottom: 10px;
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
