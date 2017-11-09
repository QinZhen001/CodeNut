<template>
  <transition name="el-fade-in">
    <div>
      <div class="solution" v-if="solution" v-html="solution">
      </div>
      <div class="nodata" v-show="!solution || solution === {}">
        No solution at the moment
      </div>
    </div>
  </transition>
</template>


<script type="text/ecmascript-6">
  import axios from 'axios'
  import { baseUrl, MSG_OK } from 'common/js/data'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        solution: {}
      }
    },
    mounted() {
      this._getSolution()
    },
    methods: {
      _getSolution() {
        console.log(this.id + '1111111111')
        let url = `${baseUrl}/problems/${this.problem.id}/solutions`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            console.log(response.data.result[0])
            this.solution = response.data.result[0].solution
          }
        }, response => {
        })
      }
    },
    computed: {
      ...mapGetters([
        'problem'
      ])
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .solution
    background #F2F2F2;
    line-height: 1.7;
    .toc
      display: table;
      border: 1px solid #aaa;
      background-color: #f9f9f9;
      padding: 7px 25px 3px 7px;
      margin-top: 50px;
      font-size: 95%;
      ul
        margin-top: 0;
        margin-bottom: 10px;
      a
        href '#'
        color: #08c;
        text-decoration: none;

  h2
    font-size: 1.75em;
    font-weight: 700;
    margin-top: 1.275em;
    margin-bottom: .85em;
    line-height: 1.7;

  h4
    font-size: 1.25em;
    font-weight: 700;
    margin-top: 1.275em;
    margin-bottom: .85em;
    line-height: 1.7;

  hr
    height: 4px;
    padding: 0;
    margin: 1.7em 0;
    overflow: hidden;
    background-color: #e7e7e7;
    border: none;

  p
    margin: 0 0 10px;
    display: block;
    -webkit-margin-before: 1em;
    -webkit-margin-after: 1em;
    -webkit-margin-start: 0px;
    -webkit-margin-end: 0px;
    font-size 16px
    font-weight: 400;

  code
    padding: 2px 4px;
    font-size: 90%;
    color: #c7254e;
    background-color: #f9f2f4;
    border-radius: 4px;

  b, strong
    font-weight: 700;

  pre
    display: block;
    padding: 9.5px;
    margin: 0 0 10px;
    overflow: auto;
    font-size: 14px;
    line-height: 1.9;
    color: #333;
    word-break: break-all;
    word-wrap: break-word;
    background-color: #f2f2f2;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
    .nf
      color: #900;
      font-weight: bold;
    .na
      color: teal;
    .kt
      color: #458;
      font-weight: bold;
    .o
      font-weight: bold;

  .nodata
    height 100%
    width 100%
    padding: 8rem 4rem;
    text-align: center;
    font-size: 1.5rem;
    color: #dadada;
</style>
