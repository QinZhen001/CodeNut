<template>
  <div class="myeditor">
    <div class="myeditor-header">
      <el-dropdown trigger="click" @command="handleCommandLangage" menu-align="start">
        <el-button type="primary">{{selectLanguage}}<i class="el-icon-caret-bottom el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-for="(item , index) in Languages" :key="index" :command="index">{{item}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown trigger="click" class="el-dropdown-theme" @command="handleCommandTheme">
        <el-button type="primary">
          {{selectTheme}}<i class="el-icon-caret-bottom el-icon--right"></i>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-for="(item,index) in editorThemes" :key="index" :command="item">{{item}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>

      <el-dropdown trigger="click" class="el-dropdown-keyMap" @command="handleCommandKeyMap">
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
                :code="code"
                :options="editorOptions"
                @ready="onEditorReady"
                @focus="onEditorFocus"
                @change="onEditorCodeChange">
    </codemirror>
    <div class="myeditor-footer">
      <el-button type="success" class="submit-button">
        Submit<i class="el-icon-upload el-icon--right"></i>
      </el-button>
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
  import { editorThemes, keyMaps, editorModes, languages, templateCodes } from 'common/js/data'
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
        }
      }
    },
    methods: {
      onEditorReady(editor) {
        console.log('the editor is readied!', editor)
      },
      onEditorFocus(editor) {
        console.log('the editor is focus!', editor)
      },
      onEditorCodeChange(newCode) {
        console.log('this is new code', newCode)
        this.code = newCode
      },
      handleCommandLangage(command) {
        // 这里的command 是 index
        console.log('xuan ' + command)
        this.editorOptions.mode = this.editorModes[command]
        this.selectLanguage = this.Languages[command]
        this.code = this.templateCodes[command]
        console.log(this.editorOptions)
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
      }
    },
    computed: {
      editor() {
        return this.$refs.myEditor.editor
      }
    },
    mounted() {
      console.log('this is current editor object', this.editor)
      // you can use this.editor to do something...
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .myeditor
    margin-top 20px
    .myeditor-header
      padding 0 0 12px 30px
      .el-dropdown-theme
        float right
      .el-dropdown-keyMap
        float right
        margin-right 8px
    .CodeMirror
      height 400px
    .myeditor-footer
      padding 20px 0 0 0
      width 100%
      .submit-button
        float right
</style>
