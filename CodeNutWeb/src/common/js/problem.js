/**
 * Created by qinzhen on 2017/9/17.
 */
export default class Problem {
  constructor ({id, title, tag, level, description, accepted, submitted, like_nums, hate_nums}) {
    this.id = id
    this.title = title
    this.tag = tag
    this.level = level
    this.description = description
    this.accepted = accepted
    this.submitted = submitted
    this.like_nums = like_nums
    this.hate_nums = hate_nums
  }
}
