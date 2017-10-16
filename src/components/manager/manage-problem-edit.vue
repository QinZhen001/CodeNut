<template>
  <div class="problem-edit">
    <div class="panel">
      <div class="panel-heading">
        <i class="el-icon-arrow-left" @click.stop="quit"></i>
        <h3 class="panel-title" v-show="!isEdit">创建题目</h3>
        <h3 class="panel-title" v-show="isEdit">修改题目(ID:{{problem.id}})</h3>
        <el-tag class="quit-tag" type="danger" @click.native.stop="quit">退出</el-tag>
      </div>
      <div class="panel-body">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="题目标题">
            <el-input class="short-input" v-model="form.title" spellcheck="false" size="small"></el-input>
          </el-form-item>
          <el-form-item label="题目标签">
            <el-input class="short-input" v-model="form.tag" spellcheck="false" size="small"></el-input>
          </el-form-item>
          <el-form-item label="题目难度">
            <el-radio-group v-model="form.level">
              <el-radio :label="1">1</el-radio>
              <el-radio :label="2">2</el-radio>
              <el-radio :label="3">3</el-radio>
              <el-radio :label="4">4</el-radio>
              <el-radio :label="5">5</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="题目描述">
            <mavon-editor v-model="form.description" default_open="edit" :toolbars="toolbars">
            </mavon-editor>
          </el-form-item>
          <el-form-item label="官方程序代码">
            <div class="program-edit">
              <codemirror
                class="program-edit-inner"
                v-model="form.program"
                :options="editorOptions1">
              </codemirror>
            </div>
          </el-form-item>
          <el-form-item label="输入样例">
            <el-input v-model="form.input" spellcheck="false"
                      type="textarea" :rows="5" placeholder="Enter a sample input testcase"></el-input>
          </el-form-item>
          <el-form-item label="输出样例">
            <el-input v-model="form.output" spellcheck="false"
                      type="textarea" :rows="5" placeholder="Enter a sample output testcase"></el-input>
          </el-form-item>
          <el-form-item label="模板选择">
            <el-checkbox-group v-model="form.checkLanguageList">
              <el-checkbox v-for="(item,index) in Languages" :key="index" :label="item"></el-checkbox>
            </el-checkbox-group>
          </el-form-item>
          <div class="editor-wrapper">
            <div class="dropdown-wrapper">
              <el-dropdown class="language-dropdown" trigger="click" @command="handleCommandLangage"
                           @visible-change="dropdownChange"
                           menu-align="start">
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
            </div>
            <div class="editor">
              <codemirror
                ref="myEditor"
                v-model="code"
                :options="editorOptions2">
              </codemirror>
            </div>
            <el-button class="setup-btn" @click="clickBtn"
                       type="success" v-text="calcBtnText()">
            </el-button>
          </div>
        </el-form>
      </div>
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

  import { mapGetters, mapMutations } from 'vuex'
  import { languages, editorThemes, editorModes, baseUrl, MSG_OK, MSG_NO } from 'common/js/data'
  import axios from 'axios'

  export default{
    props: {
      isEdit: {
        type: Boolean,
        default: false
      }
    },
    data(){
      return {
        form: {
          title: '',
          description: '',
          level: 1,
          tag: '',
          program: '',
          input: '',
          output: '',
          checkLanguageList: ['C']
        },
        toolbars: {
          bold: true, // 粗体
          italic: true, // 斜体
          header: true, // 标题
          underline: true, // 下划线
          strikethrough: true, // 中划线
          mark: true, // 标记
          quote: true, // 引用
          ol: true, // 有序列表
          ul: true, // 无序列表
          link: true, // 链接
          code: true, // code
          table: true, // 表格
          undo: true, // 上一步
          redo: true, // 下一步
          trash: true, // 清空
          alignleft: true, // 左对齐
          aligncenter: true, // 居中
          alignright: true, // 右对齐
          preview: true// 预览
        },
        editorOptions1: {
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
        editorOptions2: {
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
        editorThemes: editorThemes,
        selectTheme: editorThemes[0],
        Languages: languages,
        selectLanguage: languages[0],
        editorModes: editorModes,
        code: '',
        templetC: {value: 'c', text: 'C', defaultCode: ''},
        templetCpp: {value: 'cpp', text: 'C++', defaultCode: ''},
        templetCsharp: {value: 'csharp', text: 'C#', defaultCode: ''},
        templetJava: {value: 'java', text: 'Java', defaultCode: ''},
        templetPython: {value: 'python3', text: 'Python3', defaultCode: ''},
        templetJs: {value: 'javascript', text: 'Javascript', defaultCode: ''},
        templetRuby: {value: 'ruby', text: 'Ruby', defaultCode: ''},
        templetGolang: {value: 'golang', text: 'Go', defaultCode: ''}
      }
    },
    methods: {
      quit(){
        this.$emit('editFinish')
      },
      clickBtn(){
        let Base64 = require('js-base64').Base64
        this._addTemplet()
        let array = this._pushALLTemplets()
        console.log(array)
        let resultTemplets = []
        for (let i = 0; i < this.form.checkLanguageList.length; i++) {
          resultTemplets.push(array.find((item) => item.text === this.form.checkLanguageList[i]))
        }
        //console.log(resultTemplets)
        console.log(this.isEdit)

        if (this.isEdit) {
          //修改题目
          console.log('修改题目')
          this.reviseProblem(Base64, resultTemplets)
        } else {
          //创建题目
          this.setupProblem(Base64, resultTemplets)
        }
      },
      setupProblem(Base64, resultTemplets){
        let url = `${baseUrl}/problems`
        axios.post(url, {
          title: this.form.title,
          description: this.form.description,
          level: this.form.level + '',
          tag: this.form.tag,
          program: Base64.encode(this.form.program),
          code: JSON.stringify(resultTemplets),
          input: Base64.encode(this.form.input),
          output: Base64.encode(this.form.output)
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            //最后清空vuex中的Templets
            this.setTemplets([])
            this.$notify({
              title: '成功',
              message: `成功创建题目:${response.data.result[0].title}`,
              type: 'success'
            })
            //成功后清除表格数据
            this._clearFormData()
            this.$emit('editFinish')
          } else if (response.data.msg === MSG_NO) {
            this.$notify({
              title: '创建失败',
              message: `${response.data.error}`,
              type: 'error'
            })
          }
        }, response => {})
      },
      reviseProblem(Base64, resultTemplets){
        let url = `${baseUrl}/problems/${this.problem.id}`
        axios.put(url, {
          title: this.form.title,
          description: this.form.description,
          level: this.form.level + '',
          tag: this.form.tag,
          program: Base64.encode(this.form.program),
          code: JSON.stringify(resultTemplets),
          input: Base64.encode(this.form.input),
          output: Base64.encode(this.form.output)
        }).then(response => {
          if (response.data.msg === MSG_OK) {
            //最后清空vuex中的Templets
            this.setTemplets([])
            this.$notify({
              title: '成功',
              message: '修改题目成功',
              type: 'success'
            })
            //成功后清除表格数据
            this._clearFormData()
            this.$emit('editFinish')
          } else if (response.data.msg === MSG_NO) {
            this.$notify({
              title: '修改失败',
              message: `${response.data.error}`,
              type: 'error'
            })
          }
        }, response => {})
      },
      _clearFormData(){
        this.form.title = ''
        this.form.description = ''
        this.form.level = 1
        this.form.tag = ''
        this.form.program = ''
        this.form.input = ''
        this.form.output = ''
        this.form.checkLanguageList = ['C']
      },
      handleCommandLangage(index) {
        console.log('xuan ' + index)
        this.editorOptions2.mode = this.editorModes[index]
        this.selectLanguage = this.Languages[index]
        this.code = this.templets.find((item) => item.text === this.selectLanguage).defaultCode
      },
      dropdownChange(isShow) {
        if (isShow) {
          this._addTemplet()
          this.setTemplets(this._pushALLTemplets())
        }
      },
      _pushALLTemplets(){
        let result = []
        result.push(this.templetC)
        result.push(this.templetCpp)
        result.push(this.templetCsharp)
        result.push(this.templetJava)
        result.push(this.templetPython)
        result.push(this.templetJs)
        result.push(this.templetRuby)
        result.push(this.templetGolang)
        return result
      },
      _addTemplet(){
        if (this.selectLanguage === this.templetC.text) {
          this.templetC.defaultCode = this.code
        } else if (this.selectLanguage === this.templetCpp.text) {
          this.templetCpp.defaultCode = this.code
        } else if (this.selectLanguage === this.templetCsharp.text) {
          this.templetCsharp.defaultCode = this.code
        } else if (this.selectLanguage === this.templetJava.text) {
          this.templetJava.defaultCode = this.code
        } else if (this.selectLanguage === this.templetPython.text) {
          this.templetPython.defaultCode = this.code
        } else if (this.selectLanguage === this.templetJs.text) {
          this.templetJs.defaultCode = this.code
        } else if (this.selectLanguage === this.templetRuby.text) {
          this.templetRuby.defaultCode = this.code
        } else if (this.selectLanguage === this.templetGolang.text) {
          this.templetGolang.defaultCode = this.code
        }
      },
      showPromblemInfo(){
        this.form.title = this.problem.title
        this.form.description = this.problem.description
        this.form.level = this.problem.level
        this.form.tag = this.problem.tag
      },
      calcBtnText(){
        if (this.isEdit) {
          return '修改题目'
        } else {
          return '创建题目'
        }
      },
      handleCommandTheme(command) {
        console.log('click on item ' + command)
        this.editorOptions2.theme = command
        this.selectTheme = command
      },
      ...mapMutations({
        setTemplets: 'SET_TEMPLETS'
      })
    },
    computed: {
      ...mapGetters([
        'problem',
        'templets'
      ])
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">

  .problem-edit
    .panel
      border-radius: 5px;
      margin-bottom: 20px;
      background-color: #fff;
      border: 1px solid #ddd;
      -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
      box-shadow: 0 1px 1px rgba(0, 0, 0, .05);
      .panel-heading
        padding: 10px 15px;
        color: #333;
        background-color: #f5f5f5;
        border-color: #ddd;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        border-bottom: 1px solid transparent;
        .el-icon-arrow-left
          color: lightsteelblue
          &:hover
            cursor pointer
        .panel-title
          display inline-block
          margin-left 5px
          margin-top 0
          margin-bottom 0
          font-size: 18px;
          color: inherit;
          font-weight: 500;
          line-height: 1.1;
        .quit-tag
          float right
          &:hover
            cursor pointer
      .panel-body
        padding: 15px 45px;
        .el-form
          .el-form-item
            margin-right 10%
            .program-edit
              display inline-block
              width 83%
              border 1px solid #ddd
            .short-input
              width 50%
          .editor-wrapper
            position relative
            .dropdown-wrapper
              position absolute
              top: 0
              left 0
              display inline-block
              .language-dropdown
                margin-right 5px
            .editor
              margin-left 200px
              display inline-block
              width 70%
              border 1px solid #ddd
              .CodeMirror
                height 330px
            .setup-btn
              position relative
              left 10px
              bottom 10px
</style>
