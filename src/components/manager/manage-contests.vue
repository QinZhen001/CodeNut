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
        <contest-table :contestDatas="contestDatas" @handleEdit="handleEdit"
                       @handleDelete="handleDelete">
        </contest-table>
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
    <contests-chart v-show="!isShowEdit"></contests-chart>

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
      <contest-edit v-show="isShowEdit" :contest="curContest" @editSuccess="editSuccess"
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
  import ContestTable from 'components/manager/manage-contests-table'

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
        date: null,
        canPassword: false,
        isAutoJoin: true,
        confirmText: '',
        curContestname: '',
        curContestId: '',
        isShowEdit: false,
        curContest: {},
        time: ''
      }
    },
    created(){
      this.getData(this.cur_page)
    },
    methods: {
      editSuccess(){
        console.log('editSuccess')
        this.isShowEdit = false
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
      handleEdit(contest){
        this.curContest = contest
        this.isShowEdit = true
        this.$nextTick(() => {
          this.$refs.contestEdit.show()
        })
      },
      handleDelete(contest){
        this.curContestId = contest.id
        this.curContestname = contest.title
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
      setupContest(){
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
            this.afterSetupSuccess()
          } else {
            this.$notify({
              title: '创建比赛失败',
              message: `${response.data.error}`,
              type: 'error'
            })
          }
        }, response => {})
      },
      afterSetupSuccess(){
        this.getData(this.cur_page)
        this.dialogFormVisible = false
        this.form.title = ''
        this.form.description = ''
        this.form.password = ''
        this.isAutoJoin = true
        this.date = null
      },
      refreshContests(){
        this.cur_page = 1
        this.getData(this.cur_page)
      },
      getTime(date){
        this.time = date
      }
    },
    components: {
      Confirm,
      ContestEdit,
      ContestsChart,
      ContestTable
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


</style>
