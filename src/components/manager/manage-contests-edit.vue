<template>
  <transition name="el-fade-in-linear">
    <div class="problem-edit">
      <div class="panel">
        <div class="panel-heading">
          <i class="el-icon-arrow-left" @click.stop="quit"></i>
          <h3 class="panel-title">更新比赛</h3>
          <h3 class="panel-title">比赛(ID:{{contest.id}})</h3>
          <el-tag class="quit-tag" type="danger" @click.native.stop="quit">退出</el-tag>
        </div>
        <div class="panel-body">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="比赛题目">
              <el-input class="short-input" v-model="form.title" spellcheck="false" size="small"></el-input>
            </el-form-item>
            <el-form-item label="描述" prop="description">
              <el-input v-model="form.description" spellcheck="false" type="textarea" :rows="5"></el-input>
            </el-form-item>
            <el-form-item class="password-item" prop="password">
              <div>
                <el-checkbox class="time-checkbox" v-model="canChangeTime">修改比赛时间</el-checkbox>
                <el-date-picker
                  v-show="canChangeTime"
                  format="yyyy-MM-dd HH:mm:ss"
                  v-model="date"
                  type="datetimerange"
                  :picker-options="pickerOptions"
                  placeholder="选择时间范围"
                  @change="geteDditTime"
                  align="left">
                </el-date-picker>
              </div>
            </el-form-item>
            <el-form-item class="autojoin-item">
              <el-checkbox v-model="isAutoJoin">自动批准用户加入</el-checkbox>
            </el-form-item>
            <el-form-item class="password-item" prop="password">
              <div>
                <el-checkbox class="password-checkbox" v-model="canChangePassword">修改比赛密码</el-checkbox>
                <el-input class="short-input password-input" v-model="form.password" spellcheck="false"
                          v-show="canChangePassword"></el-input>
              </div>
            </el-form-item>
            <el-button class="setup-btn" @click="clickBtn"
                       type="success">更新比赛
            </el-button>
          </el-form>
        </div>
      </div>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
  import axios from 'axios'
  import { baseUrl, MSG_OK, MSG_NO } from 'common/js/data'

  export default{
    components: {ElFormItem},
    props: {
      contest: {
        type: Object,
        default: {}
      }
    },
    data(){
      return {
        form: {
          title: '',
          description: '',
          password: ''
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
        date: [],
        isAutoJoin: true,
        canChangePassword: false,
        resultTime: [],
        canChangeTime: false
      }
    },
    methods: {
      quit(){
        this._clearAllData()
        this.$emit('editFinish')
      },
      clickBtn(){
        let url = `${baseUrl}/contests/${this.contest.id}`
        if (this.canChangeTime) {
          this.editContestWithTime(url)
        } else {
          this.editContestWithoutTime(url)
        }
      },
      editContestWithTime(url){
        axios.put(url, {
          title: this.form.title,
          description: this.form.description,
          start_time: this.resultTime[0],
          end_time: this.resultTime[1],
          auto_approve: this.isAutoJoin,
          password: this.form.password
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.notifySuccess()
            this._clearAllData()
            this.$emit('editSuccess')
          } else if (response.data.msg === MSG_NO) {
            this.notifyError(response.data.error)
          }
        }, response => {})
      },
      editContestWithoutTime(url){
        axios.put(url, {
          title: this.form.title,
          description: this.form.description,
          auto_approve: this.isAutoJoin,
          password: this.form.password
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.notifySuccess()
            this._clearAllData()
            this.$emit('editSuccess')
          } else if (response.data.msg === MSG_NO) {
            this.notifyError(response.data.error)
          }
        }, response => {})
      },
      notifySuccess(){
        this.$notify({
          title: '成功',
          message: '更新比赛成功',
          type: 'success'
        })
      },
      notifyError(error){
        this.$notify({
          title: '更新失败',
          message: error,
          type: 'error'
        })
      },
      _clearAllData(){
        this.date = []
        this.form.title = ''
        this.form.description = ''
        this.form.password = ''
        this.isAutoJoin = true
        this.canChangePassword = false
        this.canChangeTime = false
      },
      show(){
        this._clearAllData()
        console.log(this.contest)
        this.form.title = this.contest.title
        this.form.description = this.contest.description
        this.date = this.contest.date
      },
      geteDditTime(date){
        this.resultTime = (date + '').split(/\s\S\s/)
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .problem-edit
    .panel
      border-radius: 5px;
      margin-bottom: 20px;
      background-color: #fff;
      border: 1px solid #ddd;
      -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
      box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
      .panel-heading
        padding: 10px 15px;
        color: #333;
        background-color: #f5f5f5;
        border-color: #ddd;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        border-bottom: 1px solid transparent;
        .el-icon-arrow-left
          color: lightsteelblue
          &:hover
            cursor pointer
        .panel-title
          display inline-block
          margin-left 5px
          margin-top 0
          margin-bottom 0
          font-size: 18px;
          color: inherit;
          font-weight: 500;
          line-height: 1.1;
        .quit-tag
          float right
          &:hover
            cursor pointer
      .panel-body
        padding: 15px 45px;
        .el-form
          position relative
          .el-form-item
            margin-right 10%
            .program-edit
              display inline-block
              width 83%
              border 1px solid #ddd
            .short-input
              width 50%
            .password-input
              margin-left 20px
            .time-checkbox
              margin-right 20px
          .setup-btn
            position absolute
            bottom -20px
            right 0
            width 100px
</style>
