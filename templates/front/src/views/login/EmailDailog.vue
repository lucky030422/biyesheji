<script setup>
import { reactive, ref } from 'vue'
import YyEmail from '@/components/FormItem/components/YyEmail.vue'
import { commonTableAPI } from '@/api/common'
const emailVisible = defineModel()
const emits = defineEmits(['loginSucessEvent'])
let { emailType, tableName } = defineProps(['emailType', 'tableName'])
const emailFormRef = ref()
const ruleForm = reactive({
  email: '',
  mobile: '',
  code: '',
})
const rules = reactive({
  email: [
    {
      required: true,
      message: '请输入邮箱',
      trigger: 'change',
    },
  ],
  mobile: [
    {
      required: true,
      message: '请输入手机',
      trigger: 'change',
    },
  ],
  code: [
    {
      required: true,
      message: '请输入验证码',
      trigger: 'change',
    },
  ],
})
const emailColumn = {
  columnName: emailType == '邮箱登录' ? 'email' : 'mobile',
  comments: emailType == '邮箱登录' ? '邮箱' : '手机',
}

const isLoading = ref(false)
function closeEmailDialog() {
  emailVisible.value = false
}
// 发送api
const sendCodeAPI = (tableName, text) => {
  return emailType == '邮箱登录'
    ? commonTableAPI({
        url: tableName + '/sendemail/login',
        method: 'get',
        params: {
          email: text,
        },
      })
    : commonTableAPI({
        url: tableName + '/sendsms/login',
        method: 'get',
        params: {
          mobile: text,
        },
      })
}
// 登录逻辑
async function emailLogin() {
  // 表单校检逻辑
  let valid = await emailFormRef.value.validate((valid, fields) => {
    if (!valid) {
      // 验证不通过，提示第一个错误
      let firstErrorField = Object.entries(fields)
      let firstErrorMessage = firstErrorField[0][1][0].message || '表单校验失败，请检查输入'
      ElMessage.error(firstErrorMessage)
    }
  })
  if (!valid) return

  isLoading.value = true

  try {
    let apiConfig =
      emailType == '邮箱登录'
        ? {
            url: tableName + '/email/login',
            method: 'post',
            params: {
              email: ruleForm.email,
              emailcode: ruleForm.code,
            },
          }
        : {
            url: tableName + '/sms/login',
            method: 'post',
            params: {
              mobile: ruleForm.mobile,
              smscode: ruleForm.code,
            },
          }
    let res = await commonTableAPI(apiConfig)
    emits('loginSucessEvent', res.token, tableName)
  } catch (error) {
    ElMessage.error(error.msg || error.message || '发送失败')
  }

  isLoading.value = false
}
</script>
<template>
  <el-dialog
    class="yy-dialog email-login-dialog"
    v-model="emailVisible"
    width="460px"
    destroy-on-close
    :close-on-click-modal="false"
    append-to-body
  >
    <template #header>
      <div class="email-dialog-head">
        <button class="email-back" type="button" @click="closeEmailDialog">返回账号登录</button>
        <p>使用邮箱验证码快速进入宠物寄养预约平台。</p>
      </div>
    </template>
    <el-form
      class="emailform"
      :rules="rules"
      :model="ruleForm"
      ref="emailFormRef"
      @submit.prevent="emailLogin"
    >
      <div class="email-field-label">{{ emailColumn.comments }}</div>
      <el-form-item :prop="emailColumn.columnName" class="email">
        <YyEmail
          :tableName="tableName"
          :column="emailColumn"
          :ruleForm="ruleForm"
          :customAPI="sendCodeAPI"
        />
      </el-form-item>

      <div class="email-field-label">验证码</div>
      <el-form-item prop="code" class="code">
        <el-input v-model="ruleForm.code" placeholder="请输入验证码" clearable></el-input>
      </el-form-item>
      <el-button class="email-submit" :loading="isLoading" native-type="submit" type="primary">登录</el-button>
      <div class="email-dialog-meta">
        <span>安全验证</span>
        <span>无需记住密码</span>
      </div>
    </el-form>
  </el-dialog>
