<template>
  <div class="manger-center">
    <v-head></v-head>
    <v-sidebar></v-sidebar>
    <div class="content">
      <transition name="move" mode="out-in">
        <router-view></router-view>
      </transition>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import vHead from './Header.vue'
  import vSidebar from './Sidebar.vue'
  import { mapGetters } from 'vuex'

  export default {
    computed: {
      ...mapGetters([
        'user'
      ])
    },
    watch: {
      user: function (newUser) {
        console.log('发现newUser')
        console.log(newUser)
        if (newUser.user_id == null || newUser.username == null) {
          this.$router.push('/home')
        }
      }
    },
    components: {
      vHead, vSidebar
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
