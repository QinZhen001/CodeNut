webpackJsonp([10],{"+bOk":function(e,t){},"+fg7":function(e,t){},"0tbE":function(e,t){},"1XTk":function(e,t){},"2b9r":function(e,t){},"38HL":function(e,t){},"4/hK":function(e,t){},"8sUU":function(e,t){},"95Re":function(e,t,n){"use strict";var s=n("woo5"),i=n("QfH/"),o=n("VU/8"),r=o(s.a,i.a,null,null,null);t.a=r.exports},"9ozf":function(e,t){},BEen:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=n("BJxZ"),i=n("O5KI"),o=n("VU/8"),r=o(s.a,i.a,null,null,null);t.default=r.exports},BJxZ:function(e,t,n){"use strict";var s=n("pFYg"),i=n.n(s);window.CodeMirror=n("8U58"),n("4/hK"),n("+fCR"),t.a={name:"codemirror",data:function(){return{content:""}},props:{code:String,value:String,unseenLines:Array,marker:Function,loadtheme:{type:Boolean,default:function(){return!0}},debugger:{type:Boolean,default:function(){return!0}},options:{type:Object,required:!0}},created:function(){void 0===this.options.lineNumbers&&(this.options.lineNumbers=!0),void 0===this.options.lineWrapping&&(this.options.lineWrapping=!1),void 0===this.options.mode&&(this.options.mode="text/javascript");var e=this.options.theme,t=this.options.mode,s=this.debugger,o=this.loadtheme,r=!!CodeMirror.modes[t];if(e&&"solarized light"==e&&(e="solarized"),"string"==typeof t){var a=CodeMirror.findModeByMIME(t);t=a?a.mode:a}else if("object"==(void 0===t?"undefined":i()(t)))if(t.name){var a=CodeMirror.findModeByName(t.name);t=a?a.mode:null}else if(t.ext){var a=CodeMirror.findModeByExtension(t.ext);t=a?a.mode:null}else if(t.mime){var a=CodeMirror.findModeByMIME(t.mime);t=a?a.mode:null}else if(t.filename){var a=CodeMirror.findModeByFileName(t.filename);t=a?a.mode:null}t&&"null"!=t||!s||r||console.warn("CodeMirror language mode: "+t+" configuration error (CodeMirror语言模式配置错误，或者不支持此语言) See http://codemirror.net/mode/ for more details."),t&&"null"!==t&&n("ENpB")("./"+t+"/"+t+".js"),e&&o&&n("aHkt")("./"+e+".css")},mounted:function(){var e=this;this.editor=CodeMirror.fromTextArea(this.$el,this.options),this.editor.setValue(this.code||this.value||this.content),this.editor.on("change",function(t){e.content=t.getValue(),e.$emit&&(e.$emit("change",e.content),e.$emit("input",e.content))});for(var t=["changes","beforeChange","cursorActivity","keyHandled","inputRead","electricInput","beforeSelectionChange","viewportChange","swapDoc","gutterClick","gutterContextMenu","focus","blur","refresh","optionChange","scrollCursorIntoView","update"],n=t.length-1;n>=0;n--)!function(t){e.editor.on(t,function(n,s,i){e.$emit(t,n,s,i)})}(t[n]);this.$emit("ready",this.editor),this.unseenLineMarkers(),window.setTimeout(function(){e.editor.refresh()},0)},beforeDestroy:function(){var e=this.editor.doc.cm.getWrapperElement();e&&e.remove&&e.remove()},watch:{options:{deep:!0,handler:function(e,t){var n;for(n in e)this.editor.setOption(n,e[n])}},code:function(e,t){if(e!==this.editor.getValue()){var n=this.editor.getScrollInfo();this.editor.setValue(e),this.content=e,this.editor.scrollTo(n.left,n.top)}this.unseenLineMarkers()},value:function(e,t){if(e!==this.editor.getValue()){var n=this.editor.getScrollInfo();this.editor.setValue(e),this.content=e,this.editor.scrollTo(n.left,n.top)}this.unseenLineMarkers()}},methods:{refresh:function(){this.editor.refresh()},unseenLineMarkers:function(){var e=this;void 0!==e.unseenLines&&void 0!==e.marker&&e.unseenLines.forEach(function(t){var n=e.editor.lineInfo(t);e.editor.setGutterMarker(t,"breakpoints",n.gutterMarkers?null:e.marker())})}}}},BR0Y:function(e,t){},DEaM:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"myhead"},[n("div",{staticClass:"meun-wrapper"},[n("img",{staticClass:"logo",attrs:{width:"146",height:"38",src:"static/logo.png"},on:{click:e.clickLogo}}),e._v(" "),n("el-menu",{staticClass:"menu",attrs:{theme:"dark",mode:"horizontal"},on:{select:e.handleSelect}},[e._l(e.headrs,function(t,s){return n("el-menu-item",{key:s,attrs:{index:t}},[e._v(e._s(t)+"\n      ")])}),e._v(" "),n("transition",{attrs:{name:"el-fade-in-linear"}},[n("el-dropdown",{directives:[{name:"show",rawName:"v-show",value:e.showUserItem,expression:"showUserItem"}],attrs:{trigger:"hover"},on:{command:e.handleCommand}},[n("span",{staticClass:"el-dropdown-link"},[n("img",{staticClass:"user-logo",attrs:{src:"static/avatar.jpg"}}),e._v(" "),n("span",{staticClass:"user-name"},[e._v(e._s(e.user.username))])]),e._v(" "),n("el-dropdown-menu",{slot:"dropdown"},[n("el-dropdown-item",{attrs:{command:"usercenter"}},[e._v("用户中心")])],1)],1)],1)],2)],1)])},i=[],o={render:s,staticRenderFns:i};t.a=o},DW9A:function(e,t,n){"use strict";n.d(t,"g",function(){return s}),n.d(t,"j",function(){return i}),n.d(t,"d",function(){return o}),n.d(t,"i",function(){return r}),n.d(t,"f",function(){return a}),n.d(t,"e",function(){return l}),n.d(t,"h",function(){return c}),n.d(t,"a",function(){return u}),n.d(t,"b",function(){return f}),n.d(t,"c",function(){return d});var s=[{linkProblemId:"8B9",picUrl:"static/slides/slide_1.png"},{linkProblemId:"oX4",picUrl:"static/slides/slide_2.png"},{linkProblemId:"jMK",picUrl:"static/slides/slide_3.png"},{linkProblemId:"KeK",picUrl:"static/slides/slide_4.png"},{linkProblemId:"jL9",picUrl:"static/slides/slide_5.png"}],i=["Array","Search","Tree","String","Backtracking","Math","Dynamic Programming","Hash"],o=["default","base16-dark","ambiance","paraiso-light","cobalt","paraiso-dark","rubyblue","mbo","solarized"],r=["sublime","emacs","vim"],a=["text/x-csrc","text/x-c++src","text/x-csharp","text/x-java","text/x-python","text/javascript","text/x-ruby","text/x-go"],l=["C","C++","C#","Java","Python3","JavaScript","Ruby","Go"],c=["int findMaximumXOR(int* nums, int numsSize) {\n\n}","class Solution {\npublic:\n     int findMaximumXOR(vector<int>& nums) {\n\n     }\n};","class Solution {\n    public int findMaximumXOR(int[] nums) {\n\n    }\n}",'class Solution(object):\n    def findMaximumXOR(self, nums):\n      """\n      :type nums: List[int]\n      :rtype: int\n      """',"class Solution {\n    func findMaximumXOR(_ nums: [Int]) -> Int {\n\n    }\n}","func findMaximumXOR(nums []int) int {\n\n}"],u="https://api.txdna.cn",f="ok",d="no"},"Du/2":function(e,t,n){"use strict";n.d(t,"a",function(){return s}),n.d(t,"b",function(){return i}),n.d(t,"c",function(){return o}),n.d(t,"d",function(){return r});var s="SET_PROBLEM",i="SET_USER",o="SET_COLLECTION_LIST",r="SET_TEMPLETS"},E4Ja:function(e,t){},ENpB:function(e,t,n){function s(e){return n(i(e))}function i(e){var t=o[e];if(!(t+1))throw new Error("Cannot find module '"+e+"'.");return t}var o={"./apl/apl.js":"qxza","./asciiarmor/asciiarmor.js":"fKDv","./asn.1/asn.1.js":"P89j","./asterisk/asterisk.js":"5YCJ","./brainfuck/brainfuck.js":"77wO","./clike/clike.js":"6S2o","./clojure/clojure.js":"1J1+","./cmake/cmake.js":"3l40","./cobol/cobol.js":"SHcL","./coffeescript/coffeescript.js":"yI/k","./commonlisp/commonlisp.js":"+T+e","./crystal/crystal.js":"Id8r","./css/css.js":"puAj","./cypher/cypher.js":"To3j","./d/d.js":"zdi2","./dart/dart.js":"T43g","./diff/diff.js":"HDE3","./django/django.js":"B5Q8","./dockerfile/dockerfile.js":"bNms","./dtd/dtd.js":"Vcha","./dylan/dylan.js":"V3et","./ebnf/ebnf.js":"+yUg","./ecl/ecl.js":"yP40","./eiffel/eiffel.js":"kaWT","./elm/elm.js":"gO0v","./erlang/erlang.js":"KyD5","./factor/factor.js":"ZZxW","./fcl/fcl.js":"VmZn","./forth/forth.js":"OEOO","./fortran/fortran.js":"SUHZ","./gas/gas.js":"DVrE","./gfm/gfm.js":"bWRU","./gherkin/gherkin.js":"BGqB","./go/go.js":"CQVp","./groovy/groovy.js":"lYxz","./haml/haml.js":"kDpU","./handlebars/handlebars.js":"Qei9","./haskell-literate/haskell-literate.js":"TUpE","./haskell/haskell.js":"ao9a","./haxe/haxe.js":"T0xp","./htmlembedded/htmlembedded.js":"zA3a","./htmlmixed/htmlmixed.js":"8Nur","./http/http.js":"Ssj+","./idl/idl.js":"s5ks","./javascript/javascript.js":"5IAE","./jinja2/jinja2.js":"3h7H","./jsx/jsx.js":"KR8v","./julia/julia.js":"uRaj","./livescript/livescript.js":"SEST","./lua/lua.js":"SN96","./markdown/markdown.js":"f6fj","./mathematica/mathematica.js":"BPpj","./mbox/mbox.js":"g3M4","./meta.js":"+fCR","./mirc/mirc.js":"nngO","./mllike/mllike.js":"YJVH","./modelica/modelica.js":"tbda","./mscgen/mscgen.js":"O099","./mumps/mumps.js":"MIy+","./nginx/nginx.js":"fQr+","./nsis/nsis.js":"qp6r","./ntriples/ntriples.js":"Aju4","./octave/octave.js":"JPpr","./oz/oz.js":"/8wJ","./pascal/pascal.js":"MXNw","./pegjs/pegjs.js":"MJwH","./perl/perl.js":"rQCa","./php/php.js":"c6RA","./pig/pig.js":"AnxN","./powershell/powershell.js":"n04a","./properties/properties.js":"0nxQ","./protobuf/protobuf.js":"UHRe","./pug/pug.js":"PdD+","./puppet/puppet.js":"11SB","./python/python.js":"tWbI","./q/q.js":"LE4k","./r/r.js":"9BoL","./rpm/rpm.js":"QGGy","./rst/rst.js":"A2n/","./ruby/ruby.js":"uOPQ","./rust/rust.js":"9NDn","./sas/sas.js":"uQEz","./sass/sass.js":"7BQ2","./scheme/scheme.js":"l6KL","./shell/shell.js":"PG9i","./sieve/sieve.js":"T01z","./slim/slim.js":"M/P5","./smalltalk/smalltalk.js":"IQG/","./smarty/smarty.js":"qFPF","./solr/solr.js":"Gz0W","./soy/soy.js":"d4f2","./sparql/sparql.js":"0hjm","./spreadsheet/spreadsheet.js":"rHua","./sql/sql.js":"JGZi","./stex/stex.js":"1cvq","./stylus/stylus.js":"yKVp","./swift/swift.js":"uNyq","./tcl/tcl.js":"F9rU","./textile/textile.js":"NnLm","./tiddlywiki/tiddlywiki.js":"ATIm","./tiki/tiki.js":"HVZi","./toml/toml.js":"mcQ8","./tornado/tornado.js":"pjLr","./troff/troff.js":"MrOV","./ttcn-cfg/ttcn-cfg.js":"P/dt","./ttcn/ttcn.js":"su+d","./turtle/turtle.js":"hL2b","./twig/twig.js":"RfqI","./vb/vb.js":"DZXy","./vbscript/vbscript.js":"Vyxb","./velocity/velocity.js":"CdSB","./verilog/verilog.js":"BgqI","./vhdl/vhdl.js":"K/yg","./vue/vue.js":"/9hD","./webidl/webidl.js":"JfGf","./xml/xml.js":"ezqs","./xquery/xquery.js":"zGcu","./yacas/yacas.js":"KXeR","./yaml-frontmatter/yaml-frontmatter.js":"ybz3","./yaml/yaml.js":"uqUb","./z80/z80.js":"3Y8U"};s.keys=function(){return Object.keys(o)},s.resolve=i,e.exports=s,s.id="ENpB"},EV1k:function(e,t,n){"use strict";function s(e){n("38HL")}var i=n("broi"),o=n("PbDU"),r=n("VU/8"),a=s,l=r(i.a,o.a,a,null,null);t.a=l.exports},F4ME:function(e,t,n){"use strict";function s(e){n("jMQ7")}var i=n("WTo+"),o=n("DEaM"),r=n("VU/8"),a=s,l=r(i.a,o.a,a,"data-v-6c2f2492",null);t.a=l.exports},Fncu:function(e,t){},GggT:function(e,t){},IcnI:function(e,t,n){"use strict";var s=n("7+uW"),i=n("NYxO"),o=n("mUbh"),r=n("UjVw"),a=n("lwq5"),l=n("m9kF"),c=n("sax8");n.n(c);s.default.use(i.d);t.a=new i.d.Store({actions:o,getters:r,state:a.a,mutations:l.a,strict:!1,plugins:[]})},"Ijt+":function(e,t){},K00g:function(e,t){},"Kf/3":function(e,t,n){"use strict";function s(e,t,n,s){var i=e.findIndex(n);0!==i&&(i>0&&e.splice(i,1),e.unshift(t),s&&e.length>s&&e.pop())}function i(e,t){var n=e.findIndex(t);n>-1&&e.splice(n,1)}function o(e){var t=v.a.get(b,[]);return s(t,e,function(t){return e.id===t.id},j),v.a.set(b,t),t}function r(e){var t=v.a.get(b,[]);return i(t,function(t){return t.id===e.id}),v.a.set(b,t),t}function a(){return v.a.get(b,[])}function l(e){return v.a.set(_,e),e}function c(){return v.a.get(_,{})}function u(e){return v.a.set(y,e),e}function f(){return v.a.get(y,{})}function d(){return v.a.remove(y),{}}function h(e){v.a.set(w,e)}function m(){return v.a.get(w,"")}function p(){v.a.remove(w)}t.g=o,t.h=r,t.f=a,t.i=l,t.d=c,t.j=u,t.e=f,t.k=d,t.a=h,t.b=m,t.c=p;var g=n("MfZv"),v=n.n(g),b="__favorite__",j=200,w="__token__",_="__PROBLEM_KEY__",y="__USER_KEY__"},LDKD:function(e,t){},LiRR:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-dialog",{attrs:{title:"注册用户",visible:e.dialogShow,"before-close":e.handleBeforeClose},on:{"update:visible":function(t){e.dialogShow=t}}},[n("el-form",[n("el-form-item",{attrs:{label:"账号:","label-width":e.formLabelWidth}},[n("el-input",{ref:"username",attrs:{placeholder:"请输入用户名",spellcheck:"false"},model:{value:e.username,callback:function(t){e.username="string"==typeof t?t.trim():t},expression:"username"}}),e._v(" "),n("span",{staticClass:"prompt prompt-username",class:e.showUserPrompt},[e._v("*用户名过短")])],1),e._v(" "),n("el-form-item",{attrs:{label:"密码:","label-width":e.formLabelWidth}},[n("el-input",{attrs:{type:"password",placeholder:"请输入密码"},model:{value:e.password,callback:function(t){e.password="string"==typeof t?t.trim():t},expression:"password"}}),e._v(" "),n("span",{staticClass:"prompt prompt-password",class:e.showPasswordPrompt},[e._v("*密码过短")])],1),e._v(" "),n("el-form-item",{attrs:{label:"邮箱","label-width":e.formLabelWidth}},[n("el-input",{ref:"email",staticClass:"input-item",attrs:{placeholder:"请输入邮箱",spellcheck:"false"},model:{value:e.email,callback:function(t){e.email="string"==typeof t?t.trim():t},expression:"email"}}),e._v(" "),n("span",{staticClass:"prompt prompt-email",class:e.showEmailPrompt},[e._v("*邮箱格式错误")])],1)],1),e._v(" "),n("div",{staticClass:"dialog-footer",slot:"footer"},[n("el-button",{on:{click:e.clickCancel}},[e._v("取 消")]),e._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:e.clickConfirm}},[e._v("确 定")])],1)],1)},i=[],o={render:s,staticRenderFns:i};t.a=o},M93x:function(e,t,n){"use strict";function s(e){n("aBsq")}var i=n("xJD8"),o=n("rjqw"),r=n("VU/8"),a=s,l=r(i.a,o.a,a,"data-v-54647535",null);t.a=l.exports},MPNI:function(e,t){},"Mpj/":function(e,t){},NHnr:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=n("7+uW"),i=n("M93x"),o=n("YaEn"),r=n("IcnI"),a=n("zL8q"),l=n.n(a),c=n("f90G"),u=n.n(c),f=n("OS1Z"),d=n.n(f),h=n("4/hK"),m=(n.n(h),n("8U58")),p=(n.n(m),n("q8zI")),g=(n.n(p),n("E4Ja")),v=(n.n(g),n("pw1w"));n.n(v);s.default.config.productionTip=!1,s.default.use(l.a),s.default.use(u.a),s.default.use(d.a),new s.default({el:"#app",data:function(){return{value:""}},router:o.a,store:r.a,template:"<App/>",components:{App:i.a}})},O5KI:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement;return(e._self._c||t)("textarea")},i=[],o={render:s,staticRenderFns:i};t.a=o},PbDU:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-dialog",{attrs:{title:"用户登录",visible:e.dialogShow,"before-close":e.handleBeforeClose},on:{"update:visible":function(t){e.dialogShow=t}}},[n("el-form",[n("el-form-item",{attrs:{label:"账号:","label-width":e.formLabelWidth}},[n("el-input",{ref:"username",attrs:{placeholder:"请输入账号",spellcheck:"false"},model:{value:e.username,callback:function(t){e.username="string"==typeof t?t.trim():t},expression:"username"}})],1),e._v(" "),n("el-form-item",{attrs:{label:"密码:","label-width":e.formLabelWidth}},[n("el-input",{attrs:{type:"password",placeholder:"请输入密码"},model:{value:e.password,callback:function(t){e.password="string"==typeof t?t.trim():t},expression:"password"}})],1)],1),e._v(" "),n("div",{staticClass:"dialog-footer",slot:"footer"},[n("el-button",{on:{click:e.clickCancel}},[e._v("取 消")]),e._v(" "),n("el-button",{attrs:{type:"primary"},on:{click:e.clickConfirm}},[e._v("确 定")])],1)],1)},i=[],o={render:s,staticRenderFns:i};t.a=o},Q6j7:function(e,t){},QQmU:function(e,t,n){"use strict";function s(e){n("Fncu")}var i=n("cNUl"),o=n("LiRR"),r=n("VU/8"),a=s,l=r(i.a,o.a,a,"data-v-19cf3bd2",null);t.a=l.exports},"QfH/":function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"el-form-item",class:{"is-error":"error"===e.validateState,"is-validating":"validating"===e.validateState,"is-required":e.isRequired||e.required}},[e.label||e.$slots.label?n("label",{staticClass:"el-form-item__label",style:e.labelStyle,attrs:{for:e.prop}},[e._t("label",[e._v(e._s(e.label+e.form.labelSuffix))])],2):e._e(),e._v(" "),n("div",{staticClass:"el-form-item__content",style:e.contentStyle},[e._t("default"),e._v(" "),n("transition",{attrs:{name:"el-zoom-in-top"}},["error"===e.validateState&&e.showMessage&&e.form.showMessage?n("div",{staticClass:"el-form-item__error"},[e._v(e._s(e.validateMessage))]):e._e()])],2)])},i=[],o={render:s,staticRenderFns:i};t.a=o},R3s6:function(e,t){},UM8r:function(e,t){},UjVw:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),n.d(t,"problem",function(){return s}),n.d(t,"user",function(){return i}),n.d(t,"collectionList",function(){return o}),n.d(t,"templets",function(){return r});var s=function(e){return e.problem},i=function(e){return e.user},o=function(e){return e.collectionList},r=function(e){return e.templets}},UoAS:function(e,t){},"WTo+":function(e,t,n){"use strict";var s=n("//Fk"),i=n.n(s),o=n("Dd8w"),r=n.n(o),a=n("Kf/3"),l=n("mtWM"),c=n.n(l),u=n("NYxO"),f=n("DW9A");t.a={props:{datas:{type:Array,default:["注册","用户登录","管理员登录"]}},data:function(){return{headrs:this.datas,user:{}}},methods:r()({handleSelect:function(e,t){console.log(e),"注册"===e?this.$emit("register"):"用户登录"===e?this.$emit("login"):"退出登录"===e?this.quitUser():"管理员登录"===e&&this.mangerLogin()},quitUser:function(){var e=this;this.$confirm("是否要退出登录?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){e._logoff()}).catch(function(){})},_logoff:function(){var e=this,t=f.a+"/tokens";c.a.delete(t).then(function(t){t.data.msg===f.b&&(e.headrs=["注册","用户登录","管理员登录"],e.$notify({title:"退出登录",message:"注销用户成功!",type:"success"}),console.log("成功退出"),e.$router.push("/home"),n.i(a.c)(),e.clearOneUser(),e._changeAxiosInterceptor())},function(t){e._logoff()})},_changeAxiosInterceptor:function(){console.log("_changeAxiosInterceptor"),c.a.interceptors.request.use(function(e){return e.headers.token="",e.auth={},e},function(e){return i.a.reject(e)})},handleCommand:function(e){console.log(e),"usercenter"===e&&this.$router.push("/home/usercenter")},clickLogo:function(){this.$router.push("/home")},mangerLogin:function(){this.$router.push("/home/managerlogin")}},n.i(u.a)({setUser:"SET_USER"}),n.i(u.c)({getUser:"user"}),n.i(u.b)(["clearOneUser"])),watch:{datas:function(e){this.headrs=e}},computed:{showUserItem:function(){return-1!==this.headrs.indexOf("退出登录")&&(this.user=this.getUser(),console.log(this.user),!0)}}}},X1Ds:function(e,t){},XQDJ:function(e,t){},Xdwu:function(e,t){},Y0SK:function(e,t){},Y7A8:function(e,t){},YaEn:function(e,t,n){"use strict";var s=n("7+uW"),i=n("/ocq");s.default.use(i.a);var o=function(e){n.e(0).then(n.bind(null,"LqM4")).then(function(t){e(t)})},r=function(e){n.e(2).then(n.bind(null,"McHp")).then(function(t){e(t)})},a=function(e){n.e(1).then(n.bind(null,"ESnm")).then(function(t){e(t)})},l=function(e){n.e(8).then(n.bind(null,"imfC")).then(function(t){e(t)})},c=function(e){n.e(4).then(n.bind(null,"4XJM")).then(function(t){e(t)})},u=function(e){n.e(5).then(n.bind(null,"IeUv")).then(function(t){e(t)})},f=function(e){n.e(6).then(n.bind(null,"+9k5")).then(function(t){e(t)})},d=function(e){n.e(3).then(n.bind(null,"BUZr")).then(function(t){e(t)})},h=function(e){n.e(7).then(n.bind(null,"4Ggt")).then(function(t){e(t)})};t.a=new i.a({routes:[{path:"/",redirect:"/home"},{path:"/home",component:o},{path:"/home/problem",component:r,meta:{scrollToTop:!0}},{path:"/home/usercenter",component:a},{path:"/home/managerlogin",component:l},{path:"/home/manager",redirect:"/home/manager/manageusers",component:c,children:[{path:"/home/manager/manageusers",component:f},{path:"/home/manager/manageproblems",component:d},{path:"/home/manager/managecontests",component:h}]},{path:"/home/breakthrough",component:u}]})},Zlvo:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)},i=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"myfooter"},[n("div",{staticClass:"footer-wrapper"},[n("span",{staticClass:"footer-text-up"},[e._v("Copyright © 2017 CodeNut")]),e._v(" "),n("div",{staticClass:"line-wrapper"},[n("div",{staticClass:"line"})]),e._v(" "),n("span",{staticClass:"footer-text-down"},[e._v("从小白到大神,一步一个脚印")])])])}],o={render:s,staticRenderFns:i};t.a=o},ZrWO:function(e,t){},aBsq:function(e,t){},aHkt:function(e,t,n){function s(e){return n(i(e))}function i(e){var t=o[e];if(!(t+1))throw new Error("Cannot find module '"+e+"'.");return t}var o={"./3024-day.css":"tPrY","./3024-night.css":"UoAS","./abcdef.css":"9ozf","./ambiance-mobile.css":"ZrWO","./ambiance.css":"vX90","./base16-dark.css":"jGSh","./base16-light.css":"x15G","./bespin.css":"R3s6","./blackboard.css":"kSL7","./cobalt.css":"t9xi","./colorforth.css":"Q6j7","./dracula.css":"8sUU","./duotone-dark.css":"n+LN","./duotone-light.css":"GggT","./eclipse.css":"hD67","./elegant.css":"2b9r","./erlang-dark.css":"XQDJ","./hopscotch.css":"opVC","./icecoder.css":"scuT","./isotope.css":"u3n7","./lesser-dark.css":"LDKD","./liquibyte.css":"fXer","./material.css":"epNC","./mbo.css":"1XTk","./mdn-like.css":"vsRU","./midnight.css":"zLDg","./monokai.css":"UM8r","./neat.css":"Ijt+","./neo.css":"bF3y","./night.css":"ncdg","./panda-syntax.css":"mBIq","./paraiso-dark.css":"BR0Y","./paraiso-light.css":"Y0SK","./pastel-on-dark.css":"v/ec","./railscasts.css":"zUoc","./rubyblue.css":"0tbE","./seti.css":"jykA","./solarized.css":"Xdwu","./the-matrix.css":"K00g","./tomorrow-night-bright.css":"MPNI","./tomorrow-night-eighties.css":"+bOk","./ttcn.css":"+fg7","./twilight.css":"Y7A8","./vibrant-ink.css":"w/Cc","./xq-dark.css":"qyuG","./xq-light.css":"gSgD","./yeti.css":"X1Ds","./zenburn.css":"Mpj/"};s.keys=function(){return Object.keys(o)},s.resolve=i,e.exports=s,s.id="aHkt"},bF3y:function(e,t){},broi:function(e,t,n){"use strict";var s=n("//Fk"),i=n.n(s),o=n("mtWM"),r=n.n(o),a=n("Kf/3"),l=n("DW9A");t.a={props:{dialogVisible:{type:Boolean,default:!1}},data:function(){return{username:"",password:"",formLabelWidth:"50px",dialogShow:!1}},mounted:function(){this.username="",this.password=""},methods:{clickCancel:function(){this.dialogShow=!1,this.$emit("closeLoginDialog"),this.username="",this.password=""},clickConfirm:function(){var e=this,t=l.a+"/tokens";r.a.post(t,{username:this.username,password:this.password}).then(function(t){console.log(t),n.i(a.a)(t.data.result[0].token),console.log(t.data.result[0].token),e._changeAxiosInterceptor(),e.$emit("closeLoginDialog"),e.$emit("loginSuccess",t.data.result[0].id),e.$notify({title:"成功",message:"登录成功",type:"success"})},function(t){console.log(t),e.$notify.error({title:"错误",message:"登录失败"}),e.username="",e.password=""}),console.log(this.username),console.log(this.password)},handleBeforeClose:function(e){this.$emit("closeLoginDialog"),this.username="",this.password=""},_changeAxiosInterceptor:function(){var e=this;r.a.interceptors.request.use(function(t){return t.headers.token=n.i(a.b)(),t.auth={username:e.username,password:e.password},t},function(e){return i.a.reject(e)})}},watch:{dialogVisible:function(e){this.dialogShow=e}}}},cNUl:function(e,t,n){"use strict";var s=n("95Re"),i=n("mtWM"),o=n.n(i),r=n("DW9A");t.a={components:{ElFormItem:s.a},props:{dialogVisible:{type:Boolean,default:!1}},data:function(){return{username:"",password:"",email:"",formLabelWidth:"50px",dialogShow:!1}},created:function(){this.username="",this.password="",this.email=""},methods:{clickCancel:function(){this.$emit("closeRegisterDialog"),this._clearData()},clickConfirm:function(){var e=this,t=r.a+"/users";console.log(this.school),console.log(this.occupation),o.a.post(t,{username:this.username,password:this.password,email:this.email}).then(function(t){t.data.msg===r.b?(console.log(t),e.$notify({title:"成功",message:"注册成功!",type:"success"}),e.$emit("closeRegisterDialog"),e._clearData()):t.data.msg===r.c&&e.$notify({title:"警告",message:t.data.error,type:"warning"})},function(t){console.log(t),e.$notify.error({title:"错误",message:"注册失败,请重试!"})})},handleBeforeClose:function(e){this.$emit("closeRegisterDialog"),this._clearData()},_clearData:function(){this.username="",this.password="",this.email=""}},watch:{dialogVisible:function(e){this.dialogShow=e}},computed:{showUserPrompt:function(){return this.username.length<6&&0!==this.username.length?"show-username":"hide-username"},showPasswordPrompt:function(){return this.password.length<6&&0!==this.password.length?"show-password":"hide-password"},showEmailPrompt:function(){return new RegExp("([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+").test(this.email)||0===this.email.length?"hide-email":"show-email"},showSchoolPrompt:function(){return this.school.length<2&&0!==this.school.length?"show-school":"hide-school"},showOccupationPrompt:function(){return this.occupation.length<2&&0!==this.occupation.length?"show-occupation":"hide-occupation"}}}},epNC:function(e,t){},fXer:function(e,t){},gSgD:function(e,t){},hD67:function(e,t){},irpA:function(e,t){},jCJf:function(e,t,n){"use strict";var s=n("Zrlr"),i=n.n(s),o=function e(t){var n=t.user_id,s=t.username,o=t.create_time,r=t.login_time,a=t.accept_nums,l=t.realname,c=t.submit_nums,u=t.profile,f=t.school,d=t.about_me,h=t.role,m=t.tag;i()(this,e),this.user_id=n,this.username=s,this.realname=l,this.accept_nums=a,this.submit_nums=c,this.create_time=o,this.login_time=r,this.profile=u,this.school=f,this.about_me=d,this.role=h,this.tag=m};t.a=o},jGSh:function(e,t){},jMQ7:function(e,t){},jykA:function(e,t){},kSL7:function(e,t){},lwq5:function(e,t,n){"use strict";var s=n("Kf/3"),i={problem:n.i(s.d)(),user:n.i(s.e)(),collectionList:n.i(s.f)(),templets:[]};t.a=i},m9kF:function(e,t,n){"use strict";var s,i=n("bOdI"),o=n.n(i),r=n("Du/2"),a=(s={},o()(s,r.a,function(e,t){e.problem=t}),o()(s,r.b,function(e,t){e.user=t}),o()(s,r.c,function(e,t){e.collectionList=t}),o()(s,r.d,function(e,t){e.templets=t}),s);t.a=a},mBIq:function(e,t){},mUbh:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),n.d(t,"saveFavoriteList",function(){return o}),n.d(t,"deleteFavoriteList",function(){return r}),n.d(t,"saveOneProblem",function(){return a}),n.d(t,"saveOneUser",function(){return l}),n.d(t,"clearOneUser",function(){return c});var s=n("Du/2"),i=n("Kf/3"),o=function(e,t){(0,e.commit)(s.c,n.i(i.g)(t))},r=function(e,t){(0,e.commit)(s.c,n.i(i.h)(t))},a=function(e,t){(0,e.commit)(s.a,n.i(i.i)(t))},l=function(e,t){(0,e.commit)(s.b,n.i(i.j)(t))},c=function(e){(0,e.commit)(s.b,n.i(i.k)())}},"n+LN":function(e,t){},ncdg:function(e,t){},opVC:function(e,t){},pw1w:function(e,t){},q8zI:function(e,t){},qyuG:function(e,t){},rjqw:function(e,t,n){"use strict";var s=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("el-row",[n("el-col",{attrs:{span:0,sm:24,lg:24,md:24,xs:24}},[n("m-header",{attrs:{datas:e.headers},on:{login:e._login,register:e._register}})],1)],1),e._v(" "),n("login",{directives:[{name:"show",rawName:"v-show",value:e.showLoginDialog,expression:"showLoginDialog"}],ref:"login",attrs:{dialogVisible:e.showLoginDialog},on:{closeLoginDialog:e._closeLoginDialog,loginSuccess:e.loginSuccess}}),e._v(" "),n("register",{attrs:{dialogVisible:e.showRegisterDialog},on:{closeRegisterDialog:e._closeRegisterDialog}}),e._v(" "),n("router-view"),e._v(" "),n("m-footer")],1)},i=[],o={render:s,staticRenderFns:i};t.a=o},scuT:function(e,t){},t3QM:function(e,t,n){"use strict";function s(e){n("irpA")}var i=n("zva/"),o=n.n(i),r=n("Zlvo"),a=n("VU/8"),l=s,c=a(o.a,r.a,l,null,null);t.a=c.exports},t9xi:function(e,t){},tPrY:function(e,t){},u3n7:function(e,t){},"v/ec":function(e,t){},vX90:function(e,t){},vsRU:function(e,t){},"w/Cc":function(e,t){},woo5:function(e,t,n){"use strict";function s(){}function i(e,t){var n=e;t=t.replace(/\[(\w+)\]/g,".$1"),t=t.replace(/^\./,"");for(var s=t.split("."),i=0,o=s.length;i<o-1;++i){var r=s[i];if(!(r in n))throw new Error("please transfer a valid prop path to form item!");n=n[r]}return{o:n,k:s[i],v:n[s[i]]}}var o=n("CDcn"),r=n.n(o),a=n("ufP2");t.a={name:"ElFormItem",componentName:"ElFormItem",mixins:[a.a],props:{label:String,labelWidth:String,prop:String,required:Boolean,rules:[Object,Array],error:String,validateStatus:String,showMessage:{type:Boolean,default:!0}},watch:{error:function(e){this.validateMessage=e,this.validateState=e?"error":""},validateStatus:function(e){this.validateState=e}},computed:{labelStyle:function(){var e={};if("top"===this.form.labelPosition)return e;var t=this.labelWidth||this.form.labelWidth;return t&&(e.width=t),e},contentStyle:function(){var e={},t=this.label;if("top"===this.form.labelPosition||this.form.inline)return e;if(!t&&!this.labelWidth&&this.isNested)return e;var n=this.labelWidth||this.form.labelWidth;return n&&(e.marginLeft=n),e},form:function(){for(var e=this.$parent,t=e.$options.componentName;"ElForm"!==t;)"ElFormItem"===t&&(this.isNested=!0),e=e.$parent,t=e.$options.componentName;return e},fieldValue:{cache:!1,get:function(){var e=this.form.model;if(e&&this.prop){var t=this.prop;return-1!==t.indexOf(":")&&(t=t.replace(/:/,".")),i(e,t).v}}},isRequired:function(){var e=this.getRules(),t=!1;return e&&e.length&&e.every(function(e){return!e.required||(t=!0,!1)}),t}},data:function(){return{validateState:"",validateMessage:"",validateDisabled:!1,validator:{},isNested:!1}},methods:{validate:function(e){var t=this,n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:s,i=this.getFilteredRule(e);if(!i||0===i.length)return n(),!0;this.validateState="validating";var o={};o[this.prop]=i;var a=new r.a(o),l={};l[this.prop]=this.fieldValue,a.validate(l,{firstFields:!0},function(e,s){t.validateState=e?"error":"success",t.validateMessage=e?e[0].message:"",n(t.validateMessage)})},resetField:function(){this.validateState="",this.validateMessage="";var e=this.form.model,t=this.fieldValue,n=this.prop;-1!==n.indexOf(":")&&(n=n.replace(/:/,"."));var s=i(e,n);Array.isArray(t)?(this.validateDisabled=!0,s.o[s.k]=[].concat(this.initialValue)):(this.validateDisabled=!0,s.o[s.k]=this.initialValue)},getRules:function(){var e=this.form.rules,t=this.rules;return e=e?e[this.prop]:[],[].concat(t||e||[])},getFilteredRule:function(e){return this.getRules().filter(function(t){return!t.trigger||-1!==t.trigger.indexOf(e)})},onFieldBlur:function(){this.validate("blur")},onFieldChange:function(){if(this.validateDisabled)return void(this.validateDisabled=!1);this.validate("change")}},mounted:function(){if(this.prop){this.dispatch("ElForm","el.form.addField",[this]);var e=this.fieldValue;Array.isArray(e)&&(e=[].concat(e)),Object.defineProperty(this,"initialValue",{value:e});this.getRules().length&&(this.$on("el.form.blur",this.onFieldBlur),this.$on("el.form.change",this.onFieldChange))}},beforeDestroy:function(){this.dispatch("ElForm","el.form.removeField",[this])}}},x15G:function(e,t){},xJD8:function(e,t,n){"use strict";var s=n("Dd8w"),i=n.n(s),o=n("F4ME"),r=n("EV1k"),a=n("mtWM"),l=n.n(a),c=n("NYxO"),u=n("QQmU"),f=n("t3QM"),d=n("jCJf"),h=n("DW9A");t.a={data:function(){return{showLoginDialog:!1,showRegisterDialog:!1,headers:["注册","用户登录","管理员登录"]}},methods:i()({_login:function(){this.showLoginDialog=!0},_register:function(){this.showRegisterDialog=!0},_closeRegisterDialog:function(){this.showRegisterDialog=!1},_closeLoginDialog:function(){this.showLoginDialog=!1},loginSuccess:function(e){var t=this;console.log(e);var n=h.a+"/users/"+e;l.a.get(n).then(function(e){if(e.data.msg===h.b){t.headers=["退出登录"];var n=e.data.result[0];t.saveOneUser(new d.a(n))}},function(e){console.log(e),t.loginSuccess()})}},n.i(c.a)({setUser:"SET_USER"}),n.i(c.b)(["saveOneUser"])),components:{MHeader:o.a,Login:r.a,Register:u.a,MFooter:f.a}}},zLDg:function(e,t){},zUoc:function(e,t){},"zva/":function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.d15b8b63bff2b6d202fc.js.map