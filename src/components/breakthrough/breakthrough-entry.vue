<template>
  <div>
    <h3 @click="enterBreakThrough">闯关模式</h3>
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

<style lang="stylus" rel="stylesheet/stylus">

</style>
