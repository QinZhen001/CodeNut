<template>
  <div class="breakthrough">
    <canvas id="canvas" class="canvas"></canvas>
    <img src="static/breakthrough/people.png" @click="clickItem($refs.people)" ref="people" class="people"
         width="48" height="48">
    <div class="planet-wrapper planet-simple-1-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetSimple1)" ref="planetSimple1"
           class="planet-simple-1"
           width="120" height="120">
      <span class="planet-text">简单难度</span>
    </div>
    <div class="planet-wrapper planet-simple-2-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetSimple2)" ref="planetSimple2"
           class="planet-simple-2"
           width="120" height="120">
      <span class="planet-text">简单难度</span>
    </div>

    <div class="planet-wrapper planet-middle-1-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetMiddle1)" ref="planetMiddle1"
           class="planet-middle-1"
           width="120" height="120">
      <span class="planet-text">冒险难度</span>
    </div>
    <div class="planet-wrapper planet-middle-2-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetMiddle2)" ref="planetMiddle2"
           class="planet-middle-2"
           width="120" height="120">
      <span class="planet-text">冒险难度</span>
    </div>

    <div class="planet-wrapper planet-hard-1-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetHard1)" ref="planetHard1"
           class="planet-hard-1"
           width="120" height="120">
      <span class="planet-text">地狱难度</span>
    </div>
    <div class="planet-wrapper planet-hard-2-wrapper">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetHard2)" ref="planetHard2"
           class="planet-hard-2"
           width="120" height="120">
      <span class="planet-text">地狱难度</span>
    </div>

    <div class="planet-wrapper planet-boss">
      <img src="static/breakthrough/planet.png" @click="clickItem($refs.planetBoss)" ref="planetBoss"
           class="planetBoss"
           width="120" height="120">
      <span class="planet-text">BOSS</span>
    </div>

    <div class="city"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { getAbsPosition } from 'common/js/util'
  import Stars from 'common/js/Star'
  import Moon from 'common/js/Moon'
  import Meteor from 'common/js/Meteor'
  import Path from 'common/js/Path'

  export default{
    mounted() {
      let canvas = document.getElementById('canvas'),
        ctx = canvas.getContext('2d'),
        width = window.innerWidth,
        height = window.innerHeight,
        // 实例化月亮和星星。流星是随机时间生成，所以只初始化数组
        stars = new Stars(ctx, width, height, 200),
        moon = new Moon(ctx, width, height),
        path = new Path(ctx, 144.1875, 760, 450, 653),
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
        path.draw()
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
    },
    methods: {
      clickItem(ele) {
        let position = getAbsPosition(ele)
        console.log(position)
      }
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
    width 100%
    height 100%
    z-index 10
    babackground: rgba(7, 17, 27, 0.95);
    .canvas
      z-index: -1;
      position: fixed
    .people
      position relative
      top 80%
      left 10%
      z-index 1
      animation: myfirst 5s linear;
    .planet-wrapper
      position absolute
      width 128px
    .planet-simple-1-wrapper
      top 400px
      left 220px
    .planet-simple-2-wrapper
      bottom 150px
      left 450px
    .planet-middle-1-wrapper
      bottom 590px
      left 479px
    .planet-middle-2-wrapper
      bottom 253px
      left 754px
    .planet-hard-1-wrapper
      top 50px
      left 879px
    .planet-hard-2-wrapper
      bottom 353px
      right 560px
    .planet-boss
      top 100px
      right 100px

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

  @keyframes myfirst
    from
      margin-top: 10px
    to
      margin-bottom: 10px


</style>
