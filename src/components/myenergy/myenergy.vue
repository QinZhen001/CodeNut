<template>
  <transition name="el-zoom-in-top">
    <div class="energy-wrapper">
      <div class="energy-title">
        <img width="32" height="32" src="static/energy.png" class="img-title"/>
        <p class="text-title">Capacity</p>
      </div>
      <div class="box-card">
        <div class="chart">
          <energychart></energychart>
        </div>
      </div>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import Energychart from 'common/js/energychart'

  export default {
    data() {
      return {}
    },
    components: {
      Energychart
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .energy-wrapper
    width 100%
    margin-top 10px
    .energy-title
      height 65px
      .img-title
        vertical-align: middle
      .text-title
        margin-left 3px
        vertical-align: middle
        display inline-block
        font-size: 20px;
        font-weight: 300;
    .box-card
      max-height 350px
      border 1px solid #EEF1F6
      .chart
        width 80%
        margin 0 auto
        #radar-chart
          max-height 280px
</style>
