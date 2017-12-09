<template>
  <div class="problem-edit" v-show="showFlag">
    <div class="panel">
      <div class="panel-heading">
        <i class="el-icon-arrow-left" @click.stop="hide"></i>
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
                :options="officialEditorOptions">
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
            <el-checkbox-group v-model="form.checkedLanguageList">
              <el-checkbox v-for="(item,index) in Languages" :key="index" :label="item"></el-checkbox>
            </el-checkbox-group>
          </el-form-item>
          <div class="editor-wrapper">
            <div class="dropdown-wrapper">
              <el-dropdown class="language-dropdown" trigger="click" @command="handleCommandLangage"
                           @visible-change="dropdownChange"
                           menu-align="start">
                <el-button type="primary" size="small">{{selectLanguage}}<i
                  class="el-icon-caret-bottom el-icon--right"></i>
                </el-button>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item v-for="(item , index) in Languages" :key="index" :command="index">{{item}}
                  </el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>

              <el-dropdown menu-align="start" trigger="click" class="el-dropdown-theme" @command="handleCommandTheme">
                <el-button type="success" size="small">
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
                :options="templetEditorOptions">
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
        showFlag: false,
        form: {
          title: '',
          description: '',
          level: 1,
          tag: '',
          program: '',
          input: '', //输入
          output: '', //输出
          checkedLanguageList: ['C']  //选择了的语言
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
        officialEditorOptions: {
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
        templetEditorOptions: {
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
        templetJs: {value: 'javascript', text: 'JavaScript', defaultCode: ''},
        templetRuby: {value: 'ruby', text: 'Ruby', defaultCode: ''},
        templetGolang: {value: 'golang', text: 'Go', defaultCode: ''},
        initialTitle: ''
      }
    },
    methods: {
      clickBtn(){
        //把最后一次模板templet加上
        this.addCodeToTemplet()
        let array = this.pushALLTemplets()
        console.log(array)
        let resultTemplets = []
        for (let i = 0; i < this.form.checkedLanguageList.length; i++) {
          resultTemplets.push(array.find((item) => item.text === this.form.checkedLanguageList[i]))
        }
        this.isEdit ? this.reviseProblem(resultTemplets) : this.setupProblem(resultTemplets)
      },
      setupProblem(resultTemplets){
        let url = `${baseUrl}/problems`
        axios.post(url, this.createProblem(this.form.title, resultTemplets)).then(response => {
          if (response.data.msg === MSG_OK) {
            this.notifySuccess('创建题目成功！')
            //成功后清除数据
            this._clearAllData()
            this.$emit('editFinish')
          } else if (response.data.msg === MSG_NO) {
            this.notifyError(response.data.error)
          }
        }, response => {})
      },
      reviseProblem(resultTemplets){
        let url = `${baseUrl}/problems/${this.problem.id}`
        //this.form.title === this.initialTitle 相等证明标题并未修改过 不相等证明标题修改过
        if (this.form.title === this.initialTitle) {
          console.log('未改变标题')
          this.reviseProblemNoChangeTitle(url, resultTemplets)
        } else {
          this.reviseProblemChangeTitle(url, resultTemplets)
        }
      },
      reviseProblemNoChangeTitle(url, resultTemplets){
        axios.put(url, this.createProblem(null, resultTemplets)
        ).then(response => {
          if (response.data.msg === MSG_OK) {
            this.notifySuccess()
            //成功后清除数据
            this._clearAllData()
            this.$emit('editFinish')
          } else if (response.data.msg === MSG_NO) {
            this.notifyError(response.data.error)
          }
        }, response => {})
      },
      reviseProblemChangeTitle(url, resultTemplets){
        axios.put(url, this.createProblem(this.form.title, resultTemplets)).then(response => {
          if (response.data.msg === MSG_OK) {
            this.notifySuccess()
            //成功后清除数据
            this._clearAllData()
            this.$emit('editFinish')
          } else if (response.data.msg === MSG_NO) {
            this.notifyError(response.data.error)
          }
        }, response => {})
      },
      createProblem(title, resultTemplets){
        let Base64 = require('js-base64').Base64
        let tempProblem = {
          description: this.form.description,
          level: this.form.level + '',
          tag: this.form.tag,
          program: Base64.encode(this.form.program),
          code: JSON.stringify(resultTemplets),
          input: Base64.encode(this.form.input),
          output: Base64.encode(this.form.output)
        }
        if (title) {
          tempProblem.title = title
        }
        console.log('tempProblem')
        console.log(tempProblem)
        return tempProblem
      },
      notifySuccess(text = '修改题目成功！'){
        this.$notify({
          title: '成功',
          message: text,
          type: 'success'
        })
      },
      notifyError(error){
        this.$notify({
          title: '修改失败',
          message: error,
          type: 'error'
        })
      },
      _clearAllData(){
        //清除所有数据 回到默认状态
        this.form.title = ''
        this.form.description = ''
        this.form.level = 1
        this.form.tag = ''
        this.form.program = ''
        this.form.input = ''
        this.form.output = ''
        this.form.checkedLanguageList = ['C']
        this.code = ''
        this.selectTheme = editorThemes[0]
        this.selectLanguage = languages[0]
        this.templetEditorOptions.mode = this.editorModes[0]
        this.templetEditorOptions.theme = this.selectTheme
        this.templetC = {value: 'c', text: 'C', defaultCode: ''}
        this.templetCpp = {value: 'cpp', text: 'C++', defaultCode: ''}
        this.templetCsharp = {value: 'csharp', text: 'C#', defaultCode: ''}
        this.templetJava = {value: 'java', text: 'Java', defaultCode: ''}
        this.templetPython = {value: 'python3', text: 'Python3', defaultCode: ''}
        this.templetJs = {value: 'javascript', text: 'JavaScript', defaultCode: ''}
        this.templetRuby = {value: 'ruby', text: 'Ruby', defaultCode: ''}
        this.templetGolang = {value: 'golang', text: 'Go', defaultCode: ''}
        //最后清空vuex中的Templets
        this.setTemplets([])
      },
      handleCommandLangage(index) {
        //切换语言
        console.log('xuan ' + index)
        this.templetEditorOptions.mode = this.editorModes[index]
        this.selectLanguage = this.Languages[index]
        //如果之前(一次编辑中)写过code   那么code=之前的对应的templet的defaultCode
        let result = this.templets.find((item) => item && item.text === this.selectLanguage)
        if (result) {
          this.code = result.defaultCode
        } else {
          this.code = ''
        }
      },
      dropdownChange(isShow) {
        //当语言下拉菜单状态改变
        if (isShow) {
          //当语言下拉菜单展开
          this.addCodeToTemplet()
          //  这里有bug (showPromblemInfo获取了setTemplets 这里又修改了Templets )
          //   解决：在此之前 每个对应模板加入相应的的数据
          this.setTemplets(this.pushALLTemplets())
        }
      },
      pushALLTemplets(){
        //把所有模板集合成一个数组返回
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
      addCodeToTemplet(){
        //把code加入到当前选中的语言的 对应的语言模板的defaultCode中
        switch (this.selectLanguage) {
          case 'C':
            this.templetC.defaultCode = this.code
            break
          case 'C++':
            this.templetCpp.defaultCode = this.code
            break
          case 'C#':
            this.templetCsharp.defaultCode = this.code
            break
          case 'Java':
            this.templetJava.defaultCode = this.code
            break
          case 'Python3':
            this.templetPython.defaultCode = this.code
            break
          case 'JavaScript':
            this.templetJs.defaultCode = this.code
            break
          case 'Ruby':
            this.templetRuby.defaultCode = this.code
            break
          case 'Go':
            this.templetGolang.defaultCode = this.code
            break
        }
      },
      hide(){
        this.showFlag = false
        this._clearAllData()
        this.$emit('editFinish')
      },
      show(){
        this._clearAllData()
        this.showFlag = true
        //处于编辑题目模式 先展示出题目信息
        let url1 = `${baseUrl}/problems/${this.problem.id}`
        axios.get(url1).then(response => {
          if (response.data.msg === MSG_OK) {
            this.form.title = response.data.result[0].title
            this.initialTitle = response.data.result[0].title
            this.form.description = response.data.result[0].description
            this.form.level = response.data.result[0].level
            this.form.tag = response.data.result[0].tag
          }
        }, response => {})

        let url2 = `${baseUrl}/problems/${this.problem.id}/codes`
        axios.get(url2).then(response => {
          if (response.data.msg === MSG_OK) {
            console.log('setTemplets')
            //Templets后端捕获时出错
            this.setTemplets(response.data.result[0].code)
            this.changeTemplets()
          }
        }, response => {})

        this.getProblemStd()
      },
      getProblemStd(){
        let Base64 = require('js-base64').Base64
        let url = `${baseUrl}/problems/${this.problem.id}/std`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.form.input = Base64.decode(response.data.result[0].input)
            this.form.output = Base64.decode(response.data.result[0].output)
            this.form.program = Base64.decode(response.data.result[0].program)
            console.log(response.data.result[0])
          }
        }, response => {})
      },
      findAndAddTemp(lang){
        console.log(this.templets)
        //由于这里后端的json数据有误 所以暂时采用静态数据
//        let resultTemp =
//          this.templets.find((item) => {
//            if (item) {
//              item.text === lang
//            }
//          }) || null

        let resultTemp = null  //resultTemp静态设置为了null 所以模板选择了所有语言
        switch (lang) {
          case 'C':
            this.templetC = resultTemp || this.templetC
            this.form.checkedLanguageList.push(this.templetC.text)
            break
          case 'C++':
            this.templetCpp = resultTemp || this.templetCpp
            this.form.checkedLanguageList.push(this.templetCpp.text)
            break
          case 'C#':
            this.templetCsharp = resultTemp || this.templetCsharp
            this.form.checkedLanguageList.push(this.templetCsharp.text)
            break
          case 'Java':
            this.templetJava = resultTemp || this.templetJava
            this.form.checkedLanguageList.push(this.templetJava.text)
            break
          case 'Python3':
            this.templetPython = resultTemp || this.templetPython
            this.form.checkedLanguageList.push(this.templetPython.text)
            break
          case 'JavaScript':
            this.templetJs = resultTemp || this.templetJs
            this.form.checkedLanguageList.push(this.templetJs.text)
            break
          case 'Ruby':
            this.templetRuby = resultTemp || this.templetRuby
            this.form.checkedLanguageList.push(this.templetRuby.text)
            break
          case 'Go':
            this.templetGolang = resultTemp || this.templetGolang
            this.form.checkedLanguageList.push(this.templetGolang.text)
            break
        }
      },
      changeTemplets(){
        this.form.checkedLanguageList = []
        this.findAndAddTemp('C')
        this.findAndAddTemp('C++')
        this.findAndAddTemp('C#')
        this.findAndAddTemp('Java')
        this.findAndAddTemp('Python3')
        this.findAndAddTemp('JavaScript')
        this.findAndAddTemp('Ruby')
        this.findAndAddTemp('Go')
        try {
          this.code = this.templets.find((item) => item && item.text === this.selectLanguage).defaultCode
        } catch (error) {
          this.code = ''
        }
      },
      calcBtnText(){
        //计算btn的文字
        return this.isEdit ? '修改题目' : '创建题目'
      },
      handleCommandTheme(command){
        //修改主题
        this.templetEditorOptions.theme = command
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
              margin-left 205px
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
