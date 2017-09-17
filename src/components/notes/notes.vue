<template>
  <div class="notes">
    <el-dialog title="保存笔记" :visible.sync="noteDialogVisible">
      <el-form ref="form" label-width="60px">
        <el-form-item label="文件名:">
          <el-input v-model="noteName"></el-input>
        </el-form-item>
        <el-radio-group v-model="fileType">
          <el-radio label="1">Save as .txt</el-radio>
          <el-radio label="2">Save as .md</el-radio>
        </el-radio-group>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="noteDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveNoteConfirm">保 存</el-button>
      </div>
    </el-dialog>
    <mavon-editor v-model="note" default_open="edit" placeholder="记录学习笔记" :ishljs="true" @save="saveNote">
    </mavon-editor>
  </div>
</template>

<script type="text/ecmascript-6">
  export default{
    props: {
      name: String,
      default: 'CodeNut笔记'
    },
    data() {
      return {
        note: '',
        noteDialogVisible: false,
        fileType: '1',
        noteName: this.name + '笔记'
      }
    },
    methods: {
      saveNote() {
//        let FileSaver = require('file-saver')
//        console.log(this.note)
//        let blob = new Blob(['Hello, world!'], {type: 'text/plain;charset=utf-8'})
//        FileSaver.saveAs(blob, 'hello world.md')
        this.noteDialogVisible = true
      },
      saveNoteConfirm() {
        let FileSaver = require('file-saver')
        let blob = new Blob([this.note], {type: 'text/plain;charset=utf-8'})
        if (this.fileType === '1') {
          // Save as .txt
          FileSaver.saveAs(blob, this.noteName + '.txt')
        } else if (this.fileType === '2') {
          FileSaver.saveAs(blob, this.noteName + '.md')
        }
        this.noteDialogVisible = false
      }
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .notes
    margin-top 25px
    height 590px
    .v-note-wrapper
      height 500px
</style>
