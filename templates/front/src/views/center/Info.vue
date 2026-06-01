<script setup>
/**
 * @description 个人信息
 *
 * infoList 数据列表
 * item.label 名称
 * item.value 值
 *
 * userAvatar 头像
 */
import { computed, inject, ref } from 'vue'
import { updateAPI } from '@/api/list'
import { useUserInfo } from '@/store'
import { getAvatar } from '@/utils'
import { clearFilePath } from '@/utils/getFilePath'
import UpdatePassword from './updatePassword.vue'
import MyDiscuss from '@/components/MyDiscuss.vue'

let { infoList, userAvatar, tableName, columns, avatarColumn, infoEvent } = inject('center')

const userInfoStore = useUserInfo()
const editingColumnName = ref('')
const editingForm = ref({})
const isSaving = ref(false)
const showAvatarDialog = ref(false)
const avatarEditMode = ref(false)
const avatarForm = ref({})
const showPasswordDialog = ref(false)
const showDiscussDialog = ref(false)
const avatarPreviewList = computed(() => userAvatar.value ? [userAvatar.value] : [])
const actionItems = [
  {
    label: '修改密码',
    value: '定期更新密码，保护账号安全',
    action: 'password',
  },
  {
    label: '我的评论',
    value: '查看、跳转或删除已发布评论',
    action: 'discuss',
  },
]

function getUserForm() {
  return JSON.parse(localStorage.getItem('userForm') || '{}')
}

function syncUserInfo(form) {
  let [avatar, username] = getAvatar(form, tableName)
  userInfoStore.setUserInfo({
    avatar,
    username,
    isLogin: true,
  })
  localStorage.setItem('userForm', JSON.stringify(form))
  localStorage.setItem('useravatar', clearFilePath(avatar))
  localStorage.setItem('username', username)
  infoEvent()
}

function startEdit(item) {
  editingColumnName.value = item.columnName
  editingForm.value = { ...getUserForm() }
}

function cancelEdit() {
  editingColumnName.value = ''
  editingForm.value = {}
}

async function saveEdit() {
  isSaving.value = true
  try {
    await updateAPI(tableName, editingForm.value)
    syncUserInfo(editingForm.value)
    cancelEdit()
    ElMessage.success('修改成功')
  } catch (error) {
    ElMessage.error(`修改失败：${error.msg || error.message || ''}`)
  }
  isSaving.value = false
}

function openAvatarDialog() {
  avatarForm.value = { ...getUserForm() }
  avatarEditMode.value = false
  showAvatarDialog.value = true
}

function handleAction(item) {
  if (item.action === 'password') {
    showPasswordDialog.value = true
  }
  if (item.action === 'discuss') {
    showDiscussDialog.value = true
  }
}

async function saveAvatar() {
  if (!avatarColumn.value) {
    return
  }

  isSaving.value = true
  try {
    await updateAPI(tableName, avatarForm.value)
    syncUserInfo(avatarForm.value)
    avatarEditMode.value = false
    showAvatarDialog.value = false
    ElMessage.success('头像修改成功')
  } catch (error) {
    ElMessage.error(`头像修改失败：${error.msg || error.message || ''}`)
  }
  isSaving.value = false
}
</script>

