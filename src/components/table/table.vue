<template>
  <div>
    <div class="problems-title">
      <img src="static/classification.png" class="img-title"/>
      <h2 class="text-title">Category - All</h2>
      <el-dropdown>
        <el-input
          class="search-input"
          placeholder="请输入要搜索的题目"
          icon="search"
          v-model="mysearch"
          spellcheck="false"
          :on-icon-click="SearchClick"
          @change="changeSearch">
        </el-input>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-show="dropdownLoading">拼命加载中...</el-dropdown-item>
          <el-dropdown-item v-for="(item,index) in searchResult" v-show="index <= 10 && !dropdownLoading"
                            :key="index">{{item.title}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <el-table
      :highlight-current-row=true v-loading="tableLoading" element-loading-text="拼命加载中..." :data="tableData" stripe
      @row-click="click">
      <el-table-column prop="id" label="id" width="100" align="left">
      </el-table-column>
      <el-table-column prop="title" label="题目" width="450" align="left">
      </el-table-column>
      <el-table-column prop="tag" label="标签" width="300" align="left">
      </el-table-column>
      <el-table-column prop="level" label="难度" width="110" align="left">
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

  const PER_PAGE = 30

  export default {
    data() {
      return {
        tableData: [],
        currentPage: 1,
        mysearch: '',
        searchResult: [],
        tableLoading: false,
        dropdownLoading: false
      }
    },
    created() {
      this._getProblems()
    },
    methods: {
      _getProblems() {
        this.tableLoading = true
        let url = 'https://api.txdna.cn/problems?page=' + this.currentPage + '&per_page=' + PER_PAGE
        axios.get(url).then(response => {
          console.log(response.data.result)
          this.tableData = response.data.result
          console.log(this.tableData)
          this.tableLoading = false
        }, response => {
          console.log(response)
          this._showErrorMessage()
          this._getProblems()
        })
      },
      _showErrorMessage() {
//        this.$notify.info({
//          title: '错误',
//          message: '无法正常加载数据,自动刷新页面'
//        })
      },
      click(row, event, column) {
        console.log(row.id)
        this.setProblem(row)
        this.$emit('clickrow')
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
      SearchClick() {
        this.dropdownLoading = true
        console.log('SearchClick')
        let url = 'https://api.txdna.cn/search'
        // 清空之前的结果
        this.searchResult = []
        axios.post(url, {
          'target': 'Problem',
          'content': this.mysearch,
          'type': 'title'
        }).then(response => {
          console.log(response.data.result)
          if (response.data.result.length === 0) {
            this.searchResult = [{title: `无法查询到含有关键字:${this.mysearch}的题目`}]
          } else {
            this.searchResult = response.data.result
          }
          this.dropdownLoading = false
        }, response => {
          console.log(response)
          this.SearchClick()
        })
      },
      changeSearch() {
        if (this.mysearch === '') {
          this.searchResult = []
          return
        }
        this.dropdownLoading = true
        let url = 'https://api.txdna.cn/search'
        // 清空之前的结果
        this.searchResult = []
        console.log(this.mysearch)
        axios.post(url, {
          'target': 'Problem',
          'content': this.mysearch,
          'type': 'title'
        }).then(response => {
          console.log(response.data.result)
          if (response.data.result.length === 0) {
            this.searchResult = [{title: `无法查询到含有关键字:${this.mysearch}的题目`}]
          } else {
            this.searchResult = response.data.result
          }
          this.dropdownLoading = false
        }, response => {
          console.log(response)
          this.changeSearch()
        })
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
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">

  .problems-title
    .img-title
      vertical-align: middle
    .text-title
      vertical-align: middle
      display inline-block
    .el-dropdown
      float right
      vertical-align bottom
      .el-input
        margin-top 3%
        width 500px

  .el-dropdown-menu
    width 500px

  .el-table
    border-radius 5px

  .pagination
    padding 15px 0 15px 30px
</style>
