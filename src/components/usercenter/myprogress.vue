<template>
  <div class="progress">
    <div class="panel">
      <div class="panel-heading">
        <h3 class="panel-title">Your Progress</h3>
      </div>
      <div class="panel-body">
        <ul class="list-group">
          <li class="list-group-item">
            <img width="22" height="22" src="static/question.png" class="tag-img">Solved Question
            <el-tag type="success">0/662</el-tag>
          </li>
          <li class="list-group-item">
            <img width="22" height="22" src="static/setup.png" class="tag-img">Accepted Submission
            <el-tag type="success">0/0</el-tag>
          </li>
          <li class="list-group-item">
            <img width="22" height="22" src="static/yes.png" class="tag-img">Acceptance Rate
            <el-tag type="warning">0%</el-tag>
          </li>
        </ul>
        <div class="progresschart-wrapper">
          <progresschart></progresschart>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import Progresschart from 'common/js/progress'

  export default{
    components: {
      Progresschart
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .progress
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
        vertical-align bottom
        margin-top: 0;
        margin-bottom: 0;
        font-size: 16px;
        color: inherit;
        font-family: inherit;
        font-weight: 500;
        line-height: 1.1;
    .panel-body
      p
        margin 6px 0
      .list-group
        margin-top: 0;
        margin-bottom: 0;
        padding-left: 0;
        list-style none
        &:frist-child
          border-top-width: 0;
        .list-group-item
          border-radius: 0;
          position: relative;
          display: block;
          padding: 10px 15px;
          margin-bottom: -1px;
          background-color: #fff;
          border-width 1px 0
          border-style solid
          border-color #ddd
          .tag-img
            vertical-align bottom
            margin-right 8px
          .el-tag
            float: right
      .progresschart-wrapper
        margin 20px
</style>
