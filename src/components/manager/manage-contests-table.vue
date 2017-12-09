<template>
  <el-table :data="contestDatas" border style="width: 100%" ref="multipleTable" @expand="expandCol">
    <el-table-column type="expand">
      <template scope="props">
        <ul class="user-list">
          <li>
            <span>参赛选手:</span>
          </li>
          <li v-for="(item,index) in contestants" :key="index">
            {{item.user}}
          </li>
        </ul>
      </template>
    </el-table-column>
    <el-table-column prop="id" label="ID" width="150">
    </el-table-column>
    <el-table-column prop="title" label="标题" sortable width="150">
    </el-table-column>
    <el-table-column prop="description" label="描述" width="330" show-overflow-tooltip>
    </el-table-column>
    <el-table-column prop="start_time" label="开始时间" width="250">
    </el-table-column>
    <el-table-column prop="end_time" label="结束时间" width="250">
    </el-table-column>
    <el-table-column prop="sponsor" label="举办者" width="120">
    </el-table-column>
    <el-table-column prop="user_nums" label="参加人数" width="120">
    </el-table-column>
    <el-table-column label="操作" width="150" fixed="right">
      <template scope="scope">
        <el-button size="small"
                   @click="handleEdit(scope.$index, scope.row)">编辑
        </el-button>
        <el-button size="small" type="danger"
                   @click="handleDelete(scope.$index, scope.row)">删除
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script type="text/ecmascript-6">
  import { baseUrl, MSG_OK } from 'common/js/data'
  import axios from 'axios'

  export default{
    props: {
      contestDatas: {
        type: Array
      }
    },
    data(){
      return {
        contestantsL: ''
      }
    },
    methods: {
      expandCol(row, expanded){
        console.log(row)
        console.log(expanded)
        if (expanded) {
          let url = `${baseUrl}/contests/${row.id}/users`
          axios.get(url).then(response => {
            if (response.data.msg === MSG_OK) {
              this.contestants = response.data.result || '暂无'
              console.log(this.contestants)
            }
          }, response => {})
        }
      },
      handleEdit(index, row){
        this.$emit('handleEdit', row)
      },
      handleDelete(index, row){
        this.$emit('handleDelete', row)
      }
    }
  }
</script>

<style lang="stylus" scoped rel="stylesheet/stylus">
  .user-list
    li
      float: left
      list-style: none; /* 将默认的列表符号去掉 */
      padding: 0; /* 将默认的内边距去掉 */
      margin-left: 6px;
      font-size 16px
      span
        font-weight 400
        font-size 16px
        color #1D8CE0
</style>
