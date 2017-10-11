<template>
  <div>
    <div class="problems-head">
      <img class="img-title" src="static/classification.png"/>
      <h2 class="text-title">Category - All</h2>
      <div class="serach-warpper">
        <search></search>
      </div>
    </div>
    <el-table
      :highlight-current-row=true v-loading="tableLoading" element-loading-text="拼命加载中..." :data="tableData" stripe
      @row-click="_rowclick">
      <el-table-column prop="id" label="id" width="100" align="left" sortable>
      </el-table-column>
      <el-table-column prop="title" label="题目" width="420" align="left" sortable>
      </el-table-column>
      <el-table-column prop="tag" label="标签" width="300" align="left" :formatter="calcTag" sortable>
      </el-table-column>
      <el-table-column prop="level" label="难度" width="110" align="left" sortable>
        <template scope="scope">
          <el-tag
            :type=calcDifficultyTag(scope.row.level)>
            {{calcDifficulty(scope.row.level)}}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="submitted" label="提交" align="left">
        <template scope="scope">
          <el-tag type="primary">{{scope.row.submitted}}</el-tag>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination ">
      <el-pagination
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        layout="prev, pager, next, jumper"
        :total="170">
      </el-pagination>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import axios from 'axios'
  import { mapMutations } from 'vuex'
  import Problem from 'common/js/problem'
  import { baseUrl } from 'common/js/data'
  import Search from 'components/search/search'

  const PER_PAGE = 30

  export default {
    data() {
      return {
        tableData: [],
        currentPage: 1,
        searchResult: [],
        tableLoading: false
      }
    },
    created() {
      this._getProblems()
    },
    methods: {
      _getProblems() {
        this.tableLoading = true
        let url = `${baseUrl}/problems?page=` + this.currentPage + '&per_page=' + PER_PAGE
        axios.get(url).then(response => {
          console.log(response.data.result)
          this.tableData = response.data.result
          console.log(this.tableData)
          this.tableLoading = false
        }, response => {
          console.log(response)
          this._getProblems()
        })
      },
      _rowclick(row, event, column) {
        console.log(row)
        this.setProblem(new Problem({
          id: row.id,
          title: row.title,
          tag: row.tag,
          level: row.level,
          accepted: row.accepted,
          submitted: row.submitted
        }))
        // this.$emit('clickrow')
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
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`)
        console.log(val)
        this._getProblems()
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
    },
    computed: {
      loading: function () {
        if (this.tableData === [] || this.tableData === null) {
          return true
        } else {
          return false
        }
      }
    },
    components: {
      Search
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .problems-head
    .img-title
      vertical-align: middle
    .text-title
      vertical-align: middle
      display inline-block
    .serach-warpper
      float right
      margin-top 16px;
      display inline-block

  .el-table
    border-radius 5px

  .pagination
    margin-top 15px
    margin-bottom 10px
    float right
</style>
