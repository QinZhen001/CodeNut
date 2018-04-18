<template>
  <div class="breakthrough">
    <canvas id="canvas" class="canvas"></canvas>
  </div>
</template>

<script type="text/ecmascript-6">
  export default{
    mounted() {
      let canvas = document.getElementById('canvas'),
        ctx = canvas.getContext('2d'),
        width = window.innerWidth,
        height = window.innerHeight
      canvas.width = width
      canvas.height = height
      ctx.save()
      ctx.lineWidth = 7
      ctx.lineCap = 'round'
      ctx.strokeStyle = '#fff'
      ctx.beginPath()
      ctx.moveTo(144, 760)
      ctx.quadraticCurveTo(120, 522, 120, 522)
      ctx.setLineDash([5, 12])
      ctx.stroke()
      ctx.restore()
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .breakthrough
    position fixed
    left 0
    top 0
    bottom 0
    right 0
    width 100%
    height 100%
    z-index 10
    babackground: rgba(7, 17, 27, 0.95);
    .canvas
      z-index: -1;
      position: fixed
</style>
