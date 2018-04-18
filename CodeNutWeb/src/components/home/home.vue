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
          <mytable></mytable>
        </el-col>
        <el-col :lg="5" :md="6" :sm="24" :xs="24">
          <myinfo></myinfo>
          <myenergy></myenergy>
          <breakthrough-entry></breakthrough-entry>
          <listview></listview>
        </el-col>
        <el-col :lg="3" :md="1" :sm="0" :xs="0">
          <div class="grid-content"></div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { slides } from 'common/js/data'
  import mytable from 'components/table/table'
  import Listview from 'components/listview/listview'
  import Myenergy from 'components/myenergy/myenergy'
  import Myinfo from 'components/myinfo/myinfo'
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
      mytable,
      Listview,
      Myenergy,
      Myinfo,
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

</style>
