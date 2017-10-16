<template>
  <div class="entry-wrapper">
    <div class="entry-head" @click="enterBreakThrough">
      <img class="entry-head-img" width="32" height="32" src="static/challenge.png"/>
      <p class="entry-head-text">闯关模式</p>
    </div>
    <div class="entry-img-wrapper">
      <img class="enter-img" src="static/breakthrough/planet_enter.png" width="128" height="128"
           @click="enterBreakThrough">
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { mapGetters } from 'vuex'

  export default{
    methods: {
      enterBreakThrough() {
        if (this.user.user_id == null || this.user.user_id === '') {
          this.$notify({
            title: '请先登录',
            message: '无法进入闯关模式',
            type: 'error'
          })
          return
        }
        this.$router.push('/home/breakthrough')
      }
    },
    computed: {
      ...mapGetters([
        'user'
      ])
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .entry-wrapper
    width 100%
    margin-top 10px
    .entry-head
      height 65px
      .entry-head-img
        vertical-align middle
      .entry-head-text
        margin-left 3px
        vertical-align: middle
        display inline-block
        font-size: 20px;
        font-weight: 400;
    &:hover
      cursor pointer
    .entry-img-wrapper
      width 100%
      text-align center
      .enter-img
        margin-top 5px
      &:hover
        cursor pointer
</style>
