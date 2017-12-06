<template>
  <el-table :data="collectionList" stripe @row-click="clickRow"
            :max-height="600" :highlight-current-row=true empty-text="暂无收藏">
    <el-table-column label="我的收藏" class="el-table-head">
      <el-table-column prop="id" label="ID" width="80" align="left">
      </el-table-column>

      <el-table-column prop="title" label="题目" width="400" align="left">
      </el-table-column>

      <el-table-column prop="tag" label="标签" width="380" align="left" :formatter="calcTag">
      </el-table-column>
      <el-table-column prop="level" label="难度" align="left">
        <template scope="scope">
          <el-tag
            :type=calcDifficultyTag(scope.row.level)>
            {{calcDifficulty(scope.row.level)}}
          </el-tag>
        </template>
      </el-table-column>
    </el-table-column>
  </el-table>
</template>

<script type="text/ecmascript-6">
  import { mapMutations } from 'vuex'

  export default{
    props: {
      collectionList: {
        type: Array
      }
    },
    methods: {
      clickRow(row, event, column) {
        this.setProblem(row)
        this.$router.push('/problem')
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
      calcTag(row, column, cellValue) {
        if (cellValue === '') {
          return 'Nothing'
        }
        return cellValue.replace(',', ' & ')
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .el-table
    border-radius 5px
</style>
