import { Radar } from 'vue-chartjs'
import { RandomNumBoth } from 'common/js/util'

export default Radar.extend({
  data(){
    return {
      res1: 0,
      res2: 0,
      res3: 0,
      res4: 0,
      res5: 0
    }
  },
  mounted() {
    this.res1 = RandomNumBoth(0, 100)
    this.res2 = RandomNumBoth(0, 100)
    this.res3 = RandomNumBoth(0, 100)
    this.res4 = RandomNumBoth(0, 100)
    this.res5 = RandomNumBoth(0, 100)
    this.renderChart({
      labels: ['活跃度', '经验值', '多样性', '技能值', '规范性'],
      datasets: [
        {
          label: '码力值',
          backgroundColor: 'rgba(88,183,255,0.5)',
          borderColor: '#20A0FF',
          pointBackgroundColor: '#1D8CE0',
          // pointHoverBackgroundColor: 'rgba(1,1,1,1)',
          // pointHoverBorderColor: 'rgba(220,220,220,1)',
          data: [this.res1, this.res2, this.res3, this.res4, this.res5]
        }
      ]
    }, {
      pointLabelFontColor: '#111',
      responsive: true,
      maintainAspectRatio: false,
      scaleShowLine: true,
      angleShowLineOut: true,
      scaleShowLabels: false,
      scaleBeginAtZero: true,
      angleLineWidth: 1,
      pointLabelFontSize: 22,
      pointDot: true,
      pointDotRadius: 5,
      pointDotStrokeWidth: 1,
      pointHitDetectionRadius: 20,
      legendTemplate: '<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<datasets.length; i++){%><li><span style="background-color:<%=datasets[i].strokeColor%>"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>'
    })
  }
})
