<template>
  <scroll ref="suggest"
          class="suggest"
          :data="result"
          :pullup="pullup"
          :beforeScroll="beforeScroll"
          @beforeScroll="listScroll"
  >
    <ul class="suggest-list">
      <li @click="selectItem(item)" class="suggest-item" v-for="item in result">
        <div class="icon">
          <i class="icon-mine"></i>
        </div>
        <div class="name">
          <p class="text">{{item.title}}</p>
        </div>
      </li>
      <loading v-show="!result" title=""></loading>
    </ul>
    <div v-show="!result && !result.length" class="no-result-wrapper">
      <no-result title="抱歉，暂无搜索结果"></no-result>
    </div>
  </scroll>
</template>

<script type="text/ecmascript-6">
  import Scroll from 'base/scroll/scroll'
  import Loading from 'base/loading/loading'
  import NoResult from 'base/no-result/no-result'
  import { createSong } from 'common/js/song'
  import { mapMutations, mapActions } from 'vuex'

  export default {
    props: {
      showSinger: {
        type: Boolean,
        default: true
      },
      query: {
        type: String,
        default: ''
      }
    },
    data() {
      return {
        page: 1,
        pullup: true,
        beforeScroll: true,
        hasMore: true,
        result: []
      }
    },
    methods: {
      refresh() {
        this.$refs.suggest.refresh()
      },
      _search() {
        let url = 'https://api.txdna.cn/search'
        // 清空之前的结果
        this.result = []
        this.$http.post(url, {
          'target': 'Problem',
          'content': this.query,
          'type': 'title'
        }).then(response => {
          console.log(response.body)
          this.result = this.result.concat(response.body.result)
        }, response => {
          console.log(response)
        })

        this.$http.post(url, {
          'target': 'Problem',
          'content': this.query,
          'type': 'tag'
        }).then(response => {
          console.log(response.body)
          this.result = this.result.concat(response.body.result)
        }, response => {
          console.log(response)
        })
        // this._checkMore(res.data)
        console.log(this.result)
      },
      listScroll() {
        this.$emit('listScroll')
      },
      selectItem(item) {
        console.log('itemSelect')
        console.log(item)
        this.setProblem(item)
        this.$emit('select', item)
        this.$nextTick(this.$router.push({
          path: `/recommend/${item.id}`
        }))
      },
      _normalizeSongs(list) {
        let ret = []
        list.forEach((musicData) => {
          if (musicData.songid && musicData.albummid) {
            ret.push(createSong(musicData))
          }
        })
        return ret
      },
      ...mapMutations({
        setSinger: 'SET_SINGER',
        setProblem: 'SET_PROBLEM'
      }),
      ...mapActions([
        'insertSong'
      ])
    },
    watch: {
      query(newQuery) {
        if (!newQuery) {
          return
        }
        this._search(newQuery)
      }
    },
    components: {
      Scroll,
      Loading,
      NoResult
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  @import "~common/stylus/variable"
  @import "~common/stylus/mixin"

  .suggest
    height: 100%
    overflow: hidden
    .suggest-list
      padding: 0 30px
      .suggest-item
        display: flex
        align-items: center
        padding-bottom: 20px
      .icon
        flex: 0 0 30px
        width: 30px
        [class^="icon-"]
          font-size: 14px
          color: $color-text-d
      .name
        flex: 1
        font-size: $font-size-medium
        color: $color-text-d
        overflow: hidden
        .text
          no-wrap()
    .no-result-wrapper
      position: absolute
      width: 100%
      top: 50%
      transform: translateY(-50%)
</style>
