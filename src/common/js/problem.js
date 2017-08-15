/**
 * Created by qinzhen on 2017/8/11.
 */
export default class Problem {
  constructor({id, description, title, tag, level}) {
    this.id = id
    this.description = description
    this.level = level
    this.title = title
    this.tag = tag
  }
}
