<script setup>
import '@/style/forum.scss'
import '@/components/FormItem/index.js'

import { ref, reactive, provide, computed, shallowRef } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import BreadCrumb from '../list/BreadCrumb.vue'
import Content from './Content.vue'
import ButtonList from './ButtonList.vue'
import Videos from './Videos.vue'
import DiscussForm from './DiscussForm.vue'
import DiscussList from './DiscussList.vue'
import ListEdit from '../list/ListEdit.vue'

import tableConfigs from '@/utils/tableConfigs'
import {
  addAPI,
  deleteAPI,
  getDetailAPI,
  getForumDetailAPI,
  getListAPI,
  updateAPI,
} from '@/api/list'
import { getFilePaths } from '@/utils/getFilePath'
import { hanldeSensitiveWords } from '@/utils'
const tableName = 'forum'
let tableConfig = tableConfigs[tableName]
let { table, columns, detailConfig } = tableConfig
let {
  imgName,
  imgNames,
  titleName,
  videoNames,
  hasIsanon,
} = detailConfig
let { comments, storeUp, thumbsUp } = table

const route = useRoute()
const router = useRouter()
let { id, centerType } = route.query
id = Number(id) 
const userid = Number(localStorage.getItem('userid')) // 未登录为 0
const username = localStorage.getItem('username')
const avatarurl = localStorage.getItem('useravatar')
// ----------------------------------
// ---------- 面包屑 ----------------
// ----------------------------------
const homePath = ref('/index/home')
const second = ref({
  path: centerType ? '/index/' + tableName + '?centerType=' + centerType : '/index/' + tableName,
  title: comments,
})
const lastTitle = computed(() => {
  return data.value.title
})
function backEvent() {
  router.back()
}

// ----------------------------------
// ------------ 点赞 ----------------
// ----------------------------------
const hasThumbsUp = thumbsUp == '是' // 是否有点赞功能
const thumbsUpId = ref(null) // 是否已点赞
async function getThumbsUp() {
  let params = {
    page: 1,
    limit: 1,
    type: 21,
    refid: id,
    tablename: tableName,
    userid,
  }
  let res1 = await getListAPI('storeup', params)
  thumbsUpId.value = res1.data.total > 0 ? res1.data.list[0].id : null
}
// 点赞/取消赞
async function thumbsUpEvent() {
  let num
  if (thumbsUpId.value) {
    // 删除
    await deleteAPI('storeup', [thumbsUpId.value])

    thumbsUpId.value = null
    ElMessage.success('取消点赞成功')
    num = -1
    data.value.thumbsupnum += num
  } else {
    // 新增
    let params = {
      name: data.value[titleName],
      picture: data.value[imgName],
      refid: id,
      type: 21,
      tablename: tableName,
      userid,
    }
    let res = await addAPI('storeup', params)
    thumbsUpId.value = res.data
    num = +1
    data.value.thumbsupnum += num
    ElMessage.success('点赞成功')
  }
  // 更新点赞数量
  let { data: detailData } = await getDetailAPI(tableName, id)
  detailData.thumbsupnum += num
  data.value.thumbsupnum = detailData.thumbsupnum
  await updateAPI(tableName, detailData)
}

// ----------------------------------
// ------------ 收藏 ----------------
// ----------------------------------
const hasStoreUp = storeUp == '是' // 是否有收藏功能
const storeUpId = ref(null) // 是否已点赞
async function getStoreUp() {
  let params = {
    page: 1,
    limit: 1,
    type: 22,
    refid: id,
    tablename: tableName,
    userid,
  }
  let res1 = await getListAPI('storeup', params)
  storeUpId.value = res1.data.total > 0 ? res1.data.list[0].id : null
}
// 点赞/取消赞
async function storeUpEvent() {
  let num
  if (storeUpId.value) {
    // 删除
    await deleteAPI('storeup', [storeUpId.value])

    storeUpId.value = null
    ElMessage.success('取消收藏成功')
    num = -1
    data.value.storeupnum += num
  } else {
    // 新增
    let params = {
      name: data.value[titleName],
      picture: data.value[imgName],
      refid: id,
      type: 21,
      tablename: tableName,
      userid,
    }
    let res = await addAPI('storeup', params)
    storeUpId.value = res.data
    num = +1
    data.value.storeupnum += num
    ElMessage.success('收藏成功')
  }
  // 更新点赞数量
  let { data: detailData } = await getDetailAPI(tableName, id)
  detailData.storeupnum += num
  data.value.storeupnum = detailData.storeupnum
  await updateAPI(tableName, detailData)
}

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
// ----------- 举报 --------------
// ----------------------------------
const hasReport = false;
async function reportEvent() {
  let res = await getListAPI('forumreport', {
    forumid: id,
    userid,
    page: 1,
    limit: 1,
    status: '处理中'
  })
  if (res.data.total > 0) {
    ElMessage.info('您已经举报了，请先等待审核处理。')
    return
  }
  dialogTitle.value = '举报'
  dialogClass.value = ''
  dialogComponent.value = ListEdit
  dialogData = {
    type: 'add', // add: 新增 update: 编辑 cross: 跨表
    id: '',
    tableName: 'forumreport',
    defaultData: {
      forumid: id,
      title: data.value.title,
      userid,
      username,
      reporteduserid: data.value.userid,
      reportedusername: data.value.username,
      
    },
    okText: '提交',
    cancleText: '取消',
  }
  dialogVisible.value = true
}
// ----------------------------------
// ----------- 图片 --------------
// ----------------------------------
const banners = ref([])
const showBanner = ref(false)
function getPicture() {
  let list = []
  imgNames.forEach(name => {
    let urls = getFilePaths(data.value[name])
    list = urls.map(picture => {
      return {
        id: picture,
        picture,
      }
    })
  })
  banners.value = list
  showBanner.value = true
}
function bannerEvent() {}

