<template>
  <transition name="el-fade-in-linear">
    <div class="problem">
      <el-row v-loading="loading"
              element-loading-text="拼命加载中...">
        <el-col :sm="0" :lg="2" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>

        <el-col :sm="24" :lg="20" :md="22" :xs="24">
          <div class="problem-header">
            <h3 align="left">{{problemDetail.title}}</h3>
            <img v-show="!hasCollect" width="56" height="56" src="static/nocollection.png" class="collection"
                 @click="collection">
            <img v-show="hasCollect" width="56" height="56" src="static/collection.png" class="collection"
                 @click="collection">
          </div>
          <div class="container">
            <el-tabs v-model="tab" type="card">
              <el-tab-pane label="Description" name="description">
                <description :data="problemDetail"></description>
              </el-tab-pane>
              <el-tab-pane label="Solution" name="solution">
                <solution :data="problemDetail"></solution>
              </el-tab-pane>
              <el-tab-pane label="Hints" name="third">
                <hints></hints>
              </el-tab-pane>
              <el-tab-pane label="定时任务补偿" name="fourth">
                定时任务补偿
              </el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
        <el-col :sm="0" :lg="2" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
      </el-row>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import { mapGetters } from 'vuex'
  import axios from 'axios'
  import Description from 'components/description/description'
  import Solution from 'components/solution/solution'
  import Hints from 'components/hints/hints'

  export default {
    data() {
      return {
        loading: true,
        problemDetail: {},
        tab: 'description',
        hasCollect: false
      }
    },
    created() {
      this._getProblemDetail()
    },
    computed: {
      ...mapGetters([
        'problem'
      ])
    },
    methods: {
      _getProblemDetail() {
        if (!this.problem.id) {
          this.$router.push('/home')
          return
        }
        console.log('problem detail id')
        console.log(this.problem.id)
        let url = 'https://api.txdna.cn/problems/' + `${this.problem.id}`
        axios.get(url).then(response => {
          console.log(response.data)
          this.problemDetail = response.data
          this.loading = false
        }, response => {
          console.log(response)
          this.$message.error('无法获取数据')
          setTimeout(() => { this.$router.back() }, 2000)
        })
      },
      collection() {
        this.hasCollect = !this.hasCollect
        if (this.hasCollect) {
          this.$notify({
            title: '收藏成功',
            message: `收藏题目:${this.problemDetail.title}`,
            type: 'success'
          })
        } else {
          this.$notify.info({
            title: '取消成功',
            message: `取消收藏题目:${this.problemDetail.title}`
          })
        }
      }
    },
    components: {
      Description,
      Solution,
      Hints
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .problem
    min-height 100%
    .problem-header
      .collection
        float right
        margin-top 5px
        vertical-align bottom

  h3
    display: inline-block;
    margin-bottom: 10px;
    margin-right: .5em;
    font-family: inherit;
    font-weight: 500;
    line-height: 1.1;
    font-size: 24px;
    color: inherit;

  .container
    margin-top: 32px;
    .el-tabs__content
      min-height 800px

  .grid-content
    border-radius: 4px
    min-height: 36px

  .bg-purple
    background: #d3dce6

</style>
