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
      <el-button type="success" class="custom-button" @click="onClickCustom">
        Custom<i class="el-icon-upload el-icon--right"></i>
      </el-button>
      <el-button type="success" class="submit-button" @click="onClickSubmit">
        Submit<i class="el-icon-upload el-icon--right"></i>
      </el-button>
      <el-button type="primary" class="run-button" @click="onClickRun">Run
      </el-button>
    </div>

    <div class="result-wrapper" v-show="returnResults.length>0"
         v-for="(item, index) in returnResults" :key="index"
         v-loading.fullscreen.lock="fullscreenLoading" element-loading-text="正在运行中...">
      <div class="result-type">
        <el-tag type="success" v-show="item.mytitle === 'SubmitResult'">{{item.mytitle}}</el-tag>
        <el-tag type="warning" v-show="item.mytitle === 'RunResult'">{{item.mytitle}}</el-tag>
      </div>
      <!--<span class="result-item">-->
      <!--<span class="result-item-text">程序输出</span> {{item.output}}-->
      <!--</span>-->
      <span class="result-item">
        <span class="result-item-text">耗费内存:</span> {{item.memory_used}}
      </span>
      <span class="result-item">
        <span class="result-item-text">耗费时间:</span> {{item.time_used}}
      </span>
      <span class="result-item">
        <span class="result-item-text">运行状态:
          <span :class="[item.status.includes('Error')?'error':'default']"> {{item.status}}</span>
        </span>
         <img class="result-item-img" src="static/target.png" width="32" height="32"
              v-show="index === (returnResults.length-1)">
      </span>
    </div>
    <run-result-dialog ref="dialog" v-if="returnResults"
                       :content="returnResults[returnResults.length-1]"></run-result-dialog>
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
  import 'codemirror/mode/python/python'
  import 'codemirror/mode/ruby/ruby'
  import 'codemirror/mode/clike/clike'

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
  import { mapGetters, mapMutations } from 'vuex'
  import ReturnResult from 'common/js/ReturnResult'

  //组件
  import RunResultDialog from 'components/description/runresultdialog'

  export default {
    data() {
      return {
        code: '',
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
        returnResults: [],
        fullscreenLoading: false
      }
    },
    created(){
      this._getTempletCode(this.selectLanguage)
    },
    methods: {
      handleCommandLangage(command) {
        // 这里的command 是 index
        console.log('xuan ' + command)
        this.editorOptions.mode = this.editorModes[command]
        this.selectLanguage = this.Languages[command]
        this._getTempletCode(this.selectLanguage)
      },
      _getTempletCode(selectLanguage){
        let url = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.get(url).then(response => {
          let result
          try {
            result = JSON.parse(response.data.result[0].code)
            let templet = result.find((item) => {
              return item.text === selectLanguage
            })
            if (templet && templet.defaultCode) {
              this.code = templet.defaultCode
            } else {
              this.code = this.templateCodes.find((item) => {
                return item.text === selectLanguage
              }).defaultCode
            }
          } catch (error) {
            //后端抓取的json数据 格式有问题 所以肯定会catch到error
            console.log(error)
            this.code = this.templateCodes.find((item) => {
              return item.text === selectLanguage
            }).defaultCode
          }
        }, response => {})
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
      getReturnResult(title, returnResult){
        return new ReturnResult({
          mytitle: title,
          memory_used: returnResult.memory_used.toFixed(2) + 'kb',
          output: returnResult.output,
          status: returnResult.status,
          time_used: returnResult.time_used.toFixed(2) + 's'
        })
      },
      onClickSubmit(){
        if (!this._checkLogin()) {
          return
        }
        let url = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.post(url, {
          language: this.selectLanguage,
          code: this.code
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            console.log(response.data.result[0])
            this.checkBreakthrough(this.getReturnResult('SubmitResult', response.data.result[0]))
          } else if (response.data.mag === MSG_NO) {
            this.showError(response.data.error)
          }
        }, response => {
          this.showError()
        })
      },
      onClickRun(){
        if (!this._checkLogin()) {
          return
        }
        console.log(this.code)
        let url = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.patch(url, {
          language: this.selectLanguage,
          code: this.code
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            console.log(response.data.result[0])
            this.checkBreakthrough(this.getReturnResult('RunResult', response.data.result[0]))
          } else if (response.data.mag === MSG_NO) {
            this.showError(response.data.error)
          }
        }, response => {
          this.showError()
        })
      },
      /**
       * checkBreakthrough() 闯关模式逻辑并未设计好 这里只是展示效果
       */
      checkBreakthrough(returnResult){
        if (this.breakthrough) {
          //当前处于闯关模式 不会触发returnResults.push 结果数组不会变化
          console.log('当前处于闯关模式')
          this.$router.push('/home/problem/success-animation')
          this.setBreakThrough(false)
        } else {
          //当前不处于闯关模式
          console.log('当前处不于闯关模式')
          this._showLoading()
          setTimeout(() => {
            this.$refs.dialog.show()
            this.returnResults.push(returnResult)
          }, 1000)
          this.setBreakThrough(false)
        }
      },
      showError(error = 'INTERNAL SERVER ERROR'){
        this.$notify.error({
          title: '错误',
          message: error
        })
      },
      onClickCustom(){
        let url = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            let str = JSON.parse(response.data.result[0].code)
            console.log(str)
          }
        }, response => {})
      },
      _checkLogin(){
        if (this.user.user_id === null || this.user.user_id === undefined || this.user.user_id === '') {
          this.$notify({
            title: '警告',
            message: '请先登录！',
            type: 'warning'
          })
          return false
        } else {
          return true
        }
      },
      _showLoading() {
        this.fullscreenLoading = true
        setTimeout(() => {
          this.fullscreenLoading = false
        }, 1000)
      },
      ...mapMutations({
        setBreakThrough: 'SET_BREAKTHROUGH'
      })
    },
    computed: {
      ...mapGetters([
        'problem',
        'user',
        'breakthrough'
      ])
    },
    components: {
      RunResultDialog
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .myeditor
    margin-top 20px
    .myeditor-header
      margin-bottom 12px
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
      .custom-button
        float left
        margin-right 10px
        width 150px
      .run-button
        float right
        margin-right 10px
        width 150px
      .submit-button
        float right
        width 150px
    .result-wrapper
      display flex
      height 30px
      padding 7px 0
      border-bottom 1px solid #bbb
      .result-type
        flex 0 1 auto
        display inline-block
        .el-tag
          margin-top 4px
          font-size: 18px;
      .result-item
        flex 1 1 auto
        text-align center
        .result-item-text
          font-size 18px
          margin 0 5px
          line-height 30px
          color: #9E9E9E
          .error
            color #ff1744
          .default
            color #333
      .result-item-img
        vertical-align top
</style>
