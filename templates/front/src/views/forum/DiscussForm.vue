
<script setup>
import { inject, ref, reactive } from 'vue'
const columns = [
  {
    columnName: 'content',
    comments: '评论',
    form_type: 'YyQuill',
  },
]

const rules = reactive({
  content: [
    {
      required: true,
      message: '请输入评论',
    },
  ],
})
// 表单实例
const ruleFormRef = ref()
let { formOkEvent, ruleForm } = inject('detail')
</script>
<template>
  <div class="discuss-form-forum">
    <el-form class="forumform" :model="ruleForm" :rules="rules" ref="ruleFormRef" @submit.prevent>
      <el-form-item v-for="column in columns" :key="column.columnName" :prop="column.columnName">
        <component :is="column.form_type" :columns="columns" :column="column" :ruleForm="ruleForm" />
      </el-form-item>

      <div class="btn-wrapper">
        <el-button type="primary" class="submit-btn" @click="formOkEvent(ruleForm.content)">提交</el-button>
        <el-button class="cancel-btn" @click="ruleForm.content = ''">重置</el-button>
      </div>
    </el-form>
  </div>
</template>
<style>
.discuss-form-forum{
  padding: 20px 0;
}
</style>
  