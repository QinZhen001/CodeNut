<template>
  <transition name="el-fade-in">
    <div class="notes">
      <el-dialog title="保存笔记" :visible.sync="noteDialogVisible">
        <el-form ref="form" label-width="60px">
          <el-form-item label="文件名:">
            <el-input v-model="noteName"></el-input>
          </el-form-item>
          <el-radio-group v-model="fileType">
            <el-radio label="0">保存至云端</el-radio>
            <el-radio label="1">以txt格式保存</el-radio>
            <el-radio label="2">以markdown格式保存</el-radio>
          </el-radio-group>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="noteDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveNoteConfirm">保 存</el-button>
        </div>
      </el-dialog>
      <mavon-editor v-model="note" default_open="edit" placeholder="记录学习笔记"  @save="_showSaveNoteDialog">
      </mavon-editor>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import axios from 'axios'
  import { baseUrl, MSG_OK } from 'common/js/data'
  import { mapGetters } from 'vuex'

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
    created(){
      if (this._checkLogin()) {
        let url = `${baseUrl}/problems/${this.problem.id}/notes`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.note = response.data.result[0].text
          }
        }, response => {})
      }
    },
    methods: {
      _showSaveNoteDialog() {
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
        } else if (this.fileType === '0') {
          if (this.note === '' || this.note === undefined) {
            this.$notify({
              title: '警告',
              type: 'warning',
              message: '笔记不能为空哦!'
            })
          } else {
            if (this._checkLogin()) {
              this._saveNote()
            }
          }
        }
        this.noteDialogVisible = false
      },
      _saveNote(){
        let url = `${baseUrl}/problems/${this.problem.id}/notes`
        axios.put(url, {
          text: this.note
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.$notify({
              title: '成功',
              type: 'success',
              message: '保存笔记成功!'
            })
          }
        }, response => {
          this._saveNote()
        })
      },
      _checkLogin(){
        if (this.user.user_id == null) {
          this.$notify({
            title: '警告',
            message: '请先登录！',
            type: 'warning'
          })
          return false
        } else {
          return true
        }
      }
    },
    computed: {
      ...mapGetters([
        'problem',
        'user'
      ])
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .notes
    margin-top 25px
    height 590px
    .v-note-wrapper
      height 500px
</style>
