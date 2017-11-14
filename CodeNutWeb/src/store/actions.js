/**
 * Created by qinzhen on 2017/9/5.
 */
import * as types from './mutation-types'
import { saveFavorite, deleteFavorite, saveProblem, saveUser, clearUser } from 'common/js/cache'

export const saveFavoriteList = function ({commit}, problem) {
  commit(types.SET_COLLECTION_LIST, saveFavorite(problem))
}

export const deleteFavoriteList = function ({commit}, problem) {
  commit(types.SET_COLLECTION_LIST, deleteFavorite(problem))
}

export const saveOneProblem = function ({commit}, problem) {
  commit(types.SET_PROBLEM, saveProblem(problem))
}

export const saveOneUser = function ({commit}, user) {
  commit(types.SET_USER, saveUser(user))
}

export const clearOneUser = function ({commit}) {
  commit(types.SET_USER, clearUser())
}
