/**
 * Created by qinzhen on 2017/9/5.
 */
import * as types from './mutation-types'
import { saveFavorite, deleteFavorite } from 'common/js/cache'

export const saveFavoriteList = function ({commit}, problem) {
  commit(types.SET_COLLECTION_LIST, saveFavorite(problem))
}

export const deleteFavoriteList = function ({commit}, problem) {
  commit(types.SET_COLLECTION_LIST, deleteFavorite(problem))
}