// ----------------------------------
// ----------- 视频 --------------
// ----------------------------------
const videoList = ref([])
function getVideo() {
  let list = []
  videoNames.forEach(name => {
    let urls = getFilePaths(data.value[name])
    list.push(...urls)
  })
  videoList.value = list
}

// ----------------------------------
// ----------- 输入框 --------------
// ----------------------------------
const ruleForm = ref({
  content: '',
})
const formLoading = ref(false)

// 评论 / 回复
async function formOkEvent(content, replyId) {
  let parentid = replyId ? replyId : id
  if (formLoading.value) {
    return
  }

  if (!content) {
    ElMessage.error('请先输入内容')
    return
  }

  formLoading.value = true

  try {
    content = await hanldeSensitiveWords(content)

    let discussData = {
      content,
      parentid,
      userid,
      avatarurl,
      username,
    }

    await addAPI(tableName, discussData)

    fetchData()

    ElMessage.success(replyId ? '回复成功' : '评论成功')
    ruleForm.value.content = ''
  } catch (error) {
    let msg = error.message || error.msg || ''
    ElMessage.error(msg)
  }

  formLoading.value = false
}

// ----------------------------------
// ------------ 评论列表 -------------
// ----------------------------------
const discussList = ref([])

// 拉取评论列表
async function getDiscussList(childs) {
  if (!childs) {
    discussList.value = []
    return
  }

  childs.sort((a, b) => new Date(b.addtime) - new Date(a.addtime))

  childs.forEach(item => {
    item.img = getFilePaths(item.avatarurl)
    item.hasRemove = item.userid == userid
    if (item.childs) {
      item.childs.forEach(i => {
        i.img = getFilePaths(i.avatarurl)
        i.hasRemove = i.userid == userid
      })
    }
  })
  discussList.value = childs
}

function remove(id) {
  ElMessageBox.confirm('确认删除?', '提示', {
    confirmButtonText: '删除',
    cancelButtonText: '取消',
    type: 'warning',
  })
    .then(async () => {
      await deleteAPI(tableName, [id])
      ElMessage.success('删除成功')
      fetchData()
    })
    .catch(() => {})
}
function reply(item) {
  ElMessageBox.prompt('请输入回复内容', '回复: ' + item.username, {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    inputPattern: /.+/,
    inputErrorMessage: '请输入回复内容',
    inputType: 'textarea',
  })
    .then(({ value }) => {
      formOkEvent(value, item.id)
    })
    .catch(() => {})
}

// ----------------------------------
// ----------- 数据 -----------------
// ----------------------------------
const data = ref({})
fetchData()
async function fetchData() {
  let res = await getForumDetailAPI(tableName, id)

  // 匿名
  res.data.user = res.data.isanon == 1 ? '匿名' : res.data.username
  // 评论列表
  getDiscussList(res.data.childs)
  delete res.data.childs

  data.value = res.data

  // 视频
  getVideo()

  hasThumbsUp && getThumbsUp()
  hasStoreUp && getStoreUp()
}

provide('detail', {
  id,
  data,

  homePath,
  second,
  lastTitle,
  backEvent,

  banners,
  showBanner,
  bannerEvent,

  hasThumbsUp,
  thumbsUpId,
  thumbsUpEvent,
  hasStoreUp,
  storeUpId,
  storeUpEvent,

  videoList,

  formLoading,
  formOkEvent,
  ruleForm,

  discussList,
  remove,
  reply, 
  hasReport,
  reportEvent,
})

// 确保 BreadCrumb能复用 后台的
provide('header', {
  homePath,
  second,
  lastTitle,
  backEvent,

  banners,
  showBanner,
  bannerEvent,
})
</script>
<template>
  <div class="forumdetail-page">
    
    <BreadCrumb />
    <Content />
    <ButtonList />
    <Videos />
    <DiscussForm />
    <DiscussList />
    <Custom />
  

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
      />
    </el-dialog>
  </div>
</template>
