<template>
  <el-table class="contest-table" :data="contestList"
            stripe border @row-click="clickRow"
            :highlight-current-row=true empty-text="暂无比赛">
    <el-table-column label="我的比赛" class="el-table-head">
      <el-table-column prop="id" label="ID" width="60" align="left">
      </el-table-column>
      <el-table-column prop="title" label="标题" width="200" align="left">
      </el-table-column>
      <el-table-column prop="description" label="描述" width="300" align="left" :formatter="calcTag">
      </el-table-column>
      <el-table-column prop="start_time" label="开始时间" width="250" align="left">
      </el-table-column>
      <el-table-column prop="end_time" label="结束时间" width="250" align="left">
      </el-table-column>
    </el-table-column>
    <el-table-column label="操作" fixed="right" align="left" width="100">
      <template scope="scope">
        <el-button
          size="small"
          type="success"
          @click="handleJoin(scope.$index, scope.row)">我要参加
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script type="text/ecmascript-6">
  export default{
    props: {
      contestList: {
        type: Array
      }
    },
    methods: {
      clickRow(row, event, column) {
        console.log(row)
      },
      handleJoin(index, row){
        this.$emit('joinContest', row)
      },
      calcTag(row, column, cellValue) {
        if (cellValue === '') {
          return 'Nothing'
        }
        return cellValue.replace(',', ' & ')
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .el-table
    border-radius 5px

  .contest-table
    margin-top 50px
</style>
