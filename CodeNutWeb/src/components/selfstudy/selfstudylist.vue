<template>
  <div>
    <div class="list-block" v-for="(item,index) in selfStudyItems" :key="index">
      <h3 class="title">{{item.title}}</h3>
      <p class="description">{{item.description}}</p>
      <div class="footer">
        <span class="text">难度:</span>
        <el-rate
          class="difficulty"
          v-model="item.difficulty"
          disabled
          show-score
          text-color="#ff9900">
        </el-rate>
        <span class="attention">关注人数: {{item.attention}}</span>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { selfStudyItems } from 'common/js/data'

  export default{
    props: {
      selfStudyItems: {
        type: Array,
        default: selfStudyItems
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .list-block
    padding 0 10px
    padding-top 15px
    border-bottom 1px solid #ddd
    &:last-child
      border-bottom none
    .title
      margin-top 5px
      margin-bottom 10px
      &:hover
        cursor pointer
        color #FA5555
    .description
      margin-top 5px
      margin-bottom 5px
      line-height: 1.8;
      color: #999;
      font-size: 14px;
    .footer
      padding 0 10px 10px 20px
      .text
        margin-right 2px
        font-weight 500
        color: #555;
        font-family: "微软雅黑";
      .difficulty
        vertical-align: top;
        display inline-block
      .attention
        margin-left 80px
        color: #555;
        font-size 16px
        font-weight 500
        font-family: "微软雅黑";
</style>
