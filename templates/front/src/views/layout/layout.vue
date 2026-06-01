<script setup>
import '@/style/top.scss'

import { ref, shallowRef, watch, watchEffect, defineAsyncComponent, provide, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

import Custom from './Custom.vue'
import HeaderTitle from './HeaderTitle.vue'
import LayoutContent from './LayoutContent.vue'
import LayoutFooter from './LayoutFooter.vue'
import LayoutMenu from './LayoutMenu.vue'
import Notice from './Notice.vue'
import RoleMenu from './RoleMenu.vue'
import Weather from './Weather.vue'

import projectConfig from '@/utils/project'
import base from '@/utils/base'
import axios from 'axios'
import { getOptionAPI } from '@/api/common'
import { getDetailAPI, updateAPI, getPageAPI } from '@/api/list'
import { isAuth } from '@/utils/auth'
import { 
  useUserInfo,
} from '@/store'

const router = useRouter()

// ----------------------------------
// ---------- 角色菜单 ---------------
// ----------------------------------
const roleMenus = ref([])
const userInfoStore = useUserInfo()
let userName = computed(() => userInfoStore.userInfo.username)
let userAvatar = computed(() => userInfoStore.userInfo.avatar)
let isLogin = computed(() => userInfoStore.userInfo.isLogin)
function getUserMenus(isLogin) {
  if (!isLogin) {
    roleMenus.value = []
    return
  }

  let menus = [
    {
      key: 'chat',
      icon: 'ChatLineSquare',
      label: '在线客服',
      action: () =>{
        dialogTitle.value = '在线客服'
        dialogComponent.value = ServiceChat
        dialogVisible.value = true
      }      
    },
    {
      key: 'center',
      url: '/index/center',
      icon: 'UserFilled',
      label: '个人中心',
      action: () =>{
        router.push('/index/center')
      }
    },
    {
      key: 'logout',
      icon: 'Back',
      label: '退出登录',
      action: () =>{
        // 前端登出
        userInfoStore.logOut()
        localStorage.removeItems()
        router.push('/index/home')
      }
    },
  ]
  roleMenus.value = menus
}
// 角色菜单点击事件
let roleMenuEvent = key => {
  let menu = roleMenus.value.find(menu => menu.key == key)
  menu.action()
}
// 登录
function loginEvent() {
  router.push('/login')
}

// ----------------------------------
// --------- 页面菜单 ----------------
// ----------------------------------
const menus = ref([])
// 更新菜单 + 提取二级菜单
async function getSubMenus() {
  let list = [
    {
      label: '首页',
      url: '/index/home',
    },
    {
      label: '宠物服务',
      url: '/index/chongwufuwu',
    },
    {
      label: '宠物用品',
      url: '/index/chongwuyongpin',
    },
    {
      label: '寄养服务',
      url: '/index/jiyangfuwu',
    },
    {
      label: '在售宠物',
      url: '/index/zaishouchongwu',
    },
    {
      label: '领养宠物',
      url: '/index/lingyangchongwu',
    },
    {
      label: '积分礼品',
      url: '/index/jifenlipin',
    },
    {
      label: '公告信息',
      url: '/index/news',
    },
    {
      label: '宠物论坛',
      url: '/index/forum',
    },
  ]
  // 判断是否有分类 --> 添加二级菜单
  try {
    for (let index = 0; index < list.length; index++) {
      const item = list[index]

      let { refTable, refColumn, columnName } = item
      if (refTable && refColumn) {
        let res = await getOptionAPI(refTable, refColumn)

        // 添加children字段
        item.children = res.data.map(i => {
          return {
            // 拼接query参数
            url: item.url + '?' + columnName + '=' + i,
            label: i,
          }
        })
      }
    }
  } catch (error) {} 
  menus.value = list
}

function clickEvent(item) {
  router.push(item.url)
}

watch(
  () => userInfoStore.userInfo.isLogin,
  isLogin => {
    getUserMenus(isLogin)
    getSubMenus()
  },
  { immediate: true }
)



// ----------------------------------
// ---------- 弹框 ---------------
// ----------------------------------
const dialogVisible = ref(false)
const dialogTitle = ref('弹框标题')
const dialogComponent = shallowRef(null)
let dialogData = {}

// ----------------------------------
// ---------- 客服 ----------------
// ----------------------------------
// 懒加载一个子组件
const ServiceChat = defineAsyncComponent(() => import('@/components/chat/ServiceChat.vue'))
const isServiceChatDialog = computed(() => dialogComponent.value === ServiceChat)

// ----------------------------------
// ------------ 底部 ----------------
// ----------------------------------
const footerContent = ref('')



provide('header', {


  isLogin,
  roleMenus,
  userName,
  userAvatar,
  roleMenuEvent,
  loginEvent,

  menus,
  clickEvent,

  footerContent,
})
</script>

<template>
  <div class="layout-page">
    
    <div class="header-wrapper">
      <HeaderTitle />
      <LayoutMenu />
      <Weather />
      <Notice />
      <RoleMenu />
    </div>
    <LayoutContent />
    <LayoutFooter />
    <Custom />
      

    <!-- 客服聊天 -->
    <el-dialog
      :class="['yy-dialog', { 'service-chat-dialog': isServiceChatDialog }]"
      v-model="dialogVisible"
      :title="dialogTitle"
      :width="isServiceChatDialog ? '94vw' : undefined"
      destroy-on-close
      :close-on-click-modal="false"
    >
      <component v-model="dialogVisible" :is="dialogComponent" :data="dialogData" />
    </el-dialog>

    <!-- 滚动到顶部 -->
    <el-backtop :right="100" :bottom="100" />

  </div>
</template>
