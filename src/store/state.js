/**
 * Created by qinzhen on 2017/9/5.
 */
import { loadFavorite, loadProblem } from 'common/js/cache'

const state = {
  problem: loadProblem(),
  user: {},
  headerData: ['注册', '用户登录', '管理员登录'],
  collectionList: loadFavorite(),
  templets: [],
  breakthrough: false
}

export default state
