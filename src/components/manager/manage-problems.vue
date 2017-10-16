<template>
  <div class="manage-problem">
    <confirm :text="confirmText" @confirm="confirmDele" ref="confirm"></confirm>
    <transition name="el-fade-in-linear">
      <div v-show="!isShowEdit">
        <div class="handle-box">
          <el-button-group>
            <el-button type="primary" @click.stop="showSetupProblem">创建题目</el-button>
            <el-button type="success" @click.stop="refreshProblems">刷新数据</el-button>
          </el-button-group>
          <div class="search-wrapper">
            <search></search>
          </div>
        </div>
        <el-table :data="problemDatas" border ref="multipleTable" style="width: 80%"
                  @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55"></el-table-column>
          <el-table-column prop="id" label="ID" width="150">
          </el-table-column>
          <el-table-column prop="title" label="标题" sortable width="350">
          </el-table-column>
          <el-table-column prop="tag" label="标签" sortable width="250" :formatter="calcTag">
          </el-table-column>
          <el-table-column prop="level" label="难度" sortable width="100">
          </el-table-column>
          <el-table-column prop="submitted" label="提交数" sortable width="100">
          </el-table-column>
          <el-table-column prop="accepted" label="通过数" sortable width="100">
          </el-table-column>
          <el-table-column label="操作" width="150" fixed="right">
            <template scope="scope">
              <el-button size="small"
                         @click.stop="handleEdit(scope.$index, scope.row)">编辑
              </el-button>
              <el-button size="small" type="danger"
                         @click.stop="handleDelete(scope.$index, scope.row)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="pagination">
          <el-pagination
            @current-change="handleCurrentChange"
            layout="prev, pager, next"
            :current-page="cur_page"
            :total="100">
          </el-pagination>
        </div>
      </div>
    </transition>
    <transition name="el-fade-in-linear">
      <problem-edit v-show="isShowEdit" :isEdit="isEdit"
                    @editFinish="hideEdit" ref="problemEdit"></problem-edit>
    </transition>
  </div>
</template>

<script type="text/ecmascript-6">
  import { baseUrl, MSG_OK, MSG_NO, editorThemes } from 'common/js/data'
  import axios from 'axios'
  import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
  import Search from 'components/search/search'
  import ProblemEdit from 'components/manager/manage-problem-edit'
  import { mapActions } from 'vuex'
  import Problem from 'common/js/problem'
  import Confirm from 'base/confirm/confirm'

  export default{
    data(){
      return {
        problemDatas: [],
        cur_page: 1,
        multipleSelection: [],
        select_cate: '',
        select_word: '',
        del_list: [],
        is_search: false,
        rules: {
          id: [
            {required: true, message: 'id不能为空', trigger: 'blur'},
            {min: 3, max: 3, message: 'id为3位字母', trigger: 'blur'}
          ],
          title: [
            {required: true, message: '标题不能为空', trigger: 'blur'},
            {min: 5, message: '标题过短', trigger: 'blur'}
          ],
          description: [
            {required: true, message: '描述不能为空', trigger: 'blur'},
            {min: 5, message: '描述过短', trigger: 'blur'}
          ]
        },
        isShowEdit: false,
        isEdit: false,
        confirmText: '',
        curProblemId: '',
        curProblemTitle: '',
        editorThemes: editorThemes,
        selectTheme: editorThemes[0]
      }
    },
    created(){
      this._getProblemsData(this.cur_page)
    },
    methods: {
      showSetupProblem(){
        this.isEdit = false
        this.isShowEdit = true
      },
      handleCurrentChange(val){
        this.cur_page = val
        this._getProblemsData(this.cur_page)
      },
      _getProblemsData(curPage){
        let url = `${baseUrl}/problems?page=${curPage}`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.problemDatas = response.data.result
          }
        }, response => {})
      },
      formatter(row, column){
        return row.address
      },
      filterTag(value, row){
        return row.tag === value
      },
      handleEdit(index, row){
        console.log(row)
        this.saveOneProblem(new Problem(row))
        this.isEdit = true
        this.isShowEdit = true
        this.$refs.problemEdit.showPromblemInfo()
      },
      handleDelete(index, row){
        this.curProblemId = row.id
        this.curProblemTitle = row.title
        this.confirmText = `确定要删除题目“${this.curProblemTitle}”吗?`
        this.$refs.confirm.show()
      },
      confirmDele(){
        let url = `${baseUrl}/problems/${this.curProblemId}`
        axios.delete(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this._getProblemsData(this.cur_page)
            this.$message({
              message: `成功删除题目:${this.curProblemTitle}`,
              type: 'success'
            })
          } else if (response.data.msg === MSG_NO) {
            this.$notify.error({
              title: '无法删除',
              message: `${response.data.error}`
            })
          }
        }, response => {
          this.$message.error(`无法删除题目${this.curProblemTitle}`)
        })
      },
      delAll(){
        const self = this,
          length = self.multipleSelection.length
        let str = ''
        self.del_list = self.del_list.concat(self.multipleSelection)
        for (let i = 0; i < length; i++) {
          str += self.multipleSelection[i].name + ' '
        }
        self.$message.error('删除了' + str)
        self.multipleSelection = []
      },
      calcTag(row, column, cellValue) {
        if (cellValue === '') {
          return 'Nothing'
        }
        return cellValue.replace(',', ' & ')
      },
      handleSelectionChange(val){
        this.multipleSelection = val
      },
      hideEdit(){
        this.isShowEdit = false
        this._getProblemsData(this.cur_page)
      },
      refreshProblems(){
        this.cur_page = 1
        this._getProblemsData(this.cur_page)
      },
      ...mapActions([
        'saveOneProblem'
      ])
    },
    computed: {
      data(){
        const self = this
        return self.contestDatas.filter(function (d) {
          let is_del = false
          for (let i = 0; i < self.del_list.length; i++) {
            if (d.name === self.del_list[i].name) {
              is_del = true
              break
            }
          }
          if (!is_del) {
            if (d.address.indexOf(self.select_cate) > -1 &&
              (d.name.indexOf(self.select_word) > -1 ||
              d.address.indexOf(self.select_word) > -1)
            ) {
              return d
            }
          }
        })
      }
    },
    components: {
      ElFormItem,
      Search,
      ProblemEdit,
      Confirm
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manage-problem
    .el-dialog
      .block
        .el-date-editor
          width 100%
    .handle-box
      margin-bottom 15px
      width 80%
      .el-button-group
        .el-button
          width 100px
      .search-wrapper
        float right

  .pagination
    margin: 20px 20% 0 0;
    text-align: right;
</style>
