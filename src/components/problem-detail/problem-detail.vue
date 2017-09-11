<template>
  <transition name="el-fade-in-linear">
    <div class="problem">
      <el-row v-loading="loading"
              element-loading-text="拼命加载中...">
        <el-col :sm="0" :lg="2" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
        <el-col :sm="24" :lg="20" :md="22" :xs="24">
          <h3 align="left">{{problemDetail.title}}
          </h3>
          <div class="container">
            <el-tabs v-model="tab" type="card" @tab-click="handleClick">
              <el-tab-pane label="Description" name="description">
                <description :data="problemDetail"></description>
              </el-tab-pane>
              <el-tab-pane label="Solution" name="solution">
                <solution :data="problemDetail"></solution>
              </el-tab-pane>
              <el-tab-pane label="角色管理" name="third">
                角色管理
              </el-tab-pane>
              <el-tab-pane label="定时任务补偿" name="fourth">
                定时任务补偿
              </el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
        <el-col :sm="0" :lg="2" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
      </el-row>
      <myfooter></myfooter>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import { mapGetters } from 'vuex'
  import axios from 'axios'
  import Description from 'components/description/description'
  import Solution from 'components/solution/solution'
  import Myfooter from 'components/myfooter/myfooter'

  export default {
    data() {
      return {
        loading: true,
        problemDetail: {},
        tab: 'description'
      }
    },
    created() {
      this._getProblemDetail()
    },
    computed: {
      ...mapGetters([
        'problem'
      ])
    },
    methods: {
      _getProblemDetail() {
        if (!this.problem.id) {
          this.$router.push('/home')
          return
        }
        console.log('problem detail id')
        console.log(this.problem.id)
        let url = 'https://api.txdna.cn/problems/' + `${this.problem.id}`
        axios.get(url).then(response => {
          console.log(response.data)
          this.problemDetail = response.data
          this.loading = false
        }, response => {
          console.log(response)
          this.$message.error('无法获取数据')
          setTimeout(() => { this.$router.back() }, 2000)
        })
      },
      handleClick(tab, event) {
        console.log(tab, event)
      }
    },
    components: {
      Description,
      Solution,
      Myfooter
    }
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .problem
    min-height 100%


  h3
    display: inline-block;
    margin-bottom: 10px;
    margin-right: .5em;
    font-family: inherit;
    font-weight: 500;
    line-height: 1.1;
    font-size: 24px;
    color: inherit;

  .container
    margin-top: 32px;



  .grid-content
    border-radius: 4px
    min-height: 36px

  .bg-purple
    background: #d3dce6

</style>
