<template>
  <div class="editor">
    <div class="editor-wrapper">
      <quill-editor ref="myTextEditor" v-model="content" :config="editorOption"
                    spellcheck="false" dropzone="copy"></quill-editor>
    </div>
    <el-button class="editor-btn" type="primary" @click="submit">提交</el-button>
  </div>
</template>

<script>
  import { quillEditor } from 'vue-quill-editor'
  //  import Footer from 'components/myfooter/myfooter'

  export default {
    data: function () {
      return {
        content: '',
        editorOption: {
          // something config
        }
      }
    },
    methods: {
      onEditorChange({editor, html, text}) {
        this.content = html
      },
      submit() {
        console.log(this.content)
        this.$message.success('提交成功！')
      }
    },
    computed: {
      editor() {
        return this.$refs.myTextEditor.quillEditor
      }
    },
    components: {
      quillEditor
    }
  }
</script>
<style scoped lang="stylus" rel="stylesheet/stylus">
  .editor
    width 100%
    margin-top: 30px;
    .editor-wrapper
      width 100%
      .ql-editor
        min-height 250px
    .editor-btn
      margin-top: 20px;
      width 100px

</style>
