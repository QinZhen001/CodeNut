<template>
  <div>
    <el-dialog
      title="运行结果"
      :visible.sync="dialogVisible">
      <span slot="title"> {{result.status}}</span>
      <div class="dialog-container">
        <div class="explanation" v-text="getExplanation(result.status)"></div>
        <div class="text" v-html="result.output"></div>
      </div>
      <span slot="footer" class="dialog-footer">
         <el-button @click="dialogVisible = false">取 消</el-button>
         <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script type="text/ecmascript-6">
  import { results } from 'common/js/data'

  export default{
    props: {
      result: {
        type: Object

      }
    },
    data(){
      return {
        dialogVisible: false,
        results: results
      }
    },
    methods: {
      show(){
        this.dialogVisible = true
      },
      hide(){
        this.dialogVisible = false
      },
      getExplanation(status){
        let res = this.results.find((item) => {
          return item.name === status
        })
        if (res) {
          return res.value
        } else {
          return ''
        }
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .dialog-container
    .explanation
      font-size 18px
      font-weight 500
      color #222
      margin-bottom 10px
    .text
      font-size 14px
      text-align justify
</style>
