/**
 * Created by qinzhen on 2017/9/5.
 */
import { loadFavorite } from 'common/js/cache'

const state = {
  problem: {},
  user: {},
  collectionList: loadFavorite()
}

export default state
