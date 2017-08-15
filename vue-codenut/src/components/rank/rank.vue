<template>
  <div class="problem">
    <scroll :data="problems" @scroll="scroll"
            :listen-scroll="listenScroll" :probe-type="probeType" class="list" ref="list">
      <ul>
        <li class="item" v-for="item in problems" @click.stop="selectItem(item)">
          <img width="57" height="57" src="../../common/image/default.png">

          <div class="content">
            <h2 class="problem-title">{{item.title}}</h2>
            <div class="star-wrapper">
              <span class="text">难度系数:</span>
              <star :score="item.level"></star>
            </div>

            <div class="tag-wrapper">
              <span class="tag">{{item.tag}}</span>
            </div>
          </div>

        </li>
      </ul>
    </scroll>
    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import Star from 'base/star/star'
  import Scroll from 'base/scroll/scroll'
  import {mapMutations} from 'vuex'

  export default {
    data() {
      return {
        problems: [],
        scrollY: 0
      }
    },
    created() {
      this.probeType = 3
      this.listenScroll = false
      this._getdata()
    },
    methods: {
      scroll(pos) {
        this.scrollY = pos.y
      },
      _getdata() {
        this.$http.get('http://api.txdna.cn/problems?start=1&end=20').then(response => {
          console.log(response.body)
          let result = []
          for (let item of response.body) {
            result.push(item)
          }
          this.problems = result
        }, response => {
          // error callback
        })
      },
      selectItem(item) {
        this.$router.push({
          path: `/rank/${item.id}`
        })
        this.setProblem(item)
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    },
    components: {
      Scroll,
      Star
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  @import "~common/stylus/mixin"

  .problem
    position: fixed
    top: 88px
    bottom: 0
    width: 100%

  .list
    position: relative
    width: 100%
    height: 100%
    overflow: hidden
    background: $color-background
    .item
      position: relative
      display: flex
      align-items: center
      padding: 15px 0 15px 30px
      border-bottom 1px solid red
    .content
      position relative
      width 100%
      margin-left 30px
    .problem-title
      color: $color-text-l
      font-size: $font-size-medium-x
      font-weight 200
    .star-wrapper
      margin 3px 0
      font-size: 0
      .text
        display: inline-block
        line-height: 18px
        font-size: 14px
        vertical-align: center
      .star
        display: inline-block
        margin-left 3px
        vertical-align: center

    .tag-wrapper
      position: absolute
      right: 12px
      padding: 0 8px
      height: 24px
      line-height: 24px
      border-radius: 14px
      background: rgba(0, 0, 0, 0.2)
      text-align: center
      .tag
        font-size: 10px
</style>
