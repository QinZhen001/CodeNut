<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="2" :sm="0" :lg="2" :md="2" :xs="0">
        <div class="grid-content bg-purple">
        </div>
      </el-col>

      <el-col :span="7" :sm="24" :lg="7" :md="7" :xs="24">
        <user-card></user-card>
        <about-me></about-me>
        <my-progress></my-progress>
      </el-col>

      <el-col :span="13" :sm="24" :lg="12" :md="12" :xs="24">
        <div class="grid-content bg-purple"></div>
      </el-col>

      <el-col :span="2" :sm="0" :lg="3" :md="3" :xs="0">
        <div class="grid-content bg-purple"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script type="text/ecmascript-6">
  import UserCard from 'components/usercenter/usercard'
  import MyProgress from 'components/usercenter/myprogress'
  import AboutMe from 'components/usercenter/aboutme'

  export default {
    data() {
      return {}
    },
    components: {
      UserCard,
      MyProgress,
      AboutMe
    }
  }

</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .bg-purple
    background: #d3dce6;

  .bg-purple-light
    background: #e5e9f2;

  .grid-content
    border-radius: 4px;
    min-height: 36px;


</style>
