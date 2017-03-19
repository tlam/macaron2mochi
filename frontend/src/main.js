// The following line loads the standalone build of Vue instead of the runtime-only build,
// so you don't have to do: import Vue from 'vue/dist/vue'
// This is done with the browser options. For the config, see package.json
import axios from 'axios'
import store from './store'
import Vue from 'vue'
import App from './App.vue'

Vue.prototype.$http = axios;

new Vue({ // eslint-disable-line no-new
  el: '#app',
  store,
  render: (h) => h(App)
})
