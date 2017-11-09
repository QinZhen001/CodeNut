<template>
  <transition name="el-fade-in-linear">
    <div class="selfstudy">
      <el-row :gutter="20">
        <el-col :sm="0" :lg="3" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
        <el-col :sm="24" :lg="14" :md="17" :xs="24">
          <h2 align="left">算法大全</h2>
          <div class="container">
            <el-tabs type="border-card">
              <el-tab-pane label="全部">
                <self-study-list :selfStudyItems="selfStudyAllItems"></self-study-list>
              </el-tab-pane>
              <el-tab-pane label="初级难度">
                <self-study-list :selfStudyItems="selfStudySimpleItems"></self-study-list>
              </el-tab-pane>
              <el-tab-pane label="中级难度">
                <self-study-list :selfStudyItems="selfStudyMediumItems"></self-study-list>
              </el-tab-pane>
              <el-tab-pane label="高级难度">
                <self-study-list :selfStudyItems="selfStudyHardItems"></self-study-list>
              </el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
        <el-col :sm="24" :lg="4" :md="5" :xs="24">
          <div class="sidebar-header">
            <span class="sidebar-title">经典算法</span>
          </div>
          <div class="list">
            <ul>
              <li><a href="javascript:;">使用位运算交换两个数</a></li>
              <li><a href="javascript:;">Eratosthenes 筛选求质数问题的程序源</a></li>
              <li><a href="javascript:;">C语言数组灵活多变的访问形式</a></li>
              <li><a href="javascript:;">求格雷码的完整程序源代码</a></li>
              <li><a href="javascript:;">使用位运算交换两个数</a></li>
            </ul>
          </div>
          <div class="sidebar-header">
            <span class="sidebar-title">典型程序</span>
          </div>
          <div class="list">
            <ul>
              <li><a href="javascript:;">计算一个字节里有多少位（bit）被置1</a></li>
              <li><a href="javascript:;">C语言奶牛生子的问题（腾讯面试题）</a></li>
              <li><a href="javascript:;">动物的生活习性</a></li>
              <li><a href="javascript:;">picard迭代法的实现代码</a></li>
              <li><a href="javascript:;">辛结构与Hamilton算法介绍</a></li>
            </ul>
          </div>
          <div class="sidebar-header">
            <span class="sidebar-title">最新问题</span>
          </div>
          <div class="list">
            <ul>
              <li><a href="javascript:;">背包算法的完整程序源码</a></li>
              <li><a href="javascript:;">实现插入排序算法的的完整程序源代码</a></li>
              <li><a href="javascript:;">Huber稳健估计</a></li>
              <li><a href="javascript:;">混合同余法均匀分布随机数发生器</a></li>
              <li><a href="javascript:;">QR分解计算最小二乘问题</a></li>
              <li><a href="javascript:;">共轭梯度法的完整程序源代码</a></li>
              <li><a href="javascript:;">三角方程组的完整程序源码</a></li>
              <li><a href="javascript:;">选主元消去法的完整程序源码</a></li>
              <li><a href="javascript:;">Crout分解的完整程序源代码</a></li>
              <li><a href="javascript:;">追赶法计算三对角方程</a></li>
              <li><a href="javascript:;">对称正定矩阵的cholesky分解</a></li>
            </ul>
          </div>
        </el-col>
        <el-col :sm="0" :lg="3" :md="1" :xs="0">
          <div class="grid-content">
          </div>
        </el-col>
      </el-row>
    </div>
  </transition>
</template>

<script type="text/ecmascript-6">
  import SelfStudyList from 'components/selfstudy/selfstudylist'
  import { selfStudyItems } from 'common/js/data'

  export default{
    data(){
      return {
        selfStudyAllItems: [],
        selfStudySimpleItems: [],
        selfStudyMediumItems: [],
        selfStudyHardItems: []
      }
    },
    mounted(){
      this.selfStudyAllItems = selfStudyItems.slice(0, 10)
      this.selfStudySimpleItems = selfStudyItems.filter((item, index) => {
        return index % 3 === 0
      })
      this.selfStudyMediumItems = selfStudyItems.filter((item, index) => {
        return index % 4 === 0
      })
      this.selfStudyHardItems = selfStudyItems.filter((item, index) => {
        return index % 5 === 0
      })
    },
    methods: {},
    components: {
      SelfStudyList
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .selfstudy
    flex: 1 0 auto;
    .grid-content
      border-radius: 4px;
      min-height: 36px;
    .container
      margin-top: 20px;
    .sidebar-header
      padding-top 65px
      height: 40px;
      border-bottom: 1px solid whitesmoke;
      .sidebar-title
        display: inline-block;
        border-bottom: 3px solid #0195dd;
        height: 38px;
        line-height: 38px;
        font-size: 18px;
        box-sizing: content-box;
        color: #0195dd;
    .list
      ul
        li
          margin-left -15px
          height: 30px;
          line-height: 30px;
          width: 250px;
          overflow: hidden;
          font-size: 16px;
          a
            color: #555;
            text-decoration none
            &:hover
              text-decoration underline


</style>
