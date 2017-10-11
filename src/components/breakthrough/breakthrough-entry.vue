<template>
  <div class="entry-wrapper">
    <div class="listHead">
      <img width="32" height="32" src="static/challenge.png" class="imgTag"/>
      <p class="title1" @click="enterBreakThrough">闯关模式</p>
    </div>
    <img class="enter-img" src="static/breakthrough/planet_enter.png" width="128" height="128"
         @click="enterBreakThrough">
  </div>
</template>

<script type="text/ecmascript-6">
  export default{
    methods: {
      enterBreakThrough() {
        this.$router.push('/home/breakthrough')
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .entry-wrapper
    margin-top 30px
    .listHead
      margin-bottom 0
      height: 55px
      .imgTag
        vertical-align middle
      .title1
        margin-left 3px
        vertical-align: middle
        display inline-block
        font-size: 20px;
        font-weight: 500;
    .enter-img
      margin-top 20px
      margin-left 30px
    &:hover
      cursor pointer
</style>
