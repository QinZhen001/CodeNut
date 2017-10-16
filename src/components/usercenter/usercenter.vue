<template>
  <div>
    <transition name="el-fade-in-linear">
      <div class="user-center">
        <el-row :gutter="20">
          <el-col :span="2" :sm="0" :lg="3" :md="1" :xs="0">
            <div class="grid-content">
            </div>
          </el-col>

          <el-col :span="6" :sm="24" :lg="5" :md="7" :xs="24">
            <user-card></user-card>
            <about-me></about-me>
            <my-progress></my-progress>
          </el-col>

          <el-col :span="14" :sm="24" :lg="13" :md="15" :xs="24">
            <el-table :data="collectionList" stripe @row-click="clickCollectionTableRow"
                      :max-height="600" :highlight-current-row=true empty-text="暂无收藏">
              <el-table-column label="Your Collection" class="el-table-head">
                <el-table-column prop="id" label="ID" width="80" align="left">
                </el-table-column>

                <el-table-column prop="title" label="题目" width="400" align="left">
                </el-table-column>

                <el-table-column prop="tag" label="标签" width="380" align="left" :formatter="calcTag">
                </el-table-column>
                <el-table-column prop="level" label="难度" align="left">
                  <template scope="scope">
                    <el-tag
                      :type=calcDifficultyTag(scope.row.level)>
                      {{calcDifficulty(scope.row.level)}}
                    </el-tag>
                  </template>
                </el-table-column>
              </el-table-column>
            </el-table>

            <el-table class="contest-table" :data="contestList"
                      stripe border :max-height="600" @row-click="clickContestTableRow"
                      :highlight-current-row=true empty-text="暂无比赛">
              <el-table-column label="Your Contest" class="el-table-head">
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
            </el-table>
          </el-col>

          <el-col :span="2" :sm="0" :lg="3" :md="1" :xs="0">
            <div class="grid-content"></div>
          </el-col>
        </el-row>
      </div>
    </transition>
    <el-dialog
      title="提示"
      :visible.sync="contestDialogVisible">
      <span class="contest-dialog-title">是否要加入{{chooseContest.sponsor}}举办的“{{chooseContest.title}}”比赛?</span>
      <div class="password-wrapper">
        <span class="password-text">密码:</span>
        <el-input class="password-input" v-model="password" placeholder="请输入比赛密码" size="small"></el-input>
      </div>
      <span slot="footer" class="dialog-footer">
    <el-button @click="contestDialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="comfirmContest">确 定</el-button>
        </span>
    </el-dialog>
  </div>
</template>

<script type="text/ecmascript-6">
  import UserCard from 'components/usercenter/usercard'
  import MyProgress from 'components/usercenter/myprogress'
  import AboutMe from 'components/usercenter/aboutme'
  import { mapGetters, mapMutations } from 'vuex'
  import { baseUrl, MSG_OK } from 'common/js/data'
  import axios from 'axios'

  export default {
    data() {
      return {
        contestList: [],
        contestDialogVisible: false,
        chooseContest: {},
        password: ''
      }
    },
    mounted(){
      let url = `${baseUrl}/contests`
      axios.get(url).then(response => {
        if (response.data.msg === MSG_OK) {
          this.contestList = response.data.result
          console.log('created')
          console.log(this.contestList)
        }
      }, response => {})
    },
    methods: {
      clickCollectionTableRow(row, event, column) {
        this.setProblem(row)
        this.$router.push('/home/problem')
      },
      clickContestTableRow(row, event, column) {
        console.log(row)
        this.chooseContest = row
        this.contestDialogVisible = true
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
      calcTag(row, column, cellValue) {
        if (cellValue === '') {
          return 'Nothing'
        }
        return cellValue.replace(',', ' & ')
      },
      comfirmContest(){
        let url = `${baseUrl}/contests/${this.chooseContest.id}/users`
        let password = (this.password === '' ? null : this.password)
        axios.post(url, {
          password: password
        }).then(response => {
          if (response.data.msg === 'ok') {
            this.contestDialogVisible = false
            this.$notify({
              title: '成功',
              message: '加入比赛成功！',
              type: 'success'
            })
          }
        }, response => {})
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    },
    computed: {
      ...mapGetters([
        'collectionList',
        'user'
      ])
    },
    components: {
      UserCard,
      MyProgress,
      AboutMe
    }
  }

</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .user-center
    margin-top 25px

  .el-table
    border-radius 5px

  .bg-purple
    background: #d3dce6;

  .bg-purple-light
    background: #e5e9f2;

  .grid-content
    border-radius: 4px;
    min-height: 36px;

  .user-card
    border-radius 5px

  .contest-table
    margin-top 50px

  .el-dialog
    .el-dialog__body
      padding 10px 20px
      .contest-dialog-title
        font-size 18px
        font-weight 400
      .password-wrapper
        margin-top 10px
        .password-text
          font-size 16px
          font-weight 300
        .password-input
          margin-left 3px
          width 60%
</style>
