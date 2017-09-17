<template>
  <div class="user-center">
    <el-row :gutter="20">
      <el-col :span="2" :sm="0" :lg="3" :md="1" :xs="0">
        <div class="grid-content">
        </div>
      </el-col>

      <el-col :span="7" :sm="24" :lg="6" :md="8" :xs="24">
        <user-card></user-card>
        <about-me></about-me>
        <my-progress></my-progress>
      </el-col>

      <el-col :span="13" :sm="24" :lg="12" :md="14" :xs="24">
        <el-table :data="collectionList" stripe @row-click="clickrow"
                  :max-height="800" :highlight-current-row=true empty-text="暂无收藏">
          <el-table-column label="Your Collection" class="el-table-head">
            <el-table-column prop="id" label="id" min-width="100" align="left">
            </el-table-column>
            <el-table-column prop="title" label="题目" min-width="350" align="left">
            </el-table-column>
            <el-table-column prop="tag" label="标签" min-width="350" align="left">
            </el-table-column>
            <el-table-column prop="level" label="难度" min-width="100" align="left">
              <template scope="scope">
                <el-tag
                  :type=calcDifficultyTag(scope.row.level)>
                  {{calcDifficulty(scope.row.level)}}
                </el-tag>
              </template>
            </el-table-column>
          </el-table-column>
        </el-table>
      </el-col>

      <el-col :span="2" :sm="0" :lg="3" :md="1" :xs="0">
        <div class="grid-content"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/ecmascript-6">
  import UserCard from 'components/usercenter/usercard'
  import MyProgress from 'components/usercenter/myprogress'
  import AboutMe from 'components/usercenter/aboutme'
  import { mapGetters, mapMutations } from 'vuex'

  export default {
    data() {
      return {}
    },
    methods: {
      clickrow(row, event, column) {
        this.setProblem(row)
        this.$router.push('/home/problem')
      },
      calcDifficultyTag(level) {
        if (level === 1) {
          return 'success'
        } else if (level === 2) {
          return 'warning'
        } else {
          return 'danger'
        }
      },
      calcDifficulty(level) {
        if (level === 1) {
          return 'Easy'
        } else if (level === 2) {
          return 'Medium'
        } else {
          return 'Hard'
        }
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    },
    computed: {
      ...mapGetters([
        'collectionList'
      ])
    },
    components: {
      UserCard,
      MyProgress,
      AboutMe
    }
  }

</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .user-center
    margin-top 25px

  .bg-purple
    background: #d3dce6;

  .bg-purple-light
    background: #e5e9f2;

  .grid-content
    border-radius: 4px;
    min-height: 36px;

  .user-card
    border-radius 5px

  .el-table
    border-radius 5px

</style>
