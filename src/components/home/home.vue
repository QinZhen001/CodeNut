<template>
  <div class="home">
    <div class="body">
      <el-row>
        <el-col :span="24">
          <el-carousel :interval="4000" type="card" height="288px">
            <el-carousel-item v-for="(item,index) in slideItems" :key="index">
              <img :src="item.picUrl" width="100%" height="100%" @click="clickCarouselItem(index)">
            </el-carousel-item>
          </el-carousel>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :lg="3" :md="1" :sm="0" :xs="0">
          <div class="grid-content"></div>
        </el-col>
        <el-col :lg="13" :md="16" :sm="24" :xs="24">
          <div class="table-head">
            <img class="img-title" src="static/classification.png"/>
            <span class="text-title">Category - All</span>
            <div class="serach-warpper">
              <search></search>
            </div>
          </div>
          <home-table></home-table>
        </el-col>
        <el-col :lg="5" :md="6" :sm="24" :xs="24">
          <myinfo></myinfo>
          <myenergy></myenergy>
          <breakthrough-entry></breakthrough-entry>
          <hot-list></hot-list>
        </el-col>
        <el-col :lg="3" :md="1" :sm="0" :xs="0">
          <div class="grid-content"></div>
        </el-col>
      </el-row>
    </div>
    <router-view></router-view>
  </div>
</template>

<script type="text/ecmascript-6">
  import { slides } from 'common/js/data'
  import HomeTable from 'components/home/hometable'
  import HotList from 'components/home/hotlist'
  import Myenergy from 'components/home/myenergy'
  import Myinfo from 'components/home/myinfo'
  import Search from 'base/search/search'
  import { mapMutations } from 'vuex'
  import Problem from 'common/js/problem'
  import BreakthroughEntry from 'components/breakthrough/breakthrough-entry'

  export default {
    data() {
      return {
        slideItems: [],
        page: 1,
        showLoginDialog: false
      }
    },
    created() {
      this.slideItems = slides
    },
    methods: {
      clickCarouselItem(index) {
        this.setProblem(new Problem({id: this.slideItems[index].linkProblemId}))
        this.$router.push('/home/problem')
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    },
    components: {
      HomeTable,
      HotList,
      Myenergy,
      Myinfo,
      Search,
      BreakthroughEntry
    }
  }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">
  .home
    flex: 1 0 auto;
    width: 100%;
    .body
      margin-top 4px
      .el-carousel
        margin-bottom 6px
      .el-carousel__item h3
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0

  .grid-content
    height: 36px;
    border-radius: 4px;

  .table-head
    margin-top 6px
    padding 10px 0 20px 0
    width 100%
    .img-title
      vertical-align: middle
    .text-title
      vertical-align: middle
      font-weight: 300;
      font-size: 24px;
    .serach-warpper
      float right
      vertical-align: middle
</style>
