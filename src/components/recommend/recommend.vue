<template>
  <div class="recommend" ref="recommend">
    <scroll
      :data="problems"
      :pullup="pullup"
      :beforeScroll="beforeScroll"
      @scrollToEnd="loadMore"
      @scroll="scroll"
      :listen-scroll="listenScroll" :probe-type="probeType"
      ref="scroll" class="recommend-content">
      <div>
        <div v-if="sliders.length" class="slider-wrapper">
          <div class="slider-content">
            <slider ref="slider">
              <div v-for="item in sliders">
                <a :hre="item.linkUrl">
                  <img class="needsclick" @load="loadImage" :src="item.picUrl">
                </a>
              </div>
            </slider>
          </div>
        </div>

        <div class="problem-list">
          <h1 class="list-title">热门问题推荐</h1>
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
            <loading v-show="hasMore" title="加载中..."></loading>
          </ul>
          <div v-show="!hasMore && !problems.length" class="no-result-wrapper">
            <no-result title="抱歉，暂无搜索结果"></no-result>
          </div>
        </div>
      </div>
    </scroll>

    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import Slider from 'base/slider/slider'
  import Loading from 'base/loading/loading'
  import Scroll from 'base/scroll/scroll'
  import { playlistMixin } from 'common/js/mixin'
  import { mapMutations } from 'vuex'
  import { sliderItems } from 'common/js/data'
  import NoResult from 'base/no-result/no-result'

  const PER_PAGE = 10

  export default {
    mixins: [playlistMixin],
    data() {
      return {
        recommends: [],
        discList: [],
        problems: [],
        scrollY: 0,
        page: 1,
        pullup: true,
        beforeScroll: true,
        hasMore: true
      }
    },
    created() {
      this.sliders = sliderItems
      this.probeType = 3
      this.listenScroll = false
      console.log(this.sliders)
      this._getProblemList()
    },
    activated() {
      setTimeout(() => {
        this.$refs.slider && this.$refs.slider.refresh()
      }, 20)
    },
    methods: {
      handlePlaylist(playlist) {
        const bottom = playlist.length > 0 ? '60px' : ''
        this.$refs.recommend.style.bottom = bottom
        this.$refs.scroll.refresh()
      },
      loadImage() {
        if (!this.checkloaded) {
          this.checkloaded = true
          setTimeout(() => {
            this.$refs.scroll.refresh()
          }, 20)
        }
      },
      selectItem(item) {
        this.$router.push({
          path: `/problem/${item.id}`
        })
        this.setProblem(item)
      },
      _getProblemList() {
        // 今天没有引入 vue-resourse 明天记得
        let url = 'http://api.txdna.cn/problems?page=' + this.page + '&per_page=' + PER_PAGE
        this.$http.get(url).then(response => {
          console.log(response.body)
          this.problems = this.problems.concat(response.body)
        }, response => {
          console.log(response)
        })
      },
      scroll(pos) {
        this.scrollY = pos.y
      },
      loadMore() {
        console.log('loadMore')
        this.page++
        this._getProblemList()
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    },
    components: {
      Slider,
      Loading,
      Scroll,
      NoResult
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"

  .recommend
    position: fixed
    width: 100%
    top: 88px
    bottom: 0
    .recommend-content
      height: 100%
      overflow: hidden
      .slider-wrapper
        position: relative
        width: 100%
        height: 0
        padding-top: 40%
        overflow: hidden
        .slider-content
          position: absolute
          top: 0
          left: 0
          width: 100%
          height: 100%
      .problem-list
        .list-title
          height: 65px
          line-height: 65px
          text-align: center
          font-size: $font-size-medium
          color: $color-theme
        .item
          position: relative
          display: flex
          align-items: center
          padding: 15px 0 15px 20px
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
      .no-result-wrapper
        position: absolute
        width: 100%
        top 50%
        transform translateY(-50%)
</style>
