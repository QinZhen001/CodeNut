<template>
  <transition name="slide">
    <div class="detail-wrapper">
      <div class="back" @click="back">
        <i class="icon-back"></i>
      </div>
      <h1 class="title" v-text="title"></h1>

      <div>
        <loading v-show="problemDetail.id !== problem.id" title="玩命加载中..." class="loading"></loading>
        <scroll :objectdata="problemDetail" :listen-scroll="listenScroll" :probe-type="probeType"
                v-show="problemDetail.id === problem.id" class="detail-scroll">
          <div class="scroll">
            <div class="description" v-html="problemDetail.description" v-if="problemDetail.description"></div>
            <div class="situation" v-if="problemDetail.accepted && problemDetail.submitted">
              <span>ACCEPTED: {{problemDetail.accepted}}</span>
              <span>SUBMITTED: {{problemDetail.submitted}}</span>
            </div>
            <div class="solution" v-if="problemDetail.solution" v-html="problemDetail.solution"></div>
          </div>
        </scroll>
      </div>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import Scroll from 'base/scroll/scroll'
  import Loading from 'base/loading/loading'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        problemDetail: {},
        showLoading: true
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
          this.$router.push('/recommend')
          return
        }
        console.log('problem detail id')
        console.log(this.problem.id)
        let url = 'https://api.txdna.cn/problems/' + `${this.problem.id}`
        this.$http.get(url).then(response => {
          console.log('get problem detail data')
          this.problemDetail = response.body
        }, response => {
          // error callback
        })
      }
    },
    components: {
      Scroll,
      Loading
    },
    watch: {
      problem(newProblem) {
        console.log(newProblem)
      }
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
      margin-right 4px
      width: 80%
      no-wrap()
      text-align: center
      line-height: 40px
      font-size: $font-size-large
      color: #ffd700
    .loading
      margin-top 40px
    .detail-scroll
      position: absolute
      top: 40px
      bottom: 0
      left: 0
      right: 0
      overflow: hidden
      .description
        padding 0 6px
        p
          font-weight 200
          font-size $font-size-large
          margin-bottom 4px
        pre
          margin-bottom 4px
          padding-left 5px
          font-size $font-size-medium
          white-space: pre-wrap;
          white-space: -moz-pre-wrap;
          white-space: -pre-wrap;
          white-space: -o-pre-wrap;
          word-wrap: break-word;
      .situation
        width 100%
        height 60px
        line-height 60px
        text-align center
        font-size $font-size-large
        color deepskyblue
      .solution
        padding 0 6px
        .toc
          display none
        #summary
          display none
        h2
          font-size $font-size-large-x
          color: $color-theme
        p
          font-weight 200
          font-size $font-size-large
          margin-bottom 4px
          strong
            font-size $font-size-large-x
            color: $color-theme
          script
            type = "text/javascript"
        .codehilite
          pre
            margin-bottom 4px
            padding-left 5px
            font-size $font-size-medium
            white-space: pre-wrap;
            white-space: -moz-pre-wrap;
            white-space: -pre-wrap;
            white-space: -o-pre-wrap;
            word-wrap: break-word;

  .slide-enter-active, .slide-leave-active
    transition: all 0.3s

  .slide-enter, .slide-leave-to
    transform: translate3d(100%, 0, 0)

</style>