</template>
<style lang="scss">
.email-login-dialog {
  .el-dialog {
    width: min(460px, calc(100vw - 28px)) !important;
    border-radius: 18px;
    overflow: hidden;
    background: #fbfefc;
    box-shadow: 0 24px 70px rgba(29, 66, 51, 0.22);
  }

  .el-dialog__header {
    position: relative;
    margin-right: 0;
    padding: 26px 30px 16px;
    border-bottom: 1px solid #e5f0ea;
  }

  .el-dialog__headerbtn {
    top: 18px;
    right: 18px;
    width: 34px;
    height: 34px;
    border-radius: 50%;

    &:hover {
      background: #edf7f1;
    }
  }

  .el-dialog__body {
    padding: 22px 30px 30px;
  }

  .email-dialog-head {
    position: relative;
    min-height: 72px;
    padding: 44px 34px 0 0;

    .email-back {
      position: absolute;
      top: 0;
      left: 0;
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      margin: 0;
      padding: 0 12px;
      border: 1px solid #dcebe3;
      border-radius: 999px;
      color: #1f6f52;
      background: #e8f6ef;
      font-size: 14px;
      font-weight: 700;
      line-height: 1;
      white-space: nowrap;
      cursor: pointer;

      &:hover,
      &:focus {
        border-color: rgba(47, 143, 103, 0.35);
        background: #dff2e8;
      }
    }

    p {
      margin: 0;
      color: #66736c;
      font-size: 14px;
      line-height: 1.7;
    }
  }

  .emailform {
    max-width: none;
    margin: 0;
  }

  .email-field-label {
    margin: 0 0 8px;
    color: #35453c;
    font-size: 14px;
    font-weight: 700;
  }

  .el-form-item {
    margin-bottom: 18px;
  }

  .el-input {
    --el-input-focus-border-color: #2f8f67;
  }

  .el-input__wrapper {
    min-height: 46px;
    border-radius: 10px;
    background: #f5faf7;
    box-shadow: 0 0 0 1px #dcebe3 inset;
  }

  .el-input__wrapper.is-focus {
    background: #fff;
    box-shadow: 0 0 0 1px #2f8f67 inset, 0 8px 18px rgba(47, 143, 103, 0.12);
  }

  .el-input-group__append {
    overflow: hidden;
    border: 0;
    border-radius: 0 10px 10px 0;
    background: #e8f6ef;
    box-shadow: 0 0 0 1px #dcebe3 inset;

    .el-button {
      min-height: 46px;
      color: #1f6f52;
      font-weight: 700;

      &:hover {
        color: #1f6f52;
        background: #dff2e8;
      }
    }
  }

  .code {
    .el-form-item__content {
      flex-wrap: nowrap;
      gap: 10px;
    }
  }

  .email-submit {
    width: 100%;
    min-height: 46px;
    border: 0;
    border-radius: 10px;
    color: #fff;
    background: linear-gradient(135deg, #2f8f67, #1f6f52);
    font-size: 15px;
    font-weight: 700;
    box-shadow: 0 12px 24px rgba(47, 143, 103, 0.22);

    &:hover,
    &:focus {
      color: #fff;
      background: linear-gradient(135deg, #379f75, #1f6f52);
    }
  }

  .email-dialog-meta {
    display: flex;
    justify-content: center;
    gap: 18px;
    margin-top: 16px;
    color: #6d7b73;
    font-size: 13px;

    span {
      position: relative;

      & + span::before {
        content: "";
        position: absolute;
        left: -10px;
        top: 50%;
        width: 3px;
        height: 3px;
        border-radius: 50%;
        background: #a8c7b8;
        transform: translateY(-50%);
      }
    }
  }
}
</style>
