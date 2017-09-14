<template>
  <div>
    <div class="description" v-html="data.description" v-if="data.description">
    </div>
    <my-editor></my-editor>
  </div>
</template>

<script type="text/ecmascript-6">
  //  import Editor from 'components/editor/vueeditor'
  import MyEditor from 'components/description/myeditor'

  export default {
    props: {
      data: {
        type: Object,
        default: {}
      }
    },
    components: {
      MyEditor
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .description
    border-bottom 1px solid #ddd
    p
      margin: 0 0 10px
      display: block;
      font-size: 16px;
      -webkit-margin-before: 1em;
      -webkit-margin-after: 1em;
      -webkit-margin-start: 0px;
      -webkit-margin-end: 0px;
    pre
      display: block;
      padding: 9.5px;
      margin: 0 0 10px;
      overflow: auto;
      font-size: 14px;
      line-height: 1.9;
      color: #333;
      word-break: break-all;
      word-wrap: break-word;
      background-color: #F2F2F2;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
    code
      padding: 2px 4px;
      font-size: 90%;
      color: #c7254e;
      background-color: #f9f2f4;
      border-radius: 4px;
      font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
    b
      font-weight: 700;
    ol
      margin-top: 10px;
      li
        font-size: 16px;

  .editor
    .ql-editor
      min-height 300px
</style>
