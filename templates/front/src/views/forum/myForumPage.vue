<script setup>
import '@/style/exam.scss'
import '@/style/list.scss'
import '@/components/TableItem/index'
/**
 * @description 我的发布
 */
import { provide, ref, shallowRef } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import CenterTitle from '@/views/center/CenterTitle.vue'
import BreadCrumb from '../list/BreadCrumb.vue'
import ListEdit from '../list/ListEdit.vue'

import tableConfigs from '@/utils/tableConfigs'
import { deleteAPI, getPageAPI } from '@/api/list'

const route = useRoute()
const router = useRouter()

const tableName = 'forum'
let { table, columns } = tableConfigs.forum

// 列字段配置
let hideColumNames = ['userid', 'username', 'parentid', 'avatarurl', 'content', 'crazilynum', 'delflag', 'isanon']
columns = columns.filter(column => !hideColumNames.includes(column.columnName))

// 禁止操作字段
let disabledColumnNames = ['delflag', 'istop']
// ----------------------------------
// ---------- 面包屑 ----------------
// ----------------------------------
const homePath = ref('/index/home')
const second = ref({
  path: null,
  title: null,
})
const lastTitle = ref('我的发布')
function backEvent() {
  router.back()
}
// 确保 BreadCrumb能复用 后台的
provide('header', {
  homePath,
  second,
  lastTitle,
  backEvent,
})

// ----------------------------------
// ---------- 弹框 ---------------
// ----------------------------------
const dialogVisible = ref(false)
const dialogTitle = ref('弹框标题')
const dialogComponent = shallowRef(null)
const dialogClass = ref('')
let dialogData = {}
function openDialog(data) {
  dialogTitle.value = data.dialogTitle
  dialogComponent.value = data.dialogComponent
  dialogData = data.dialogData
  dialogClass.value = data.dialogClass

  dialogVisible.value = true
}

// ----------------------------------
// ---------- 表格 ----------------
// ----------------------------------
const isLoading = ref(false)
const list = ref([])
fetchData()
async function fetchData() {
  isLoading.value = true

  try {
    let params = {
      page: 1,
      limit: 1000,
      parentid: 0,
      sort: 'istop,toptime',
      order: 'desc,desc',
    }
    let res = await getPageAPI(tableName, params)
    list.value = res.data.list || []
  } catch (error) {}

  isLoading.value = false
}

function edit(row) {
  dialogTitle.value = '编辑'
  dialogClass.value = ''
  dialogComponent.value = ListEdit
  dialogData = {
    type: 'update',
    id: row.id,
    tableName,
    row,
  }
  dialogVisible.value = true
}

// 删除
function removes(row) {
  ElMessageBox.confirm('确认删除?', '提示', {
    confirmButtonText: '删除',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(async () => {
      let ids = [row.id]
      await deleteAPI(tableName, ids)

      fetchData()
      ElMessage.success('删除成功')
    })
    .catch(() => {})
}
</script>
<template>
  <div class="exam-page">
    <BreadCrumb />
    <!-- 标题 -->
    <div class="examheader-wrapper">
      <CenterTitle title="我的发布" />
    </div>

    <div class="examtable-wrapper" v-loading="isLoading">
      <el-table :data="list">
        <el-table-column
          v-for="(column, index) in columns"
          :prop="column.columnName"
          :label="column.comments"
          :key="column.columnName"
        >
          <template #default="scope">
            <component
              :is="column.table_type"
              :row="scope.row"
              :column="column"
              :disabled="disabledColumnNames.includes(column.columnName)"
              :tableName="tableName"
              :value="scope.row[column.columnName]"
            />
          </template>
        </el-table-column>

        <el-table-column label="操作" width="140">
          <template #default="{ row }">
            <div class="table-button-wrapper">
              <el-button @click="edit(row)" size="small">编辑</el-button>
              <el-button @click="removes(row)" size="small" type="danger">删除</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 弹框公用 -->
    <el-dialog
      class="yy-dialog"
      v-model="dialogVisible"
      :title="dialogTitle"
      destroy-on-close
      :close-on-click-modal="false"
    >
      <component
        v-model="dialogVisible"
        :is="dialogComponent"
        :tableName="tableName"
        :data="dialogData"
        :class="dialogClass"
        @fetchData="fetchData"
      />
    </el-dialog>
  </div>
</template>
