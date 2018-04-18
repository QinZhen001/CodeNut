<template>
  <transition name="el-fade-in-linear">
    <div class="welcome">
      <slider ref="slider" :pages="welcomePages" :sliderinit="slider" @mousewheel.native="mouseScroll">
      </slider>
      <div class="welcome-header">
        <span class="welcome-header-title">CodeNut</span>
        <a class="welcome-header-item" href="#" @click="linkToHome">题目</a>
        <a class="welcome-header-item" href="#" @click="linkToselfStudy">学习资料</a>
        <div class="welcome-header-btn register-btn" @click="clickRegisterBtn">注册</div>
        <div class="welcome-header-btn" @click="clickLoginBtn">登录</div>
      </div>
      <div class="bottom-pointer" v-show="slider.currentPage === 0">
        <span class="bottom-pointer-img">↓</span>继续滚动
      </div>
      <transition-group name="el-fade-in">
        <img class="center-img" v-show="slider.currentPage===0" src="static/welcome/welcome_1.png" width="200"
             height="200" :key="slider.currentPage">
        <img class="center-img" v-show="slider.currentPage===1" src="static/welcome/welcome_2.png" width="200"
             height="200" :key="slider.currentPage">
        <img class="center-img" v-show="slider.currentPage===2" src="static/welcome/welcome_3.png" width="200"
             height="200" :key="slider.currentPage">
      </transition-group>
      <el-button class="enter-home-btn" @click="linkToHome" type="success" size="medium">进入主页 <i
        class="el-icon-d-arrow-right"></i></el-button>
      <login-dialog ref="loginDialog">
      </login-dialog>
      <register-dialog ref="registerDialog">
      </register-dialog>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import Slider from 'vue-concise-slider'// 引入slider组件
  import LoginDialog from 'base/logindialog/logindialog'
  import RegisterDialog from 'base/registerdialog/registerdialog'
  import { welcomePages } from 'common/js/data'

  export default{
    data(){
      return {
        welcomePages: welcomePages,
        slider: {
          currentPage: 0,  //当前页码
          thresholdDistance: 200,   //滑动判定距离
          thresholdTime: 150,   //滑动判定时间
          loop: true, //循环滚动
          direction: 'vertical', //方向设置，垂直滚动
          infinite: 1, //无限滚动前后遍历数
          slidesToScroll: 1 //每次滑动项数
        },
        showLoginDialog: false,
        showRegisterDialog: false
      }
    },
    methods: {
      linkToHome(){
        this.$router.replace('/home')
      },
      clickLoginBtn(){
        this.$refs.loginDialog.show()
      },
      clickRegisterBtn(){
        this.$refs.registerDialog.show()
      },
      linkToselfStudy(){
        this.$router.replace('/selfstudy')
      },
      mouseScroll(e){
        // wheelDelta不兼容火狐浏览器
        console.log(e.wheelDelta)
        if (e.wheelDelta < 0) {
          //向下
          this.$refs.slider.$emit('slideNext')
        } else {
          //向上
          this.$refs.slider.$emit('slidePre')
        }
      }
    },
    components: {
      Slider,
      LoginDialog,
      RegisterDialog
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .welcome
    position fixed
    left 0
    right 0
    top 0
    bottom 0
    z-index 100
    .slider-container
      margin 0
      width 100%
      height 100%
    .welcome-header
      position absolute
      top 20px
      left 20px
      width 100%
      z-index 101
      .welcome-header-title
        font-size: 45px
        color whitesmoke
      .welcome-header-item
        margin-left 18px
        text-decoration: none;
        color whitesmoke
        font-size 18px
      .welcome-header-btn
        float right
        margin-top 10px
        margin-right 15px
        display inline-block
        padding 5px 15px
        width 60px
        text-align center
        border-radius 10px
        font-size 18px
        color whitesmoke
        border 1px solid whitesmoke
        &:hover
          cursor: pointer
      .register-btn
        margin-right 30px
    .center-img
      position: absolute
      left 50%
      top 50%
      margin-left: -100px;
      margin-top -250px
      z-index 101
    .bottom-pointer
      position: absolute
      vertical-align: middle
      top: auto
      height 20px
      bottom: 20px
      left: 48%
      z-index 101
      color whitesmoke
      .bottom-pointer-img
        display inline-block
        position relative
        bottom: 2px
    .enter-home-btn
      position: absolute
      bottom: 30px
      right 30px
      width 160px
      height 60px
      font-size 22px
      border-radius 10px
      z-index 101
</style>
