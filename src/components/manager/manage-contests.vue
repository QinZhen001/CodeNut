<template>
  <div class="manage-contests">
    <el-dialog title="创建比赛" :visible.sync="dialogFormVisible">
      <el-form :model="form" :rules="rules">
        <el-form-item label="标题" prop="title">
          <el-input v-model="form.title" spellcheck="false"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="description">
          <el-input v-model="form.description" spellcheck="false" type="textarea" :rows="5"></el-input>
        </el-form-item>
        <div class="block">
          <el-date-picker
            format="yyyy-MM-dd HH:mm:ss"
            v-model="date"
            type="datetimerange"
            :picker-options="pickerOptions"
            placeholder="选择时间范围"
            align="right">
          </el-date-picker>
        </div>
        <el-form-item label="比赛密码" prop="password">
          <el-input v-model="form.password" spellcheck="false"></el-input>
        </el-form-item>
        <el-checkbox v-model="auto_checked">自动批准用户加入</el-checkbox>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="setupContest">确 定</el-button>
      </div>
    </el-dialog>

    <div class="handle-box">
      <el-button type="primary" icon="edit" @click="showSetupContestDialog">创建比赛</el-button>
    </div>
    <el-table :data="contestDatas" border style="width: 100%" ref="multipleTable"
              @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="id" label="ID" width="150">
      </el-table-column>
      <el-table-column prop="title" label="标题" sortable width="150">
      </el-table-column>
      <el-table-column prop="description" label="描述" width="330">
      </el-table-column>
      <el-table-column prop="start_time" label="开始时间" width="250">
      </el-table-column>
      <el-table-column prop="end_time" label="结束时间" width="250">
      </el-table-column>
      <el-table-column prop="sponsor" label="举办者" width="120">
      </el-table-column>
      <el-table-column prop="user_nums" label="参加人数" width="120">
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

  export default{
    components: {ElFormItem},
    data(){
      return {
        dialogFormVisible: false,
        form: {
          title: '',
          description: '',
          password: ''
        },
        contestDatas: [],
        cur_page: 1,
        multipleSelection: [],
        select_cate: '',
        select_word: '',
        del_list: [],
        is_search: false,
        rules: {
          title: [
            {required: true, message: '标题不能为空', trigger: 'blur'},
            {min: 5, message: '标题过短', trigger: 'blur'}
          ],
          description: [
            {required: true, message: '描述不能为空', trigger: 'blur'},
            {min: 5, message: '描述过短', trigger: 'blur'}
          ]
        },
        pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date()
              const start = new Date()
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
              picker.$emit('pick', [start, end])
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date()
              const start = new Date()
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
              picker.$emit('pick', [start, end])
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date()
              const start = new Date()
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
              picker.$emit('pick', [start, end])
            }
          }]
        },
        date: '',
        auto_checked: true
      }
    },
    created(){
      this.getData(this.cur_page)
    },
    methods: {
      showSetupContestDialog(){
        this.title = ''
        this.description = ''
        this.dialogFormVisible = true
      },
      handleCurrentChange(val){
        this.cur_page = val
        this.getData(this.cur_page)
      },
      getData(curPage){
        let url = `${baseUrl}/contests`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.contestDatas = response.data.result
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
        let url = `${baseUrl}/contests/${row.id}`
        axios.delete(url).then(response => {
          if (response.data.msg === 'ok') {
            this.getData(this.cur_page)
            this.$message({
              message: `成功删除比赛:${row.title}`,
              type: 'success'
            })
          }
        }, response => {
          this.$message.error(`无法删除比赛${row.title}`)
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
      handleSelectionChange(val){
        this.multipleSelection = val
      },
      setupContest(){
        console.log(this.date)
        let url = `${baseUrl}/contests`
        axios.post(url, {
          title: this.form.title,
          description: this.form.description,
          start_time: '2017-09-25 07:24:41',
          end_time: '2017-12-25 07:24:41'
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.$notify({
              title: '成功',
              message: '创建比赛成功',
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
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manage-contests
    z-index 500
    .el-dialog
      .block
        .el-date-editor
          width 100%
    .handle-box
      margin-bottom 15px
    .pagination
      margin: 20px 0;
      text-align: right;
</style>
