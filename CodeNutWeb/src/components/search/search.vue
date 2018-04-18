<template>
  <el-dropdown @command="handleCommandDropdown">
    <el-input
      class="search-input"
      placeholder="请输入要搜索的题目"
      icon="search"
      v-model.trim="mysearch"
      spellcheck="false"
      :on-icon-click="_onSearch"
      @change="_onSearch"
      @focus="_onSearch">
    </el-input>
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item v-show="dropdownLoading">拼命加载中...</el-dropdown-item>
      <el-dropdown-item v-for="(item,index) in searchResult" v-show="index <= 10 && !dropdownLoading"
                        :key="index" :command="item.id">
        <span class="problem-item-title">{{item.title}}</span>
        <img width="16" height="16 " src="static/problem.png" class="problem-item-img">
      </el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
</template>

<script type="text/ecmascript-6">
  import Problem from 'common/js/problem'
  import axios from 'axios'
  import { baseUrl } from 'common/js/data'
  import { mapMutations } from 'vuex'

  export default{
    data() {
      return {
        mysearch: '',
        dropdownLoading: false,
        searchResult: []
      }
    },
    methods: {
      _onSearch() {
        if (this.mysearch === '') {
          this.searchResult = []
          return
        }
        this.dropdownLoading = true
        console.log('SearchClick')
        let url = `${baseUrl}/search`
        // 清空之前的结果
        this.searchResult = []
        axios.post(url, {
          'target': 'Problem',
          'content': this.mysearch,
          'type': 'title'
        }).then(response => {
          if (response.data.result.length === 0) {
            this.searchResult = [{title: `无法查询到含有关键字:${this.mysearch}的题目`}]
          } else {
            this.searchResult = response.data.result
          }
          this.dropdownLoading = false
        }, response => {
          console.log(response)
          this._onSearch()
        })
      },
      handleCommandDropdown(command) {
        this.setProblem(new Problem({
          id: command
        }))
        this.$router.push('/home/problem')
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .el-dropdown
    .el-input
      width 500px

  .el-dropdown-menu__item
    width auto
    .problem-item-title
      display inline-block
    .problem-item-img
      float right
      margin-top 10px

  .el-dropdown-menu
    width 500px
</style>
