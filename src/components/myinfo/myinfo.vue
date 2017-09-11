<template>
  <transition name="el-zoom-in-top">
    <div>
      <div class="info-title">
        <img width="32" height="32" src="static/info.png" class="img-info"/>
        <p class="text-title">Information</p>
      </div>
      <el-card :body-style="{ padding: '0px' }">
        <img src="static/avatar.jpg" class="image">
        <div class="infoFooter">
          <span class="name" :class="classObject">{{user.username ? user.username : '暂未登录'}}</span>
          <div class="bottom clearfix">
            <time class="time">{{ currentDate }}</time>
            <el-collapse>
              <el-collapse-item title="我的信息" name="1">
                <div class="item-wrapper">
                  <span class="text">邮箱</span>
                  <span class="value" v-show="user.email">{{user.email}}</span>
                </div>
                <div class="item-wrapper">
                  <span class="text">学校</span>
                  <span class="value" v-show="user.school">{{user.school}}</span>
                </div>
                <div class="item-wrapper">
                  <span class="text">职业</span>
                  <span class="value" v-show="user.occupation">{{user.occupation}}</span>
                </div>
                <div class="item-wrapper">
                  <span class="text">公司</span>
                  <span class="value" v-show="user.company">{{user.company}}</span>
                </div>
              </el-collapse-item>
            </el-collapse>
          </div>
        </div>
      </el-card>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import { formatDate } from 'common/js/util'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        currentDate: formatDate(new Date(), 'yyyy-MM-dd hh:mm:ss')
      }
    },
    methods: {},
    computed: {
      ...mapGetters([
        'user'
      ]),
      classObject: function () {
        if (this.user.username) {
          return 'login'
        } else {
          return 'nologin'
        }
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .info-title
    height 65px
    .img-info
      vertical-align: middle
    .text-title
      margin-left 3px
      vertical-align: middle
      display inline-block
      font-size: 20px;
      font-weight: 300;
  .image
    width: 100%
    display: block

  .infoFooter
    padding: 14px
    .name
      display inline-block
      font-size 20px
      font-weight 600
      &.login
        color #13CE66
      &.nologin
        color #FF4949
    .bottom
      margin-top: 13px;
      line-height: 12px;
    .clearfix
      &:before
        display: table;
        content: "";
      &:after
        display: table;
        content: "";
        clear: both
      .time
        float right
        font-size: 13px;
        color: #999;
      .el-collapse
        border: none
        .el-collapse-item__header
          padding-left 0
          border-bottom none
        .el-collapse-item__wrap
          border: none
          background-color: #fff
        .el-collapse-item__content
          padding 0
        .el-collapse-item
          padding 0 5px
          .item-wrapper
            width 100%
            height 30px
            border-bottom 1px solid #ddd
            .text
              margin-left 8px
              display inline-block
              position: relative;
              top: 50%;
              transform: translateY(-50%);
            .value
              display inline-block
              position: relative;
              top: 50%;
              float right
              margin-right 5px
              transform: translateY(-50%);
</style>
