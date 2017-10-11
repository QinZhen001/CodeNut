<template>
  <div class="manage-users-table">
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item><i class="el-icon-menu"></i> 用户管理</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-table :data="userDatas" border style="width: 100%" ref="multipleTable"
              @selection-change="handleSelectionChange">
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column prop="username" label="用户名" sortable width="150">
      </el-table-column>
      <el-table-column prop="realname" label="真实姓名" width="150">
      </el-table-column>
      <el-table-column prop="school" label="所在学校" width="150">
      </el-table-column>
      <el-table-column prop="create_time" label="注册时间" width="250">
      </el-table-column>
      <el-table-column prop="login_time" label="登陆时间" width="250">
      </el-table-column>
      <el-table-column prop="submit_nums" label="编程提交数" width="120">
      </el-table-column>
      <el-table-column prop="accept_nums" label="编程通过数" width="120">
      </el-table-column>
      <el-table-column prop="role" label="用户等级" width="148">
      </el-table-column>
      <el-table-column label="操作" width="180">
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
    <div class="pagination">
      <el-pagination
        @current-change="handleCurrentChange"
        layout="prev, pager, next"
        :total="100">
      </el-pagination>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
  import { baseUrl, MSG_OK } from 'common/js/data'
  import axios from 'axios'

  export default {
    data() {
      return {
        userDatas: [],
        cur_page: 1,
        multipleSelection: [],
        select_cate: '',
        select_word: '',
        del_list: [],
        is_search: false
      }
    },
    created(){
      this.getData(this.cur_page)
    },
    computed: {
      data(){
        const self = this
        return self.userDatas.filter(function (d) {
          let is_del = false
          for (let i = 0; i < self.del_list.length; i++) {
            if (d.name === self.del_list[i].name) {
              is_del = true
              break
            }
          }
          if (!is_del) {
            if (d.address.indexOf(self.select_cate) > -1 &&
              (d.name.indexOf(self.select_word) > -1 ||
              d.address.indexOf(self.select_word) > -1)
            ) {
              return d
            }
          }
        })
      }
    },
    methods: {
      handleCurrentChange(val){
        this.cur_page = val
        this.getData(this.cur_page)
      },
      getData(curPage){
        let url = `${baseUrl}/users?page=${curPage}`
        axios.get(url).then(response => {
          if (response.data.msg === MSG_OK) {
            this.userDatas = response.data.result
          }
        }, response => {})
      },
      formatter(row, column) {
        return row.address
      },
      filterTag(value, row) {
        return row.tag === value
      },
      handleEdit(index, row) {
        this.$message('编辑第' + (index + 1) + '行')
      },
      handleDelete(index, row) {
        console.log(row.user_id)
        let url = `${baseUrl}/users/${row.user_id}`
        axios.delete(url).then(response => {
          if (response.data.msg === 'ok') {
            this.getData(this.cur_page)
            this.$message({
              message: `成功删除用户:${row.username}`,
              type: 'success'
            })
          }
        }, response => {
          this.$message.error(`无法删除用户${row.username}`)
        })
      },
      delAll(){
        const self = this,
          length = self.multipleSelection.length
        let str = ''
        self.del_list = self.del_list.concat(self.multipleSelection)
        for (let i = 0; i < length; i++) {
          str += self.multipleSelection[i].name + ' '
        }
        self.$message.error('删除了' + str)
        self.multipleSelection = []
      },
      handleSelectionChange(val) {
        this.multipleSelection = val
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .manage-users-table
    max-width 100%
    .crumbs
      margin-bottom: 20px;
    .pagination
      margin: 20px 0;
      text-align: right;

  .handle-box
    margin-bottom: 20px;

  .handle-select
    width: 120px;

  .handle-input
    width: 300px;
    display: inline-block;

</style>
