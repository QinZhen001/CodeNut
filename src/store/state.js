/**
 * Created by qinzhen on 2017/9/5.
 */
import { loadFavorite, loadProblem } from 'common/js/cache'

const state = {
  problem: loadProblem(),
  user: {},
  collectionList: loadFavorite(),
  templets: [],
  breakthrough: false
}

export default state
