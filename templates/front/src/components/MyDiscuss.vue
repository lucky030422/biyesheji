<script setup>
import { ref } from 'vue'
import { commonTableAPI } from '@/api/common'
import { deleteAPI, getDetailAPI, getListAPI, updateAPI } from '@/api/list'
import router from '@/router'

/**
 * @description 我的评论
 */

const list = ref([])
fetchData()
async function fetchData() {
  let res = await commonTableAPI({
    url: 'comment/list',
    method: 'get',
  })
  list.value = res.data
}

// 查看
function view(row) {
  let { tablename, refid } = row

  let path = '/index/' + tablename + 'Detail'


  // 跳转到详情页面
  router.push({ path, query: { id: refid } })
}

// 删除
function remove(row) {
  ElMessageBox.confirm('确认删除评论?', '提示', {
    confirmButtonText: '删除',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(async () => {
      try {
        let messageInstance = ElMessage.info({
          message: '删除中',
          duration: 0,
        })
  
        let { tablename, refid, id } = row
        let discussTableName = 'discuss' + tablename
        // 删除评论表的数据
        await deleteAPI(discussTableName, [id])
        updateDetail(tablename, refid, discussTableName)
        await fetchData()
        messageInstance.close()
        ElMessage.success('删除成功')
      } catch (error) {
        messageInstance.close()
        ElMessage.error('删除失败')
      }
    })
    .catch(() => {})
}

// 更新详情数据
async function updateDetail(tableName, id, discussTableName) {
  let { data } = await getDetailAPI(tableName, id)
  let res = await getListAPI(discussTableName, {
    refid: id,
    page: 1,
    limit: 99999,
  })

  let len = res.data.list.length || 0
  // 评论数
  data.discussnum = len


  await updateAPI(tableName, data)
}
</script>

<template>
  <el-table :data="list">
    <el-table-column prop="content" label="评论内容">
      <template #default="{ row }">
        <div class="ql-snow ql-editor" v-html="row.content"></div>
      </template>
    </el-table-column>

    <el-table-column prop="reply" label="回复内容">
      <template #default="{ row }">
        <div class="ql-snow ql-editor" v-html="row.reply"></div>
      </template>
    </el-table-column>



    <el-table-column label="操作">
      <template #default="{ row }">
        <div class="table-button-wrapper">
          <el-button @click="view(row)" size="small">查看</el-button>
          <el-button @click="remove(row)" size="small" type="danger">删除</el-button>
        </div>
      </template>
    </el-table-column>
  </el-table>
</template>
