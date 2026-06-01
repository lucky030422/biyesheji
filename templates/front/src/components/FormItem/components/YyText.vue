<script setup>
/**
 * @description 普通文本框
 */
import { computed } from 'vue'

defineOptions({
  inheritAttrs: false,
})
const { column, ruleForm, disabled } = defineProps({
  column: {
    type: Object,
    required: true,
  },
  ruleForm: {
    type: Object,
    required: true,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const accountColumnNames = ['username', 'zhanghao', 'account', 'userName']
const inputAutocomplete = computed(() =>
  accountColumnNames.includes(column.columnName) ? 'off' : undefined
)
</script>

<template>
  <el-input
    v-model="ruleForm[column.columnName]"
    :placeholder="`请输入${column.comments}`"
    :disabled="disabled"
    :autocomplete="inputAutocomplete"
    clearable
  />
</template>
