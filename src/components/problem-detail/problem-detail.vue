<template>
  <transition name="el-fade-in-linear">
    <div class="problem"
         v-loading.fullscreen="fullscreenLoading"
         element-loading-text="拼命加载中"
    >
      <el-row>
        <el-col :sm="0" :lg="2" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
        <el-col :sm="24" :lg="20" :md="22" :xs="24">
          <div class="problem-header">
            <h3 align="left">{{problemDetail.title}}</h3>
            <img width="56" height="56"
                 class="collection" :src="getFavoriteSrc(problemDetail)"
                 @click="collection">
          </div>
          <div class="container">
            <el-tabs v-model="tab" type="card">
              <el-tab-pane label="题目描述" name="description">
                <description :data="problemDetail"></description>
              </el-tab-pane>
              <el-tab-pane label="解决方案" name="solution">
                <solution></solution>
              </el-tab-pane>
              <el-tab-pane label="提示" name="third">
                <hints></hints>
              </el-tab-pane>
              <el-tab-pane label="笔记" name="fourth">
                <notes :name="problem.title"></notes>
              </el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
        <el-col :sm="0" :lg="2" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
      </el-row>
      <router-view></router-view>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import { mapGetters, mapActions } from 'vuex'
  import axios from 'axios'
  import Description from 'components/description/description'
  import Solution from 'components/solution/solution'
  import Hints from 'components/hints/hints'
  import Notes from 'components/notes/notes'
  import Problem from 'common/js/problem'
  import { baseUrl, MSG_OK } from 'common/js/data'

  export default {
    data() {
      return {
        fullscreenLoading: true,
        problemDetail: {},
        tab: 'description'
      }
    },
    created() {
      this._getProblemDetail()
    },
    methods: {
      _getProblemDetail() {
        if (!this.problem.id) {
          this.$router.push('/home')
          return
        }
        this.fullscreenLoading = true
        console.log('problem detail id')
        console.log(this.problem.id)
        let url = `${baseUrl}/problems/${this.problem.id}`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            console.log(response.data.result)
            this.problemDetail = response.data.result[0]
            console.log(this.problemDetail.id)
            this.fullscreenLoading = false
          }
        }, response => {
          this._getProblemDetail()
        })
      },
      collection() {
        if (!this.user.user_id) {
          this.$notify({
            title: '无法收藏题目',
            message: '请先登录',
            type: 'error'
          })
        } else {
          if (!this.hasCollect(this.problemDetail.id)) {
            this.saveFavoriteList(this.getCurProblem())
            this.$notify({
              title: '收藏成功',
              message: `收藏题目:${this.problemDetail.title}`,
              type: 'success'
            })
          } else {
            this.deleteFavoriteList(this.getCurProblem())
            this.$notify.info({
              title: '取消成功',
              message: `取消收藏题目:${this.problemDetail.title}`
            })
          }
        }
      },
      getCurProblem(){
        return new Problem({
          id: this.problemDetail.id,
          title: this.problemDetail.title,
          tag: this.problemDetail.tag,
          level: this.problemDetail.level,
          accepted: this.problemDetail.accepted,
          submitted: this.problemDetail.submitted
        })
      },
      hasCollect(id) {
        const index = this.collectionList.findIndex((item) => {
          return item.id === id
        })
        return index > -1
      },
      getFavoriteSrc(problemDetail) {
        if (this.user.user_id != null && this.hasCollect(problemDetail.id)) {
          return 'static/collection.png'
        } else {
          return 'static/nocollection.png'
        }
      },
      ...mapActions([
        'saveFavoriteList',
        'deleteFavoriteList'
      ])
    },
    computed: {
      ...mapGetters([
        'problem',
        'collectionList',
        'user'
      ])
    },
    components: {
      Description,
      Solution,
      Hints,
      Notes
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .problem
    flex: 1 0 auto;
    .problem-header
      .collection
        float right
        margin-top 5px
        vertical-align bottom
      h3
        display: inline-block;
        margin-bottom: 10px;
        font-weight: 500;
        line-height: 1.0;
        font-size: 24px;

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
