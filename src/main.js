// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import VueCodeMirror from 'vue-codemirror'

import 'codemirror/lib/codemirror.css'    // css，必要
import 'codemirror/lib/codemirror.js'

import 'element-ui/lib/theme-default/index.css'
import 'common/stylus/base.styl'

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(VueCodeMirror)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: {App}
})
