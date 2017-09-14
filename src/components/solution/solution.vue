<template>
  <div>
    <div class="solution" v-if="data.solution" v-html="data.solution">
    </div>
    <div class="nodata" v-show="!data.solution || data.solution === {}">
      No solution at the moment
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    props: {
      data: {
        type: Object,
        default: {}
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .solution
    line-height: 1.7;
    .toc
      display: table;
      border: 1px solid #aaa;
      background-color: #f9f9f9;
      padding: 7px 25px 3px 7px;
      margin-top: 50px;
      font-size: 95%;
      ul
        margin-top: 0;
        margin-bottom: 10px;
      a
        color: #08c;
        text-decoration: none;
    h2
      font-size: 1.75em;
      font-weight: 700;
      margin-top: 1.275em;
      margin-bottom: .85em;
      line-height: 1.7;
    h4
      font-size: 1.25em;
      font-weight: 700;
      margin-top: 1.275em;
      margin-bottom: .85em;
      line-height: 1.7;
    hr
      height: 4px;
      padding: 0;
      margin: 1.7em 0;
      overflow: hidden;
      background-color: #e7e7e7;
      border: none;
    p
      margin: 0 0 10px;
      display: block;
      -webkit-margin-before: 1em;
      -webkit-margin-after: 1em;
      -webkit-margin-start: 0px;
      -webkit-margin-end: 0px;
      font-size 16px
    code
      padding: 2px 4px;
      font-size: 90%;
      color: #c7254e;
      background-color: #f9f2f4;
      border-radius: 4px;
    b, strong
      font-weight: 700;
    pre
      margin: 0 0 1.275em;
      padding: .85em 1em;
      overflow-x: auto;
      word-wrap: normal;
      white-space: pre;
      display: block;
      font-size: 13px;
      line-height: 1.42857143;
      color: #333;
      word-break: break-all;
      background-color: #f5f5f5;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
      .nf
        color: #900;
        font-weight: bold;
      .na
        color: teal;
      .kt
        color: #458;
        font-weight: bold;
      .o
        font-weight: bold;

  .nodata
    padding: 8rem 4rem;
    text-align: center;
    font-size: 1.5rem;
    color: #dadada;
</style>
