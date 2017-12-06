<template>
  <div class="manger-center">
    <manage-header></manage-header>
    <manage-sidebar></manage-sidebar>
    <div class="content">
      <transition name="el-fade-in-linear">
        <router-view></router-view>
      </transition>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import ManageHeader from './manage-header.vue'
  import ManageSidebar from './manage-sidebar.vue'
  import { mapGetters } from 'vuex'

  export default {
    computed: {
      ...mapGetters([
        'user'
      ])
    },
    components: {
      ManageHeader,
      ManageSidebar
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manger-center
    position fixed
    left 0
    right 0
    top 0
    bottom 0
    background-color #F2F2F2
    .content
      background: none repeat scroll 0 0 #fff;
      position: absolute;
      left: 250px;
      right: 0;
      top: 70px;
      bottom: 0;
      width: auto;
      padding: 40px;
      box-sizing: border-box;
      overflow-y: scroll;
      z-index 300
</style>
