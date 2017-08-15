import * as types from './mutation-types'

const matutaions = {
  [types.SET_SINGER](state, singer) {
    state.singer = singer
  },
  [types.SET_PROBLEM](state, problem) {
    state.problem = problem
  }
}

export default matutaions
