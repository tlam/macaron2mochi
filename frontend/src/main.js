// The following line loads the standalone build of Vue instead of the runtime-only build,
// so you don't have to do: import Vue from 'vue/dist/vue'
// This is done with the browser options. For the config, see package.json
import axios from 'axios'
import store from './store'
import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import TripMap from './components/TripMap.vue'
import Overview from './components/Overview.vue'

Vue.prototype.$http = axios;
Vue.use(VueRouter);

const routes = [
  {path: '/overview', component: Overview},
  {path: '/map', component: TripMap}
];

const router = new VueRouter({
  routes
});

new Vue({ // eslint-disable-line no-new
  el: '#app',
  store,
  router,
  render: (h) => h(App)
})
