import * as types from './mutation-types'

const mutations = {
  [types.SET_PROBLEM](state, problem) {
    state.problem = problem
  },
  [types.SET_USER](state, user) {
    state.user = user
  },
  [types.SET_COLLECTION_LIST](state, list) {
    state.collectionList = list
  },
  [types.SET_TEMPLETS](state, templets){
    state.templets = templets
  },
  [types.SET_BREAKTHROUGH](state, breakthrough){
    state.breakthrough = breakthrough
  }
}

export default mutations
