<template>
  <div class="myfooter">
    <div class="footer-wrapper">
      <span class="footer-text-up">Copyright © 2017 CodeNut</span>
      <div class="line-wrapper">
        <div class="line"></div>
      </div>
      <span class="footer-text-down">从小白到大神,一步一个脚印</span>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

</script>

<style lang="stylus" rel="stylesheet/stylus">
  .myfooter
    z-index -1
    flex: 0 0 auto;
    margin-top 20px
    width 100%
    height 100px
    background-color #202020
    vertical-align: middle;
    .footer-wrapper
      height 80px
      width 500px
      margin auto auto
      padding-top 1rem
      .footer-text-up
        margin-top 5px
        text-align center
        display block
        opacity: 0.64;
        font-weight: 300;
        font-size: 0.92rem;
        letter-spacing: 0.02rem;
        line-height: 1.72rem;
        color whitesmoke
      .line-wrapper
        height 2px
        width 100%
        border-bottom 1px solid whitesmoke
      .footer-text-down
        display block
        opacity: 0.64;
        text-align center
        font-weight: 300;
        font-size: 1rem;
        letter-spacing: 0.02rem;
        line-height: 1.72rem;
        color whitesmoke
</style>
