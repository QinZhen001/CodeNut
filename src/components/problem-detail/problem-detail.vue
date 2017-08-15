<template>
  <transition name="slide">
    <div class="detail-wrapper">
      <div class="back" @click="back">
        <i class="icon-back"></i>
      </div>
      <h1 class="title" v-text="title"></h1>
      <scroll :objectdata="problemDetail" :listen-scroll="listenScroll" :probe-type="probeType" class="detail-scroll">
        <div class="scroll-wrapper">
          <div class="description" v-html="problemDetail.description"></div>
          <div class="situation">
            <span>ACCEPTED: {{problemDetail.accepted}}</span>
            <span>SUBMITTED: {{problemDetail.submitted}}</span>
          </div>
        </div>
      </scroll>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import Scroll from 'base/scroll/scroll'
  import Loading from 'base/loading/loading'
  import {mapGetters} from 'vuex'

  export default {
    data() {
      return {
        problemDetail: {}
      }
    },
    created() {
      this._getProblemDetail()
      this.probeType = 3
      this.listenScroll = false
    },
    computed: {
      title() {
        return this.problem.title
      },
      ...mapGetters([
        'problem'
      ])
    },
    methods: {
      back() {
        this.$router.back()
      },
      _getProblemDetail() {
        if (!this.problem.id) {
          this.$router.push('/rank')
          return
        }
        let url = 'http://api.txdna.cn/problems/' + `${this.problem.id}`
        this.$http.get(url).then(response => {
          console.log(response.body)
          this.problemDetail = response.body
        }, response => {
          // error callback
        })
      }
    },
    components: {
      Scroll,
      Loading
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  @import "~common/stylus/mixin"

  .detail-wrapper
    position: fixed
    z-index: 100
    top: 0
    left: 0
    bottom: 0
    right: 0
    background: $color-background
    .back
      position absolute
      top: 0
      left: 6px
      z-index: 50
      .icon-back
        display: block
        padding: 10px
        font-size: $font-size-large-x
        color: $color-theme
    .title
      position: absolute
      top: 0
      left: 10%
      z-index: 40
      width: 80%
      no-wrap()
      text-align: center
      line-height: 40px
      font-size: $font-size-large
      color: $color-text
    .detail-scroll
      position: absolute;
      overflow: hidden
      top: 40px;
      bottom: 0;
      left: 0
      right: 0
      .scroll-wrapper
        padding 0 8px 0 8px
        .description
          p
            margin-top 2px
            margin-bottom 6px
            display: block;
            font-size: 16px
            line-height 16px
            font-weight 200
            text-indent: 8px;
          p:nth-child(2)
            margin-top 0
            color #FFEB3B
        .situation
          margin: 10px auto 0 auto
          text-align: center

  .slide-enter-active, .slide-leave-active
    transition: all 0.3s

  .slide-enter, .slide-leave-to
    transform: translate3d(100%, 0, 0)

</style>
