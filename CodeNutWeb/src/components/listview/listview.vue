<template>
  <div class="list-wrapper">
    <div class="list-head">
      <img class="list-head-img" src="static/fire.png">
      <p class="list-head-text">Top Hits</p>
    </div>
    <div class="container">
      <ul class="list">
        <li v-for="item in hotHits" class="item">
          <img width="20" height="20" src="static/item.png" class="imgItem">
          <p class="itemName">{{item}}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { hotKeys } from 'common/js/data'

  export default {
    data() {
      return {
        hotHits: hotKeys
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .list-wrapper
    margin-top 10px
    .list-head
      height 65px
      .list-head-img
        vertical-align middle
      .list-head-text
        margin-left 3px
        vertical-align: middle
        display inline-block
        font-size: 20px;
        font-weight: 300;

    .container
      margin-top: 0
      .list
        margin-top 0
        padding-left 20px
        list-style: none
        .item
          padding 2px
          height 30px
          &:first-child
            padding 0 2px 2px 2px
          .imgItem
            vertical-align: middle
          .itemName
            margin-left 5px
            display inline-block
            vertical-align: middle
            font-weight: 500
            color: #3c4859
            font-size: 14px
</style>
