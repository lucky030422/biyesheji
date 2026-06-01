<script setup>
import '@/style/chat.scss'

import { computed, onBeforeUnmount, ref } from 'vue'
import { BubbleList, Sender } from '@/components/chat/chatCom'

import avatart_ai from '@/assets/img/AI.png'
import { addAPI, getListAPI, saveAPI, getPageAPI } from '@/api/list'
import getFilePath, { getFirstFilePath } from '@/utils/getFilePath'
import base from '@/utils/base'
import { closeWebSocket, initWebSocket, websocketSend } from '@/utils/webSocket'
import dayjs from 'dayjs'

const baseUrl = base.get().url
const action = baseUrl + 'file/upload'
const headers = {
  Token: localStorage.getItem('Token'),
}

let { data } = defineProps(['data'])
let userid = data?.userid || Number(localStorage.getItem('userid'))
let adminid = 1
let uimage = localStorage.getItem('useravatar')
let avatar = getFirstFilePath(uimage)
let uname = localStorage.getItem('username')

const tableName = 'chat'
const config_role = {
  shape: 'corner',
  variant: 'outlined', // filled, outlined
  isMarkdown: true,
  avatarSize: '36px',
}

const list = ref([])
const hasMessage = computed(() => list.value.length > 0)
const quickQuestions = [
  '如何预约上门服务？',
  '订单状态怎么查看？',
  '可以修改预约时间吗？',
]
fetchData()
async function fetchData() {
  let res = await getListAPI(tableName, {
    userid,
    sort: 'addtime,id',
    order: 'desc,desc',
    limit: 100,
  })
  res.data.list.reverse()
  let lastTime
   let lastIndex = res.data.list.length - 1
  let newList = res.data.list.map((item, index) => {
    let { id, ask, reply, uname, uimage, type } = item
    let time = handleTime(lastTime, item.addtime)
    lastTime = item.addtime
    let typing = index === lastIndex

    // user
    if (ask) {
      return {
        ...config_role,
        key: id,
        time,
        content: compileMedia(type, ask),
        avatar: getFirstFilePath(uimage),
        placement: 'end',
        variant: 'filled',
      }
    }
    // ai
    if (uname === 'ai') {
      return {
        ...config_role,
        key: id,
        time,
        content: compileMedia(type, reply),
        avatar: avatart_ai,
        placement: 'start',
        variant: 'outlined',
        typing,
        isFog: true,
      }
    }

    // admin
    return {
      ...config_role,
      key: id,
      time,
      content: compileMedia(type, reply),
      // uimage不存在，说明是管理员的招呼语
      avatar: getFirstFilePath(uimage),
      placement: 'start',
      variant: 'outlined',
    }
  })
  list.value = newList
}
function handleTime(lastTime, currentTime) {
  let currentTime_dayjs = dayjs(currentTime)
  let lastTime_dayjs = lastTime ? dayjs(lastTime) : null
  let time = ''
  const isToday = currentTime_dayjs.isSame(dayjs(), 'day')

  time = isToday
    ? currentTime_dayjs.format('HH:mm')
    : currentTime_dayjs.format('YYYY年MM月DD日 HH:mm')

  if (!lastTime_dayjs) {
    return time
  }

  // 距离上一条5分钟内的、连续的，不显示
  // 计算时间差（分钟），取绝对值
  const diffInMinutes = Math.abs(lastTime_dayjs.diff(currentTime_dayjs, 'minute'))
  // 判断是否在 5 分钟以内
  if (diffInMinutes <= 5) {
    time = null
  }
  return time
}

// ----------------------------------
// ---------- 输入框 ---------------
// ----------------------------------
const senderRef = ref()
const senderValue = ref('')
const senderLoading = ref(false)
const uploadRef = ref(null)
// 发送
async function sendMsg(type = 1, content) {
  senderLoading.value = true
  try {
    // 文本和表情
    let data = {
      userid,
      ask: content,
      uname,
      uimage,
      type,
    }

    await addAPI(tableName, data)

    websocketSend(content)
    // [2] 更新聊天记录
    fetchData()

    type = 1 && (senderValue.value = '')
  } catch (error) {}
  senderLoading.value = false
}

// 上传文件
function openFileDialog() {
  uploadRef.value.click()
}
function fileUploadSuccess(res, file, fileList) {
  let type = 2,
    fileName = file.raw.name,
    fileUrl = 'upload/' + res.file,
    content = fileUrl + '|' + fileName,
    fileType = file.raw?.type || ''

  switch (true) {
    case fileType.startsWith('image'):
      // 图片
      type = 2
      break
    case fileType.startsWith('video'):
      // 视频
      type = 3
      break
    case fileType.startsWith('audio'):
      // 音频
      type = 6
      break

    default:
      // 文件
      type = 4
      break
  }

  sendMsg(type, content)
}

function sendQuickQuestion(text) {
  senderValue.value = text
  sendMsg(1, text)
}
// 解析视频/文件/图片 格式的内容
function compileMedia(type, content) {
  let newContent, fileUrl, fileName
  if (type != 1) {
    let list = content.split('|')
    fileName = list[1]
    fileUrl = getFilePath(list[0])
  }
  switch (type) {
    case 1:
      newContent = content
      break

    case 2:
      newContent = `<img width="200px" src="${fileUrl}" alt="${fileName}"/>`
      break

    case 3:
      newContent = `<video controls width="200px"><source src="${fileUrl}" ></video>`
      break

    case 4:
      newContent = `[${fileName}](${fileUrl})`
      break

    case 6:
      newContent = `<audio controls width="200px" src="${fileUrl}"></audio>`
      break

    default:
      newContent = content
      break
  }

  return newContent
}

// ----------------------------------
// ---------- websocket -------------
// ----------------------------------

initWebSocket(adminid, userid, fetchData)
onBeforeUnmount(() => {
  closeWebSocket()
})
</script>
<template>
  <div class="chat-wrapper">
    <div class="chat-head">
      <div class="service-mark">
        <img :src="avatart_ai" alt="在线客服" draggable="false" />
      </div>
      <div class="service-copy">
        <strong>在线客服</strong>
        <span>在线解答预约、订单、宠物服务与售后问题</span>
      </div>
      <div class="service-state">
        <i></i>
        <span>在线</span>
      </div>
    </div>

    <div class="chat-body">
      <div class="empty-chat" v-if="!hasMessage">
        <strong>今天想了解什么？</strong>
        <span>可以直接输入问题，也可以先选择下方常用问题。</span>
      </div>

      <BubbleList :list="list">
        <template #header="{ item }">
          <div class="header">
            <span class="time" v-if="item.time">
              {{ item.time }}
            </span>
          </div>
        </template>
      </BubbleList>
    </div>

    <div class="quick-question-row">
      <button
        v-for="item in quickQuestions"
        :key="item"
        type="button"
        @click="sendQuickQuestion(item)"
      >
        {{ item }}
      </button>
    </div>

    <div class="chat-sender-panel">
      <Sender
        ref="senderRef"
        v-model="senderValue"
        :loading="senderLoading"
        @submit="sendMsg(1, senderValue)"
      >
        <template #prefix>
          <div class="prefix-self-wrap">
            <el-button @click="openFileDialog">
              <el-icon><Link /></el-icon>
            </el-button>
          </div>
        </template>
      </Sender>
    </div>

    <el-upload
      style="display: none"
      :action="action"
      :headers="headers"
      :on-success="fileUploadSuccess"
      :show-file-list="false"
    >
      <span ref="uploadRef"></span>
    </el-upload>
  </div>
</template>
