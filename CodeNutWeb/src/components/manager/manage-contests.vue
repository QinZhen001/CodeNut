<template>
  <div>
    <transition name="el-fade-in-linear">
      <div class="manage-contests" v-show="!isShowEdit">
        <div class="handle-box">
          <el-button-group>
            <el-button type="primary" @click="showSetupContestDialog">创建比赛</el-button>
            <el-button type="success" @click="refreshContests">刷新数据</el-button>
          </el-button-group>
        </div>
        <el-table :data="contestDatas" border style="width: 100%" ref="multipleTable"
                  @selection-change="handleSelectionChange" @expand="expandCol">
          <el-table-column type="expand">
            <template scope="props">
              <ul class="user-list">
                <li>
                  <span>参赛选手:</span>
                </li>
                <li v-for="(item,index) in contestants" :key="index">
                  {{item.user}}
                </li>
              </ul>
            </template>
          </el-table-column>
          <el-table-column prop="id" label="ID" width="150">
          </el-table-column>
          <el-table-column prop="title" label="标题" sortable width="150">
          </el-table-column>
          <el-table-column prop="description" label="描述" width="330" show-overflow-tooltip>
          </el-table-column>
          <el-table-column prop="start_time" label="开始时间" width="250">
          </el-table-column>
          <el-table-column prop="end_time" label="结束时间" width="250">
          </el-table-column>
          <el-table-column prop="sponsor" label="举办者" width="120">
          </el-table-column>
          <el-table-column prop="user_nums" label="参加人数" width="120">
          </el-table-column>
          <el-table-column label="操作" width="150" fixed="right">
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
            :current-page="cur_page"
            :total="100">
          </el-pagination>
        </div>
      </div>
    </transition>
    <contests-chart></contests-chart>
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
            @change="getTime"
            align="right">
          </el-date-picker>
        </div>
        <el-form-item class="autojoin-item">
          <el-checkbox v-model="isAutoJoin">自动批准用户加入</el-checkbox>
        </el-form-item>
        <el-form-item class="password-item" prop="password">
          <div>
            <el-checkbox class="password-checkbox" v-model="canPassword">设置比赛密码</el-checkbox>
            <el-input class="password-input" v-model="form.password" spellcheck="false"
                      v-show="canPassword"></el-input>
          </div>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="setupContest">确 定</el-button>
      </div>
    </el-dialog>
    <confirm ref="confirm" :text="confirmText" @confirm="confirmDele"></confirm>
    <transition name="el-fade-in-linear">
      <contest-edit v-show="isShowEdit" :contest="curContest" @successEdit="successEdit"
                    @editFinish="hideEdit" ref="contestEdit"></contest-edit>
    </transition>
  </div>
</template>

<script type="text/ecmascript-6">
  import { baseUrl, MSG_OK } from 'common/js/data'
  import axios from 'axios'
  //import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
  import Confirm from 'base/confirm/confirm'
  import ContestEdit from 'components/manager/manage-contests-edit'
  import ContestsChart from 'components/manager/contests-chart'

  export default{
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
        date: [new Date(2017, 10, 10, 10, 10), new Date(2017, 12, 30, 10, 10)],
        canPassword: false,
        isAutoJoin: true,
        confirmText: '',
        curContestname: '',
        curContestId: '',
        contestants: [],
        isShowEdit: false,
        curContest: {},
        time: ''
      }
    },
    created(){
      this.getData(this.cur_page)
    },
    methods: {
      successEdit(){
        this.getData(this.cur_page)
      },
      hideEdit(){
        this.isShowEdit = false
      },
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
        let url = `${baseUrl}/contests?page=${curPage}`
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
        this.curContest = row
        this.curContest.date = this.time
        this.isShowEdit = true
        this.$nextTick(() => {
          this.$refs.contestEdit.showInfo()
        })
      },
      handleDelete(index, row){
        this.curContestId = row.id
        this.curContestname = row.title
        this.confirmText = `确定要删除比赛 “${this.curContestname}吗?”`
        this.$refs.confirm.show()
      },
      confirmDele(){
        let url = `${baseUrl}/contests/${this.curContestId}`
        axios.delete(url).then(response => {
          if (response.data.msg === 'ok') {
            this.getData(this.cur_page)
            this.$message({
              message: `成功删除比赛:${this.curContestname}`,
              type: 'success'
            })
          }
        }, response => {
          this.$message.error(`无法删除比赛${this.curContestname}`)
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
//        let a = document.getElementById('el-input__inner')
//        console.log(a.value)
        console.log(this.time)
        let url = `${baseUrl}/contests`
        let resulTime = (this.time + '').split(/\s\S\s/)
        axios.post(url, {
          title: this.form.title,
          description: this.form.description,
          start_time: resulTime[0],
          end_time: resulTime[1],
          password: this.form.password,
          auto_approve: this.isAutoJoin
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.$notify({
              title: '成功',
              message: '创建比赛成功',
              type: 'success'
            })
            this._setupContestSuccess()
          } else {
            this.$notify({
              title: '创建比赛失败',
              message: `${response.data.error}`,
              type: 'error'
            })
          }
        }, response => {})
      },
      _setupContestSuccess(){
        this.getData(this.cur_page)
        this.dialogFormVisible = false
        this.form.title = ''
        this.form.description = ''
        this.form.password = ''
        this.isAutoJoin = true
        this.date = [new Date(2017, 10, 10, 10, 10), new Date(2017, 12, 30, 10, 10)]
      },
      refreshContests(){
        this.cur_page = 1
        this.getData(this.cur_page)
      },
      expandCol(row, expanded){
        console.log(row)
        console.log(expanded)
        if (expanded) {
          let url = `${baseUrl}/contests/${row.id}/users`
          axios.get(url).then(response => {
            if (response.data.msg === MSG_OK) {
              if (response.data.result) {
                this.contestants = response.data.result
              } else {
                this.contestants = '暂无'
              }

              console.log(this.contestants)
            }
          }, response => {})
        }
      },
      getTime(date){
        this.time = date
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
      Confirm,
      ContestEdit,
      ContestsChart
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manage-contests
    .el-dialog
      .block
        .el-date-editor
          width 100%
    .handle-box
      margin-bottom 15px
      .el-button-group
        .el-button
          width 100px
    .pagination
      margin: 20px 0;
      text-align: right;

  .autojoin-item
    margin-bottom 0

  .password-item
    padding 10px 0 0 0
    margin-bottom 0
    .password-input
      margin-left 15px
      width 50%

  .user-list
    li
      float: left
      list-style: none; /* 将默认的列表符号去掉 */
      padding: 0; /* 将默认的内边距去掉 */
      margin-left: 6px;
      font-size 16px
      span
        font-weight 400
        font-size 16px
        color #1D8CE0
</style>
