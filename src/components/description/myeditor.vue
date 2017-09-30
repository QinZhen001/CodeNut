<template>
  <div class="myeditor">
    <div class="myeditor-header">
      <el-dropdown trigger="click" @command="handleCommandLangage" menu-align="start" class="language-dropdown">
        <el-button type="primary">{{selectLanguage}}<i class="el-icon-caret-bottom el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-for="(item , index) in Languages" :key="index" :command="index">{{item}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown menu-align="start" trigger="click" class="el-dropdown-theme" @command="handleCommandTheme">
        <el-button type="primary">
          {{selectTheme}}<i class="el-icon-caret-bottom el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-for="(item,index) in editorThemes" :key="index" :command="item">{{item}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown menu-align="start" trigger="click" class="el-dropdown-keyMap" @command="handleCommandKeyMap">
        <el-button type="primary">
          {{selectkeyMap}}<i class="el-icon-caret-bottom el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-for="(item,index) in keyMaps" :key="index" :command="item">{{item}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
    <codemirror ref="myEditor"
                v-model="code"
                :options="editorOptions"
    >
    </codemirror>
    <div class="myeditor-footer">
      <el-button type="success" class="submit-button" @click="onClickSubmit">
        Submit<i class="el-icon-upload el-icon--right"></i>
      </el-button>
      <el-button type="primary" class="run-button" @click="onClickRun">Run
      </el-button>
    </div>

    <div class="result-wrapper" v-show="result!==[]"
         v-for="(item, index) in result" :key="index"
         v-loading.fullscreen.lock="fullscreenLoading" element-loading-text="正在运行中...">
      <div class="result-type">
        <el-tag type="success" v-show="item.mytitle === 'SubmitResult'">{{item.mytitle}}</el-tag>
        <el-tag type="warning" v-show="item.mytitle === 'RunResult'">{{item.mytitle}}</el-tag>
      </div>
      <span class="result-item">
        <span class="result-text">程序输出</span> {{item.output}}
      </span>
      <span class="result-item">
        <span class="result-text">耗费内存</span> {{item.memory_used}}
      </span>
      <span class="result-item">
        <span class="result-text">耗费时间</span> {{item.time_used}}
      </span>
      <span class="result-item">
        <span class="result-text">运行状态</span> {{item.status}}
      </span>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  // require active-line.js
  require('codemirror/addon/selection/active-line.js')

  // closebrackets
  require('codemirror/addon/edit/closebrackets.js')

  // styleSelectedText
  require('codemirror/addon/selection/mark-selection.js')
  require('codemirror/addon/search/searchcursor.js')

  // hint
  require('codemirror/addon/hint/show-hint.js')
  require('codemirror/addon/hint/javascript-hint.js')
  require('codemirror/addon/selection/active-line.js')

  // highlightSelectionMatches
  require('codemirror/addon/scroll/annotatescrollbar.js')
  require('codemirror/addon/search/matchesonscrollbar.js')
  require('codemirror/addon/search/searchcursor.js')
  require('codemirror/addon/search/match-highlighter.js')

  // keyMap
  require('codemirror/mode/clike/clike.js')
  require('codemirror/addon/edit/matchbrackets.js')
  require('codemirror/addon/comment/comment.js')
  require('codemirror/addon/dialog/dialog.js')
  require('codemirror/addon/dialog/dialog.css')
  require('codemirror/addon/search/searchcursor.js')
  require('codemirror/addon/search/search.js')
  require('codemirror/keymap/sublime.js')
  require('codemirror/keymap/emacs.js')
  require('codemirror/keymap/vim.js')

  // foldGutter
  require('codemirror/addon/fold/foldgutter.css')
  require('codemirror/addon/fold/brace-fold.js')
  require('codemirror/addon/fold/comment-fold.js')
  require('codemirror/addon/fold/foldcode.js')
  require('codemirror/addon/fold/foldgutter.js')
  require('codemirror/addon/fold/indent-fold.js')
  require('codemirror/addon/fold/markdown-fold.js')
  require('codemirror/addon/fold/xml-fold.js')

  // autoCloseTags
  require('codemirror/addon/edit/closetag.js')

  // 语法高亮，自行替换为你需要的语言
  import 'codemirror/mode/javascript/javascript'
  import 'codemirror/mode/go/go'
  import 'codemirror/mode/groovy/groovy'
  import 'codemirror/mode/python/python'

  // Theme
  import 'codemirror/theme/ambiance.css'
  import 'codemirror/theme/base16-dark.css'
  import 'codemirror/theme/cobalt.css'
  import 'codemirror/theme/paraiso-light.css'
  import 'codemirror/theme/paraiso-dark.css'
  import 'codemirror/theme/rubyblue.css'
  import 'codemirror/theme/solarized.css'
  import 'codemirror/theme/mbo.css'

  import { MSG_OK, MSG_NO, baseUrl, editorThemes, keyMaps, editorModes, languages, templateCodes } from 'common/js/data'
  import axios from 'axios'
  import { mapGetters } from 'vuex'
  import ReturnResult from 'common/js/ReturnResult'

  export default {
    data() {
      return {
        code: templateCodes[0],
        templateCodes: templateCodes,
        Languages: languages,
        editorModes: editorModes,
        selectLanguage: languages[0],
        editorThemes: editorThemes,
        selectTheme: editorThemes[0],
        keyMaps: keyMaps,
        selectkeyMap: keyMaps[0],
        editorOptions: {
          tabSize: 4,
          mode: 'text/x-csrc',
          theme: 'default',
          lineNumbers: true,
          line: true,
          keyMap: 'sublime',
          foldGutter: true,
          gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
          // 选中文本自动高亮，及高亮方式
          styleSelectedText: true,
          highlightSelectionMatches: {showToken: /\w/, annotateScrollbar: true}
          // 如果有hint方面的配置，也应该出现在这里
        },
        result: [],
        fullscreenLoading: false
      }
    },
    methods: {
      handleCommandLangage(command) {
        // 这里的command 是 index
        console.log('xuan ' + command)
        this.editorOptions.mode = this.editorModes[command]
        this.selectLanguage = this.Languages[command]
        this.code = this.templateCodes[command]
      },
      handleCommandKeyMap(command) {
        this.editorOptions.keyMap = command
        this.selectkeyMap = command
        console.log(this.editorOptions)
      },
      handleCommandTheme(command) {
        console.log('click on item ' + command)
        this.editorOptions.theme = command
        this.selectTheme = command
      },
      onClickSubmit(){
        this._checkLogin()
        let url = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.post(url, {
          language: this.selectLanguage,
          code: this.code
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.result.push(new ReturnResult({
              mytitle: 'SubmitResult',
              memory_used: response.data.result[0].memory_used.toFixed(4) + ' M',
              output: response.data.result[0].output,
              status: response.data.result[0].status,
              time_used: response.data.result[0].time_used.toFixed(4) + ' s'
            }))
            this._showLoading()
            console.log(this.result)
          } else if (response.data.mag === MSG_NO) {
            this.$notify.error({
              title: '错误',
              message: response.data.error
            })
          }
        }, response => {})
      },
      onClickRun(){
        this._checkLogin()
        let url = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.patch(url, {
          language: this.selectLanguage,
          code: this.code
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            this.result.push(new ReturnResult({
              mytitle: 'RunResult',
              memory_used: response.data.result[0].memory_used.toFixed(4) + ' M',
              output: response.data.result[0].output,
              status: response.data.result[0].status,
              time_used: response.data.result[0].time_used.toFixed(4) + ' s'
            }))
            this._showLoading()
            console.log(response.data.result[0])
          } else if (response.data.mag === MSG_NO) {
            this.$notify.error({
              title: '错误',
              message: response.data.error
            })
          }
        }, response => {})
      },
      _checkLogin(){
        if (this.user.user_id == null) {
          this.$notify({
            title: '警告',
            message: '请先登录！',
            type: 'warning'
          })
          return
        }
      },
      _showLoading() {
        this.fullscreenLoading = true
        setTimeout(() => {
          this.fullscreenLoading = false
        }, 2000)
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

<style lang="stylus" rel="stylesheet/stylus">
  .myeditor
    margin-top 20px
    .myeditor-header
      padding 0 0 12px 30px
      .language-dropdown
        .el-dropdown-menu__item
          padding 0 5px
      .el-dropdown-theme
        float right
      .el-dropdown-keyMap
        float right
        margin-right 8px
    .CodeMirror
      height 400px
    .myeditor-footer
      padding 20px 0 0 0
      height 100px
      width 100%
      .run-button
        float right
        margin-right 10px
        width 150px
      .submit-button
        float right
        width 150px
    .result-wrapper
      display flex
      margin-top -1px
      padding 10px 0
      border-bottom 1px solid #ddd
      border-top 1px solid #ddd
      .result-type
        flex 1 1 auto
        display inline-block
        .el-tag
          margin-top 4px
          font-size: 18px;
      .result-item
        flex 1 1 auto
        .result-text
          font-size 18px
          font-weight 600
          margin 0 5px
          line-height 30px
          color: #9E9E9E

</style>