<template>

  <div class="centerinfo">
    <div class="biaoti2">
      <div class="title">个人信息<i></i></div>
    </div>

    <div class="centerinfo-inner">
      <!-- 头像 -->
      <button class="avatar" type="button" @click="openAvatarDialog">
        <img class="img" :src="userAvatar" draggable="false" />
        <span>查看 / 修改头像</span>
      </button>

      <!-- 其它信息 -->
      <div class="info-list">
        <div
          v-for="(item, index) in infoList"
          :key="index"
          class="info-item"
          :class="{ active: editingColumnName === item.columnName }"
        >
          <div class="info-read-row">
            <span class="label">{{ item.label }}:</span>
            <span class="value">{{ item.value }}</span>
            <button class="edit-text" type="button" @click.stop="startEdit(item)">修改</button>
          </div>

          <div class="inline-edit" v-if="editingColumnName === item.columnName">
            <component
              :is="item.column.form_type"
              :columns="columns"
              :column="item.column"
              :ruleForm="editingForm"
              :tableName="tableName"
            />
            <div class="inline-actions">
              <el-button :loading="isSaving" type="primary" @click.stop="saveEdit">保存</el-button>
              <el-button @click.stop="cancelEdit">取消</el-button>
            </div>
          </div>
        </div>

        <div
          v-for="item in actionItems"
          :key="item.action"
          class="info-item action-info-item"
        >
          <div class="info-read-row">
            <span class="label">{{ item.label }}:</span>
            <span class="value">{{ item.value }}</span>
            <button class="edit-text" type="button" @click.stop="handleAction(item)">打开</button>
          </div>
        </div>
      </div>
    </div>

    <el-dialog
      v-model="showAvatarDialog"
      title="头像"
      width="520px"
      append-to-body
      class="center-avatar-dialog"
    >
      <div class="avatar-dialog-body">
        <el-image
          class="avatar-large"
          :src="userAvatar"
          fit="cover"
          :preview-src-list="avatarPreviewList"
          preview-teleported
        />

        <div class="avatar-edit-box" v-if="avatarEditMode && avatarColumn">
          <component
            :is="avatarColumn.form_type"
            :columns="columns"
            :column="avatarColumn"
            :ruleForm="avatarForm"
            :tableName="tableName"
          />
        </div>
      </div>
      <template #footer>
        <el-button v-if="!avatarEditMode && avatarColumn" @click="avatarEditMode = true">
          修改头像
        </el-button>
        <el-button v-if="avatarEditMode" :loading="isSaving" type="primary" @click="saveAvatar">
          保存头像
        </el-button>
        <el-button @click="showAvatarDialog = false">关闭</el-button>
      </template>
    </el-dialog>

    <el-dialog
      v-model="showPasswordDialog"
      title="修改密码"
      width="620px"
      append-to-body
      class="center-action-dialog"
    >
      <UpdatePassword />
    </el-dialog>

    <el-dialog
      v-model="showDiscussDialog"
      title="我的评论"
      width="900px"
      append-to-body
      class="center-action-dialog center-discuss-dialog"
    >
      <MyDiscuss />
    </el-dialog>
  </div>
</template>

<style>
.centerinfo{
  width:100%;
  margin:0 0 18px;
  padding: 22px;
  border: 1px solid #e3eadf;
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(54, 77, 59, .08);
}
.centerinfo-inner {
  padding: 16px 0 0;
  border-radius: 8px;

  .avatar {
    width: fit-content;
    margin: 0 auto 18px;
    padding: 0;
    border: 0;
    background: transparent;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    color: #2f6f4e;
    font-size: 13px;
    font-weight: 800;
    cursor: zoom-in;

    .img {
      width: 86px;
      height: 86px;
      border: 4px solid #fff;
      border-radius: 50%;
      object-fit: cover;
      box-shadow: 0 12px 24px rgba(47, 111, 78, .16);
    }
  }

  .info-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    text-align:left;

    .info-item {
      width: 100%;
      display:flex;
      align-items: flex-start;
      justify-content: flex-start;
      gap: 12px;
      padding: 14px;
      border: 1px solid #e5ece2;
      border-radius: 8px;
      background: #fbfdf9;
      transition: border-color .2s ease, box-shadow .2s ease, transform .2s ease;
      flex-direction: column;

      .info-read-row {
        width: 100%;
        display: flex;
        align-items: flex-start;
        gap: 12px;
      }

      .label {
        flex: none;
        color: #81907e;
        font-size: 14px;
      }

      .value {
        flex: auto;
        min-width: 0;
        color: #283b2f;
        font-weight: 700;
        text-align: left;
        overflow-wrap: anywhere;
      }

      &:hover,
      &.active {
        border-color: #2f6f4e;
        box-shadow: 0 10px 22px rgba(47, 111, 78, .12);
        transform: translateY(-1px);
      }
    }

    .edit-text {
      flex: none;
      padding: 0;
      border: 0;
      background: transparent;
      color: #2f6f4e;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
    }

    .inline-edit {
      width: 100%;
      padding-top: 12px;
      border-top: 1px solid #e5ece2;
    }

    .inline-actions {
      display: flex;
      gap: 10px;
      margin-top: 12px;
    }

    .info-item:last-child {
      border-bottom: 1px solid #e5ece2;
    }
  }
}

.center-avatar-dialog {
  .avatar-dialog-body {
    display: grid;
    gap: 18px;
    justify-items: center;
  }

  .avatar-large {
    width: 220px;
    height: 220px;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 14px 34px rgba(47, 111, 78, .16);
  }

  .avatar-edit-box {
    width: 100%;
  }
}

.center-action-dialog {
  .center-wrapper,
  .updatepassword-wrapper {
    width: 100%;
  }
}

.center-discuss-dialog {
  .el-dialog__body {
    max-height: 66vh;
    overflow: auto;
  }
}

@media (max-width: 760px) {
  .centerinfo-inner .info-list {
    grid-template-columns: 1fr;
  }
}
</style>
