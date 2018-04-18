/**
 * Created by qinzhen on 2017/9/23.
 */
export default class User {
  constructor ({
                 user_id, username, create_time, login_time, accept_nums,
                 realname, submit_nums, profile, school, about_me, role, tag
               }) {
    this.user_id = user_id
    this.username = username
    this.realname = realname
    this.accept_nums = accept_nums
    this.submit_nums = submit_nums
    this.create_time = create_time
    this.login_time = login_time
    this.profile = profile
    this.school = school
    this.about_me = about_me
    // user（默认）编程 &评论&写文章
    // moderator	编程&评论&写文章&管理用户评论
    // sponsor	编程 &评论&写文章&举办比赛
    // administrator全部
    this.role = role
    this.tag = tag
  }
}
