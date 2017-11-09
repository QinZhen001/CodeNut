<template>
  <div class="charts">
    <div id="users-chart"></div>
  </div>
</template>

<script type="text/ecmascript-6">
  import echarts from 'echarts'

  export default{
    data(){
      return {
        option: {
          title: {
            text: '在线人数',
            lineHeight: 40,
            left: 30,
            padding: [
              0,  // 上
              10, // 右
              0,  // 下
              30 // 左
            ],
            textStyle: {
              color: '#324057',
              fontSize: 22
            }
          },
          tooltip: {
            position: 'top'
          },
          visualMap: {
            min: 0,
            max: 1000,
            calculable: true,
            orient: 'horizontal',
            left: 'center',
            top: 'top'
          },

          calendar: [
            {
              range: '2017',
              cellSize: ['auto', 20]
            }
          ],
          series: [{
            type: 'heatmap',
            coordinateSystem: 'calendar',
            calendarIndex: 0,
            data: this.getVirtulData(2017)
          }]
        }
      }
    },
    mounted(){
//      let chartBox = document.getElementsByClassName('charts')[0]
//      let myChart = document.getElementById('users-chart')
//      // 用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
//      function resizeCharts () {
//        myChart.style.width = chartBox.style.width + 'px'
//        myChart.style.height = chartBox.style.height + 'px'
//      }
//      // 设置容器高宽
//      resizeCharts()
      let usersChart = echarts.init(document.getElementById('users-chart'))
      usersChart.setOption(this.option)
    },
    methods: {
      getVirtulData(year){
        year = year || '2017'
        let date = +echarts.number.parseDate(year + '-01-01')
        let end = +echarts.number.parseDate((+year + 1) + '-01-01')
        let dayTime = 3600 * 24 * 1000
        let data = []
        for (let time = date; time < end; time += dayTime) {
          data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            Math.floor(Math.random() * 1000)
          ])
        }
        return data
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .charts
    width 100%
    height 300px
    #users-chart
      width 100%
      height 300px
</style>
