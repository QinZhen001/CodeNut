/**
 * Created by qinzhen on 2017/9/30.
 */
export default class ReturnResult {
  constructor ({mytitle, memory_used, output, status, time_used}) {
    this.mytitle = mytitle
    this.memory_used = memory_used
    this.output = output
    this.status = status
    this.time_used = time_used
  }
}
