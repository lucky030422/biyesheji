<script setup>
/**
 * @description 个人中心
 */
import '@/style/center.scss'

// 注册表单组件
import '@/components/FormItem/index.js'
import { computed, provide, ref } from 'vue'

import Custom from './Custom.vue'
import Info from './Info.vue'
import Menus from './Menus.vue'

import tableConfigs from '@/utils/tableConfigs'
import { useUserInfo } from '@/store'
import { useRouter } from 'vue-router'

let router = useRouter()
// 检查用户是否登录
const userInfoStore = useUserInfo()
// if (!userInfoStore.userInfo.isLogin) {
//   router.push('/login')
// }

let tableName = localStorage.getItem('sessionTable')
let tableConfig = tableConfigs[tableName] || {}
let { table, columns, detailConfig } = tableConfig
columns = columns || []

const userAvatar = computed(() => userInfoStore.userInfo.avatar)
const userName = computed(() => {
  return userInfoStore.userInfo.username || localStorage.getItem('username') || '我的账号'
})
const dashboardStats = computed(() => [
  { label: '快捷入口', value: menuList.value.length, unit: '项' },
  { label: '资料字段', value: infoList.value.length, unit: '项' },
  { label: '个人操作', value: 3, unit: '项' },
])
const avatarColumn = computed(() => {
  let avatarNames = [
    detailConfig?.imgName,
    ...(detailConfig?.imgNames || []),
    'touxiang',
    'image',
    'avatarurl',
  ].filter(Boolean)

  return columns.find(column => avatarNames.includes(column.columnName) && column.form_type === 'YyFile')
})
// ----------------------------------
// ---------- 个人信息 ----------------
// ----------------------------------
const infoList = ref([])
infoEvent()
function infoEvent() {
  let excludeColumnTypes = ['图', '音', '视', '文', '编'] // 媒体类型不显示
  let excludeColumnNames = [
    'passwordwrongnum',
    'mima',
    'password',
    'status',
    'money',
    'pquestion',
    'panswer',
    'sfsh',
    'shhf',
    'clicktime',
    'browseduration',
    'thumbsupnum',
    'crazilynum',
    'clicknum',
    'storeupnum',
    'discussnum',
  ] // 排除的字段名
  let centerColumns = columns
    .filter(
      item =>
        !excludeColumnTypes.includes(item.type) && !excludeColumnNames.includes(item.columnName)
    )
  let emailColumn = centerColumns.find(column => {
    let name = column.columnName.toLowerCase()
    return name.includes('email') || name.includes('youxiang') || column.comments.includes('邮箱')
  })
  if (emailColumn) {
    centerColumns = [
      emailColumn,
      ...centerColumns.filter(column => column.columnName !== emailColumn.columnName),
    ]
  }
  centerColumns = centerColumns.slice(0, 6) // 只显示前6个字段
  // 更新个人信息
  let userForm = JSON.parse(localStorage.getItem('userForm') || '{}')

  let list = []
  centerColumns.forEach(column => {
    list.push({
      label: column.comments,
      value: userForm[column.columnName] || '',
      columnName: column.columnName,
      column,
    })
  })
  infoList.value = list
}

// ----------------------------------
// ---------- 菜单 ----------------
// ----------------------------------
const menuList = ref(getMenuList())
function getMenuList() {
  let list = [
    {
      label: '我的收藏',
      path: '/index/storeup',
      query: { type: 1 }
    },
    {
      label: '我的发布',
      path: '/index/myForum',
    },
  ]


  const filterTableNames = [
    'storeup',
    'systemintro',
    'aboutus',
    'menu',
  ]
  let roleMenu = JSON.parse(localStorage.getItem('roleMenu') || '[]')
  roleMenu.forEach(item => {
    item.child &&
      item.child.forEach(child => {
        let { menu, tableName } = child
        if (filterTableNames.includes(tableName)) {
          return
        }

        // 确定路径
        let path = '/index/' + tableName

        list.push({
          label: menu,
          tableName: tableName,
          path,
          query: { centerType: 1 }
        })
      })
  })

  return list
}

function menuEvent(item) {
  router.push({ path: item.path, query: item.query })
}


provide('center', {
  infoList,
  userAvatar,
  tableName,
  columns,
  avatarColumn,

  menuList,
  menuEvent,

  infoEvent,
})
</script>

<template>
  <div class="center-page">
    <section class="center-hero">
      <div class="center-hero-copy">
        <span class="center-kicker">个人工作台</span>
        <h1>个人中心</h1>
        <p>资料维护、服务订单和收藏内容统一管理。</p>
      </div>
      <div class="center-hero-profile">
        <div class="hero-avatar">
          <img :src="userAvatar" :alt="userName" draggable="false" />
        </div>
        <strong>{{ userName }}</strong>
        <span>宠物服务平台会员</span>
      </div>
    </section>

    <div class="center-stat-row">
      <div class="center-stat-card" v-for="item in dashboardStats" :key="item.label">
        <span>{{ item.label }}</span>
        <strong>{{ item.value }}</strong>
        <em>{{ item.unit }}</em>
      </div>
    </div>

    <div class="center-page-inner">
      <div class="left">
        <Menus />
        <Custom />
      </div>

      <div class="right">
        <Info />
      </div>
    </div>
  </div>
</template>
