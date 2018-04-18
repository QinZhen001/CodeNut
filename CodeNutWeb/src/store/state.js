/**
 * Created by qinzhen on 2017/9/5.
 */
import { loadFavorite, loadProblem, loadUser } from 'common/js/cache'

const state = {
  problem: loadProblem(),
  user: loadUser(),
  collectionList: loadFavorite(),
  templets: []
}

export default state
