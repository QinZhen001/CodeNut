export default class Path {
  constructor (ctx, x, y, targetX, targetY) {
    this.ctx = ctx
    this.x = x
    this.y = y
    this.targetX = targetX
    this.targetY = targetY
  }

  draw () {
    let ctx = this.ctx
    ctx.save()
    ctx.lineWidth = 7
    ctx.lineCap = 'round'
    ctx.strokeStyle = '#CFCFCF'
    ctx.lineCap = 'round'
    ctx.beginPath()
    ctx.moveTo(this.x + 90, this.y + 20)
    ctx.lineTo(this.targetX, this.targetY + 60)
    ctx.setLineDash([15, 20])
    ctx.stroke()
    ctx.restore()
  }
}
