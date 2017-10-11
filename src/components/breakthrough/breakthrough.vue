<template>
  <div class="breakthrough">
    <canvas id="canvas" class="canvas"></canvas>
    <img class="people" src="static/breakthrough/people.png" @click="clickItem($refs.people)" ref="people"
         width="48" height="48">
    <div class="planet-wrapper planet-simple-1-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetSimple1)" ref="planetSimple1"
           class="planet-simple-1"
           width="140" height="120">
      <span class="planet-text">简单难度</span>
    </div>
    <div class="planet-wrapper planet-simple-2-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetSimple2)" ref="planetSimple2"
           class="planet-simple-2"
           width="140" height="120">
      <span class="planet-text">简单难度</span>
    </div>

    <div class="planet-wrapper planet-middle-1-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetMiddle1)" ref="planetMiddle1"
           class="planet-middle-1"
           width="140" height="120">
      <span class="planet-text">冒险难度</span>
    </div>
    <div class="planet-wrapper planet-middle-2-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetMiddle2)" ref="planetMiddle2"
           class="planet-middle-2"
           width="140" height="120">
      <span class="planet-text">冒险难度</span>
    </div>

    <div class="planet-wrapper planet-hard-1-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetHard1)" ref="planetHard1"
           class="planet-hard-1"
           width="140" height="120">
      <span class="planet-text">地狱难度</span>
    </div>
    <div class="planet-wrapper planet-hard-2-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetHard2)" ref="planetHard2"
           class="planet-hard-2"
           width="140" height="120">
      <span class="planet-text">地狱难度</span>
    </div>

    <div class="planet-wrapper planet-boss">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetBoss)" ref="planetBoss"
           class="planetBoss"
           width="140" height="120">
      <span class="planet-text">BOSS</span>
    </div>

    <div class="city"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  // import { getAbsPosition } from 'common/js/util'
  import Stars from 'common/js/Star'
  import Moon from 'common/js/Moon'
  import Meteor from 'common/js/Meteor'
  //import { getChallengeInfo } from 'common/js/cache'
  import { mapMutations } from 'vuex'
  import { slides } from 'common/js/data'
  import Problem from 'common/js/problem'

  export default{
    data(){
      return {
        challenges: [],
        problems: []
      }
    },
    created(){
      this.problems = slides
    },
    mounted() {
      let canvas = document.getElementById('canvas'),
        ctx = canvas.getContext('2d'),
        width = window.innerWidth,
        height = window.innerHeight,
        // 实例化月亮和星星。流星是随机时间生成，所以只初始化数组
        stars = new Stars(ctx, width, height, 200),
        moon = new Moon(ctx, width, height),
        // path = new Path(ctx, 144.1875, 760, 450, 653),
        meteors = [],
        count = 0
      canvas.width = width
      canvas.height = height
      const meteorGenerator = () => {
        // x位置偏移，以免经过月亮
        let x = Math.random() * width + 800
        meteors.push(new Meteor(ctx, x, height))
        // 每隔随机时间，生成新流星
        setTimeout(() => {
          meteorGenerator()
        }, Math.random() * 2000)
      }
      const frame = () => {
        count++
        //&& 左边count % 10 === 0成立 右边 stars.blink()才会执行
        count % 10 === 0 && stars.blink()
        moon.draw()
        stars.draw()
        //path.draw()
        meteors.forEach((meteor, index, arr) => {
          // 如果流星离开视野之内，销毁流星实例，回收内存
          if (meteor.flow()) {
            meteor.draw()
          } else {
            arr.splice(index, 1)
          }
        })
        requestAnimationFrame(frame)
      }
      meteorGenerator()
      frame()
      //this.challenges = getChallengeInfo()
    },
    methods: {
      clickItem(ele) {
        // let position = getAbsPosition(ele)
//        if (ele.className.includes('simple') && this.challenges[0] === false) {
//          console.log(ele.className)
//        } else if (ele.className.includes('middle')) {
//          if (this.challenges[1] === false && this.challenges[0] === true) {
//            //通过了简单难度 还没有通过冒险难度
//          } else {
//          }
//        } else if (ele.className.includes('hard')) {}
        let index = parseInt(Math.random() * 5)
        this.setProblem(new Problem({id: this.problems[index].linkProblemId}))
        this.$router.push('/home/problem')
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .breakthrough
    position fixed
    left 0
    top 0
    bottom 0
    right 0
    z-index 10
    babackground: rgba(7, 17, 27, 0.95);
    .canvas
      z-index: -1;
      position: fixed
    .people
      position absolute
      top 10%
      left 10%
      z-index 1
    .planet-wrapper
      position relative
      width 128px
      animation: shake_up_down 3s ease-in-out;
      animation-iteration-count: infinite;
      &:hover
        cursor pointer
    .planet-simple-1-wrapper
      top 10%
      left 20%
    .planet-simple-2-wrapper
      top 16%
      left 26%
    .planet-middle-1-wrapper
      top 20%
      left 40%
    .planet-middle-2-wrapper
      top -30%
      left 40%
    .planet-hard-1-wrapper
      top 0
      left 62%
    .planet-hard-2-wrapper
      top -66%
      left 60%
    .planet-boss
      top -66%
      left 80%

  .city
    width: 100%;
    height: 170px;
    position: fixed;
    bottom: 0px;
    z-index: 100;
    background: url('../../../static/breakthrough/city.png') no-repeat;
    background-size: cover;

  .planet-text
    font-size 16px
    text-align: center
    color #ffcd32
    display block

  @keyframes shake_up_down
    0%
      margin-bottom 0
    50%
      margin-bottom: 5px
    100%
      margin-bottom 0


</style>
