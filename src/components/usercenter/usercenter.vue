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
            <collected-table :collectionList="collectionList"></collected-table>
            <contest-table :contestList="contestList" @joinContest="joinContest"></contest-table>
          </el-col>
          <el-col :span="2" :sm="0" :lg="3" :md="1" :xs="0">
            <div class="grid-content"></div>
          </el-col>
        </el-row>
        <contest-dialog ref="contestDialog" :contest="curContest"></contest-dialog>
      </div>
    </transition>
  </div>
</template>

<script type="text/ecmascript-6">
  import UserCard from 'components/usercenter/usercard'
  import MyProgress from 'components/usercenter/myprogress'
  import AboutMe from 'components/usercenter/aboutme'
  import CollectedTable from 'components/usercenter/collectedtable'
  import ContestTable from 'components/usercenter/contesttable'
  import ContestDialog from 'base/contestdialog/contestdialog'
  import { mapGetters } from 'vuex'
  import { baseUrl, MSG_OK } from 'common/js/data'
  import axios from 'axios'

  export default {
    data() {
      return {
        contestList: [],
        curContest: {}
      }
    },
    mounted(){
      let url = `${baseUrl}/contests`
      axios.get(url).then(response => {
        if (response.data.msg === MSG_OK) {
          this.contestList = response.data.result
        }
      }, response => {})
    },
    methods: {
      joinContest(contest){
        console.log('joinContest')
        this.curContest = contest
        this.$refs.contestDialog.show()
      }
    },
    computed: {
      ...mapGetters([
        'collectionList',
        'user'
      ])
    },
    watch: {
      user(newUser){
        if (newUser.user_id === null || newUser.user_id === '' || newUser.user_id === undefined) {
          this.$router.replace('/home')
        }
      }
    },
    components: {
      UserCard,
      MyProgress,
      AboutMe,
      CollectedTable,
      ContestTable,
      ContestDialog
    }
  }

</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .user-center
    margin-top 25px

  .bg-purple
    background: #d3dce6;

  .bg-purple-light
    background: #e5e9f2;

  .grid-content
    border-radius: 4px;
    min-height: 36px;

  .user-card
    border-radius 5px

</style>
