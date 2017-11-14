<template>
  <transition name="el-fade-in-linear">
    <div class="welcome" v-show="showFrag">
      <slider :pages="mypages" :sliderinit="slider">
      </slider>
      <div class="welcome-header">
        <span class="welcome-header-title">CodeNut</span>
        <a class="welcome-header-item" href="#" @click="linkToHome">题目</a>
        <a class="welcome-header-item" href="#" @click="linkToselfStudy">学习资料</a>
        <div class="welcome-header-btn register-btn" @click="clickRegisterBtn">注册</div>
        <div class="welcome-header-btn" @click="clickLoginBtn">登录</div>
      </div>
      <div class="bottom-pointer" v-show="slider.currentPage === 0">↓继续滚动</div>
      <transition-group name="el-fade-in">
        <img class="center-img" v-show="slider.currentPage===0" src="static/welcome/welcome_1.png" width="256"
             height="256" :key="slider.currentPage">
        <img class="center-img" v-show="slider.currentPage===1" src="static/welcome/welcome_2.png" width="256"
             height="256" :key="slider.currentPage">
        <img class="center-img" v-show="slider.currentPage===2" src="static/welcome/welcome_3.png" width="256"
             height="256" :key="slider.currentPage">
      </transition-group>
      <el-button class="enter-home" @click="linkToHome" type="success" size="medium">进入主页<i
        class="el-icon-d-arrow-right"></i></el-button>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import slider from 'vue-concise-slider'// 引入slider组件

  export default{
    data(){
      return {
        mypages: [
          {
            title: '邑大人自己的Online Judge平台',
            style: {
              background: '#409EFF'
            }
          },
          {
            title: '打造舒适的在线编程体验',
            style: {
              background: '#FA5555'
            }
          },
          {
            title: '一步一步，逐渐掌握知识技能',
            style: {
              background: '#EB9E05'
            }
          }
        ],
        slider: {
          currentPage: 0,  //当前页码
          thresholdDistance: 200,   //滑动判定距离
          thresholdTime: 150,   //滑动判定时间
          loop: true, //循环滚动
          direction: 'vertical', //方向设置，垂直滚动
          infinite: 1, //无限滚动前后遍历数
          slidesToScroll: 1 //每次滑动项数
        },
        showFrag: true
      }
    },
    methods: {
      linkToHome(){
        this.showFrag = false
      },
      clickLoginBtn(){
        this.$emit('clickLogin')
      },
      clickRegisterBtn(){
        this.$emit('clickRegister')
      },
      linkToselfStudy(){
        this.showFrag = false
        this.$emit('linkToselfStudy')
      }
    },
    components: {
      slider
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
      top 20%
      margin-left: -128px;
      z-index 101
    .bottom-pointer
      position: absolute
      top: auto
      bottom: 20px
      left: 48%
      z-index 101
      color whitesmoke
    .enter-home
      position: absolute
      bottom: 30px
      right 30px
      width 160px
      height 60px
      font-size 22px
      border-radius 10px
      z-index 101
</style>
