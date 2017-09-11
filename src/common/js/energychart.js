import { Radar } from 'vue-chartjs'

export default Radar.extend({
  mounted() {
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
          data: [65, 59, 90, 81, 56]
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
