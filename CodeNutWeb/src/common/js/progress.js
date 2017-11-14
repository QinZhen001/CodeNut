/**
 * Created by qinzhen on 2017/9/16.
 */
import { Doughnut } from 'vue-chartjs'

export default Doughnut.extend({
  mounted() {
    this.renderChart({
      datasets: [{
        data: [5, 10, 20, 30],
        backgroundColor: ['#13CE66', '#FF3D67', '#059BFF', '#FFC233']
      }],
      // These labels appear in the legend and in the tooltips when hovering different arcs
      labels: [
        'Accepted',
        'Wrong Answer',
        'Runtime Error',
        'Attempted'
      ]
    }, {
      responsive: true,
      maintainAspectRatio: false
    })
  }
})
