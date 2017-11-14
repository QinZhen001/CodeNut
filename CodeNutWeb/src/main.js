// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import VueCodeMirror from 'vue-codemirror'
import mavonEditor from 'mavon-editor'

import 'codemirror/lib/codemirror.css'
import 'codemirror/lib/codemirror.js'

import 'element-ui/lib/theme-default/index.css'
import 'common/stylus/base.styl'

import 'mavon-editor/dist/css/index.css'

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(VueCodeMirror)
Vue.use(mavonEditor)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  data() {
    return {value: ''}
  },
  router,
  store,
  template: '<App/>',
  components: {App}
})
