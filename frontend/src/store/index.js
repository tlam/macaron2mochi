import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedTrip: null
  },
  mutations: {
    reset(state) {
      state.selectedTrip = null;
    },
    setSelectedTrip(state, payload) {
      state.selectedTrip = payload.trip;
    }
  }
});
