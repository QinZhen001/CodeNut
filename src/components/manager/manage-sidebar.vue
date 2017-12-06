<template>
  <div class="sidebar">
    <el-menu class="el-menu-vertical-demo"
             theme="dark" router @select="handleSelect">
      <el-menu-item :index="item.index" v-for="(item,idx) in items" :key="idx">
        <template slot="title">
          <i :class="item.icon"></i>{{ item.title }}
        </template>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data() {
      return {
        items: [
          {
            icon: 'el-icon-setting',
            index: 'manageusers',
            title: '用户管理'
          },
          {
            icon: 'el-icon-document',
            index: 'manageproblems',
            title: '题目管理'
          },
          {
            icon: 'el-icon-date',
            index: 'managecontests',
            title: '比赛管理'
          }
        ]
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        this.$router.push(`/home/manager/${key}`)
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .sidebar
    display: block;
    position: absolute;
    width: 250px;
    left: 0;
    top: 70px;
    bottom: 0;
    background: #2E363F;
    ul
      height: 100%;

</style>
