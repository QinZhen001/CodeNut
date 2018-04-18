<template>
  <div class="charts">
    <div id="contests-chart"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import echarts from 'echarts'

  export default{
    mounted(){
      // Generate data
      let category = []
      let contestantData = []
      let successData = []
      let failData = []
      for (let i = 17; i >= 0; i--) {
        let date = new Date(new Date() - i * 3600 * 24 * 1000)
        category.push([
          date.getFullYear(),
          date.getMonth() + 1,
          date.getDate()
        ].join('-'))
        let b = Math.floor(Math.random() * 30)
        let d = Math.floor(Math.random() * 30)
        successData.push(b)
        contestantData.push(b + d)
        failData.push(d)
      }
// option
      let option = {
        title: {
          text: '比赛情况',
          padding: 15,
          fontSize: 22,
          textStyle: {
            color: '#E5E9F2'
          }
        },
        backgroundColor: '#0f375f',
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['line', 'bar'],
          textStyle: {
            color: '#ccc'
          }
        },
        xAxis: {
          data: category,
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        yAxis: {
          splitLine: {show: false},
          axisLine: {
            lineStyle: {
              color: '#ccc'
            }
          }
        },
        series: [{
          name: '参赛选手',
          type: 'line',
          smooth: true,
          showAllSymbol: true,
          symbol: 'emptyCircle',
          symbolSize: 15,
          data: contestantData
        }, {
          name: '通过选手',
          type: 'bar',
          barWidth: 10,
          itemStyle: {
            normal: {
              barBorderRadius: 5,
              color: new echarts.graphic.LinearGradient(
                0, 0, 0, 1,
                [
                  {offset: 0, color: '#14c8d4'},
                  {offset: 1, color: '#43eec6'}
                ]
              )
            }
          },
          data: successData
        }, {
          name: '失败选手',
          type: 'bar',
          barGap: '-100%',
          barWidth: 10,
          itemStyle: {
            normal: {
              color: new echarts.graphic.LinearGradient(
                0, 0, 0, 1,
                [
                  {offset: 0, color: 'rgba(20,200,212,0.5)'},
                  {offset: 0.2, color: 'rgba(20,200,212,0.2)'},
                  {offset: 1, color: 'rgba(20,200,212,0)'}
                ]
              )
            }
          },
          z: -12,
          data: failData
        }, {
          name: 'dotted',
          type: 'pictorialBar',
          symbol: 'rect',
          itemStyle: {
            normal: {
              color: '#0f375f'
            }
          },
          symbolRepeat: true,
          symbolSize: [12, 4],
          symbolMargin: 1,
          z: -10
        }]
      }
      let usersChart = echarts.init(document.getElementById('contests-chart'))
      usersChart.setOption(option)
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .charts
    width 100%
    height 500px
    #contests-chart
      width 100%
      height 500px
</style>
