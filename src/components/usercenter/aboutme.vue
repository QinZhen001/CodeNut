<template>
  <div class="about-me">
    <div class="panel">
      <div class="panel-heading">
        <h3 class="panel-title">About Me</h3>
      </div>
      <div class="panel-body">
        <p class="about-me-text">
          仰望星空,脚踏星空</p>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">

</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .about-me
    margin-top 20px
    .panel
      border-radius: 5px
      border 1px solid #ddd
      margin-bottom: 20px;
      background-color: #F5F5F5
      -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
      box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
    .panel-heading
      padding: 10px 15px;
      background-color: #ddd;
      border-bottom 1px solid #ddd;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      .panel-title
        margin-top: 0;
        margin-bottom: 0;
        font-size: 16px;
        color: inherit;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.1;
    .panel-body
      padding: 15px;
      .about-me-text
        word-wrap: break-word;
        word-break: normal;
</style>
