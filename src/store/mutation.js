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
  }
}

export default mutations
