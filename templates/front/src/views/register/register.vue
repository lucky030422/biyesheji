<script setup>
/**
 * @description 注册页面
 */
import '@/style/register.scss'
import { reactive, ref, provide, onMounted, nextTick } from 'vue'
import { useRouter, useRoute } from 'vue-router'

import FormItems from './FormItems.vue'
import LoginButton from './LoginButton.vue'
import RegisterButton from './RegisterButton.vue'
import Custom from './Custom.vue'
import getFilePath from '@/utils/getFilePath'

// 注册表单组件
import '@/components/FormItem/index.js'
import { getInitRuleForm, getInitRules, getColums, getDisable } from '@/utils/form'
import { roleList } from '@/utils/role'
import tableConfigs from '@/utils/tableConfigs'
import { registerAPI } from '@/api/login'

const router = useRouter()
const route = useRoute()
let tableName = route.query.tableName
const defaultRegisterBackground = getFilePath('upload/chongwufuwu_宠物猫上门洗护喂养套餐1.jpg')

// 表单实例
const ruleFormRef = ref()
// 列字段
let columns = reactive(getColums(tableName, 'register'))
// 表单数据
let ruleForm = reactive(getInitRuleForm(tableName))
// 表单验证规则
let rules = reactive(getInitRules(columns))
// 禁止操作字段
let disabledColumnNames = getDisable(tableName, columns, 'register')

function clearRegisterCredentials() {
  const accountName = roleList.find(role => role.tableName === tableName)?.accountName
  const names = [accountName, 'username', 'zhanghao', 'password', 'mima', 'repeatPassword']

  names.forEach(name => {
    if (name && Object.prototype.hasOwnProperty.call(ruleForm, name)) {
      ruleForm[name] = ''
    }
  })
}

// ----------------------------------
// ---------- 邮箱/手机注册 ----------
// ----------------------------------
let { emailRegister } = tableConfigs[tableName].table
if (emailRegister == '是' || emailRegister == '短信') {
  let emailColumn = {
    columnName: emailRegister == '是' ? 'email' : 'mobile',
    comments: emailRegister == '是' ? '邮箱' : '手机号',
    form_type: 'YyEmail',
  }
  let codeColumn = {
    columnName: 'code',
    comments: '验证码',
    form_type: 'YyText',
  }
  columns.push(emailColumn, codeColumn)
  emailRegister == '是' ? (ruleForm.email = '') : (ruleForm.mobile = '')
  ruleForm.code = ''
}

// 注册事件
async function registerEvent() {

  // 表单校检逻辑
  let valid = await ruleFormRef.value.validate((valid, fields) => {
    if (!valid) {
      // 验证不通过，提示第一个错误
      let firstErrorField = Object.entries(fields)
      let firstErrorMessage = firstErrorField[0][1][0].message || '表单校验失败，请检查输入'
      ElMessage.error(firstErrorMessage)
    }
  })
  if (!valid) return

  // 确认密码
  let password = ruleForm.password || ruleForm.mima
  let passwordColumn = columns.find(
    column => column.columnName == 'password' || column.columnName == 'mima'
  )
  if (ruleForm.repeatPassword != password) {
    ElMessage.error(passwordColumn.comments + ' 与 确认' + passwordColumn.comments + ' 不一致')
    return
  }

  try {
    // 请求后端
    let params = {}
    let data = {
      ...ruleForm
    }
    delete data.repeatPassword

    // 邮箱验证码
    if (emailRegister == '是') {
      params.emailcode = data.code
      delete data.code
    }


    await registerAPI(tableName, data, params)

    ElMessage.success('注册成功')

    // 跳转首页
    setTimeout(() => {
      let accountName = roleList.find(role => role.tableName === tableName).accountName
      router.push({
        path: '/login',
        query: {
          tableName: tableName,
          username: data[accountName],
        },
      })
    }, 1000)
  } catch (error) {
    ElMessage.error('注册失败：')
    ElMessage.error(error.message || error.msg || '')
  }
}

// ----------------------------------
// ------------ 注入-----------------
// ----------------------------------
function loginEvent() {
  router.push('/login')
}

onMounted(() => {
  clearRegisterCredentials()
  nextTick(() => {
    setTimeout(clearRegisterCredentials, 120)
  })
})

provide('register', {
  tableName,
  ruleForm,
  columns,
  disabledColumnNames,
  loginEvent,
})
</script>

<template>
  <div
    class="register"
    :style="{
      '--register-bg': `url(${$projectImages.fRegisterBackgroudImg || defaultRegisterBackground})`,
    }"
  >
    <section class="register-hero">
      <span class="register-kicker">用户注册 · 宠物寄养预约平台</span>
      <h1>欢迎加入宠物寄养预约平台</h1>
      <div class="register-hero-grid">
        <div class="register-hero-item">
          <strong>预约寄养</strong>
          <span>快速提交宠物入住需求</span>
        </div>
        <div class="register-hero-item">
          <strong>宠物服务</strong>
          <span>洗护、喂养、照看一站完成</span>
        </div>
        <div class="register-hero-item">
          <strong>用品商城</strong>
          <span>精选宠物用品安心购买</span>
        </div>
      </div>
    </section>
    <el-form
      class="registerform"        
      :model="ruleForm"
      :rules="rules"
      autocomplete="off"
      ref="ruleFormRef"
      @submit.prevent="registerEvent"
    >
      
<div class="registerform-wrapper">
  <div class="register-card-head">
    <h2>创建你的宠物服务账号</h2>
    <p>填写基础信息后，即可继续预约服务、购买用品和查看订单。</p>
  </div>
  <FormItems />
  <div class="btn-wrapper">
    <RegisterButton />
    <LoginButton />
  </div>
  <Custom />
</div>
  
    </el-form>
  </div>
</template>
