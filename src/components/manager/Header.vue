<template>
  <div class="manager-header">
    <div class="logo">后台管理系统</div>
    <div class="user-info">
      <el-dropdown @command="handleCommand">
                <span class="el-dropdown-link">
                    <img class="user-logo" src="static/avatar.jpg" width="40px" height="40px">{{user.username}}
                </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="loginout">退出</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>


<script type="text/ecmascript-6">
  import { mapGetters, mapMutations } from 'vuex'
  import User from 'common/js/user'

  export default {
    methods: {
      handleCommand(command) {
        if (command === 'loginout') {
          let myuser = new User({})
          this.setProblem(myuser)
          this.$router.push('/home')
        }
      },
      ...mapMutations({
        setProblem: 'SET_PROBLEM'
      })
    },
    computed: {
      ...mapGetters([
        'user'
      ])
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manager-header
    position: relative;
    box-sizing: border-box;
    width: 100%;
    height: 70px;
    font-size: 22px;
    line-height: 70px;
    color: #fff;
    background-color #242F42
    .logo
      float: left;
      width: 250px;
      text-align: center;
    .user-info
      float: right;
      padding-right: 80px;
      font-size: 16px;
      color: #fff;
      .el-dropdown-link
        position: relative;
        display: inline-block;
        padding-left: 50px;
        color: #fff;
        cursor: pointer;
        vertical-align: middle;
        .user-logo
          position: absolute;
          left: 0;
          top: 15px;
          width: 40px;
          height: 40px;
          border-radius: 50%;
      .el-dropdown-menu__item
        text-align: center;

</style>
