<template>
  <div class="manage-problem">
    <el-dialog title="创建题目" :visible.sync="dialogFormVisible">
      <el-form :model="form" :rules="rules">
        <el-form-item label="ID" prop="id">
          <el-input v-model="form.id" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="标题" prop="title">
          <el-input v-model="form.title" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="description">
          <el-input v-model="form.description" spellcheck="false" type="textarea" :rows="3"></el-input>
        </el-form-item>
        <el-form-item label="程序模板">
          <el-input v-model="form.temlate" spellcheck="false" type="textarea" :rows="5"></el-input>
        </el-form-item>
        <el-form-item label="标签">
          <el-input v-model="form.tag" spellcheck="false"></el-input>
        </el-form-item>
        <el-radio-group v-model="radio">
          <el-radio :label="1">Easy</el-radio>
          <el-radio :label="2">Medium</el-radio>
          <el-radio :label="3">Hard</el-radio>
        </el-radio-group>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="setupContest">确 定</el-button>
      </div>
    </el-dialog>
    <div class="handle-box">
      <el-button type="primary" icon="edit" @click="showSetupContestDialog">创建题目</el-button>
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
      <el-table-column label="操作" width="150">
        <template scope="scope">
          <el-button size="small"
                     @click="handleEdit(scope.$index, scope.row)">编辑
          </el-button>
          <el-button size="small" type="danger"
                     @click="handleDelete(scope.$index, scope.row)">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination
        @current-change="handleCurrentChange"
        layout="prev, pager, next"
        :total="100">
      </el-pagination>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { baseUrl, MSG_OK } from 'common/js/data'
  import axios from 'axios'
  import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
  import Search from 'components/search/search'

  export default{
    data(){
      return {
        dialogFormVisible: false,
        form: {
          title: '',
          description: '',
          temlate: '',
          tag: '',
          id: ''
        },
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
        date: '',
        radio: 1
      }
    },
    created(){
      this._getData(this.cur_page)
    },
    methods: {
      showSetupContestDialog(){
        this.title = ''
        this.description = ''
        this.dialogFormVisible = true
      },
      handleCurrentChange(val){
        this.cur_page = val
        this._getData(this.cur_page)
      },
      _getData(curPage){
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
        this.$message('编辑第' + (index + 1) + '行')
      },
      handleDelete(index, row){
        //this.$message.error('删除第' + (index + 1) + '行')
        let url = `${baseUrl}/problems/${row.id}/codes`
        axios.delete(url).then(response => {
          if (response.data.msg === 'ok') {
            this.getData(this.cur_page)
            this.$message({
              message: `成功删除题目:${row.title}`,
              type: 'success'
            })
          }
        }, response => {
          this.$message.error(`无法删除题目${row.title}`)
        })
        this._getData(this.cur_page)
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
      setupContest(){
        let url = `${baseUrl}/problems/${this.form.id}/solutions`
        let level = ''
        if (this.radio === 1) {
          level = 'Easy'
        } else if (this.radio === 2) {
          level = 'Medium'
        } else if (this.radio === 3) {
          level = 'Hard'
        }
        axios.post(url, {
          title: this.form.title,
          description: this.form.description,
          tag: this.form.tag,
          level: level,
          code: this.form.temlate
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.$notify({
              title: '成功',
              message: '创建题目成功',
              type: 'success'
            })
            this.dialogFormVisible = false
          } else {
            this.$notify({
              title: '失败',
              message: '创建比赛失败',
              type: 'error'
            })
          }
        }, response => {})
      }
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
      Search
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manage-problem
    z-index 500
    .el-dialog
      .block
        .el-date-editor
          width 100%
    .handle-box
      margin-bottom 15px
      width 80%
      .search-wrapper
        float right

  .pagination
    margin: 20px 20% 0 0;
    text-align: right;
</style>
