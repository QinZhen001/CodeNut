<template>
  <div class="home">
    <div class="body">
      <el-row>
        <el-col :span="0" :sm="24" :lg="24" :md="24" :xs="24">
          <el-carousel :interval="4000" type="card" height="288px">
            <el-carousel-item v-for="(item,index) in slideItems" :key="index">
              <img :src="item.picUrl" width="100%" height="100%">
            </el-carousel-item>
          </el-carousel>
        </el-col>
      </el-row>

      <el-row :gutter="20">
        <el-col :span="1" :sm="0" :lg="2" :md="0" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
        <el-col :span="15" :sm="24" :lg="14" :md="16" :xs="24">
          <mytable @clickrow="clicktable"></mytable>
        </el-col>
        <el-col :span="7" :sm="24" :lg="5" :md="7" :xs="24">
          <myinfo></myinfo>
          <myenergy></myenergy>
          <listview></listview>
        </el-col>
        <el-col :span="0" :sm="0" :lg="3" :md="0" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
      </el-row>
    </div>
    <myfooter></myfooter>
  </div>
</template>

<script type="text/ecmascript-6">
  import { slides } from 'common/js/data'
  import mytable from 'components/table/table'
  import Listview from 'components/listview/listview'
  import Myenergy from 'components/myenergy/myenergy'
  import Myinfo from 'components/myinfo/myinfo'
  import Myfooter from 'components/myfooter/myfooter'

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
      clicktable() {
        this.$router.push('/problem')
      }
    },
    components: {
      mytable,
      Listview,
      Myenergy,
      Myinfo,
      Myfooter
    }
  }
</script>


<style scoped lang="stylus" rel="stylesheet/stylus">

  .home
    .body
      min-height 100%
      margin-top 4px
      .el-carousel
        margin-bottom 5px
        .el-carousel__item h3
          color: #475669;
          font-size: 14px;
          opacity: 0.75;
          line-height: 200px;
          margin: 0
    .bg-purple-dark
      background: #99a9bf;
    .bg-purple
      background: #d3dce6;
    .bg-purple-light
      background: #e5e9f2;
    .grid-content
      border-radius: 4px;
      min-height: 36px;

  /*@media screen and (max-width: 1199px) {*/
  /*}*/
</style>
