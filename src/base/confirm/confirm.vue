<template>
  <el-dialog
    title="提示"
    :visible.sync="visible">
    <span class="text">{{text}}</span>
    <span slot="footer" class="dialog-footer">
    <el-button @click="cancel">{{cancelBtnText}}</el-button>
    <el-button type="primary" @click="confirm">{{confirmBtnText}}</el-button>
  </span>
  </el-dialog>
</template>

<script type="text/ecmascript-6">
  export default{
    props: {
      text: {
        type: String,
        default: ''
      },
      confirmBtnText: {
        type: String,
        default: '确 定'
      },
      cancelBtnText: {
        type: String,
        default: '取 消'
      }
    },
    data(){
      return {
        visible: false
      }
    },
    methods: {
      show(){
        this.visible = true
      },
      hide(){
        this.visible = false
      },
      confirm(){
        this.hide()
        this.$emit('confirm')
      },
      cancel(){
        this.hide()
        this.$emit('cancel')
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .el-dialog
    .el-dialog__body
      padding 10px 20px
      .text
        font-size 18px
        font-weight 400
</style>
