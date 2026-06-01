<script setup>
import '@/style/list.scss'
import '@/components/FormItem/index.js'

import { computed, shallowRef, ref, watchEffect, reactive, provide, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import BreadCrumb from './BreadCrumb.vue'
import Category from './Category.vue'
import ContentNormal from './Content.vue'
import ContentNews from './ContentNews.vue'
import ContentForum from './ContentForum.vue'
import Custom from './Custom.vue'
import Hot from './Hot.vue'
import Pagination from './Pagination.vue'
import Search from './Search.vue'
import Sort from './Sort.vue'

import ListEdit from './ListEdit.vue'
import ChartEntry from '@/components/Echart/index.vue'

import tableConfigs from '@/utils/tableConfigs'
import { alipayAPI, getOptionAPI, getRemindAPI } from '@/api/common'
import { 
  getListAPI, 
  getPageAPI, 
  predictAPI, 
  predictImgAPI,
  updateAPI,
  getForumListAPI,
  } from '@/api/list'
import { getAutoSort1API } from '@/api/front'
import { downloadFile, getNanoId } from '@/utils'
import { toDetailPage, toListPage } from '@/utils/navigate'
import getUiList from '@/utils/getUiList'
import { isAuth } from '@/utils/auth'
import getFilePath, { getFirstFilePath } from '@/utils/getFilePath'
import chartData from '@/components/Echart/chartData'

let { tableName } = defineProps(['tableName'])
let tableConfig = tableConfigs[tableName]
let { table, columns, searchColumns, detailConfig, headerButtons } = tableConfig
let { hasHot, comments } = table
hasHot = hasHot == '列' || hasHot == '全'
const hasOnshelves = columns.some(column => column.columnName === 'onshelves') // 上下架

const route = useRoute()
const router = useRouter()
const query = route.query
const centerType = query.centerType // 后台权限
const isGoodsPage = computed(() => tableName === 'chongwuyongpin')
const isServicePage = computed(() => tableName === 'chongwufuwu')
const isBoardingPage = computed(() => tableName === 'jiyangfuwu')
const isPetSalePage = computed(() => tableName === 'zaishouchongwu')
const isAdoptionPage = computed(() => tableName === 'lingyangchongwu')
const isGiftPage = computed(() => tableName === 'jifenlipin')
const isNewsPage = computed(() => tableName === 'news')
const isForumPage = computed(() => tableName === 'forum')
const goodsHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(20, 42, 27, .9), rgba(20, 42, 27, .56) 48%, rgba(20, 42, 27, .12)), url("${getFilePath('upload/chongwuyongpin_全期猫粮1.jpg')}")`,
}))
const serviceHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(18, 42, 45, .92), rgba(18, 42, 45, .62) 52%, rgba(18, 42, 45, .16)), url("${getFilePath('upload/chongwufuwu_宠物犬上门洗护遛护套餐1.jpg')}")`,
}))
const boardingHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(43, 35, 25, .9), rgba(43, 35, 25, .58) 50%, rgba(43, 35, 25, .16)), url("${getFilePath('upload/jiyangfuwu_全天候寄宿寄养1.jpg')}")`,
}))
const petSaleHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(31, 38, 58, .92), rgba(31, 38, 58, .58) 50%, rgba(31, 38, 58, .16)), url("${getFilePath('upload/zaishouchongwu_布偶猫1.jpg')}")`,
}))
const adoptionHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(30, 45, 38, .92), rgba(30, 45, 38, .58) 50%, rgba(30, 45, 38, .16)), url("${getFilePath('upload/lingyangchongwu_布丁1.jpg')}")`,
}))
const giftHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(55, 38, 72, .92), rgba(55, 38, 72, .58) 50%, rgba(55, 38, 72, .16)), url("${getFilePath('upload/jifenlipin_互动羽毛逗猫棒1.jpg')}")`,
}))
const newsHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(24, 35, 52, .92), rgba(24, 35, 52, .58) 50%, rgba(24, 35, 52, .16)), url("${getFilePath('upload/news_picture1.jpg')}")`,
}))
const forumHeroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(35, 43, 37, .92), rgba(35, 43, 37, .58) 50%, rgba(35, 43, 37, .16)), url("${getFilePath('upload/forum_狗狗感冒1.jpg')}")`,
}))

// 内容列表
let Content = ContentNormal
switch (tableName) {
  case 'news':
    Content = ContentNews
    break;

  case 'forum':
    Content = ContentForum
    break;

  default:
    Content = ContentNormal
    break;
}
// ----------------------------------
// ---------- 面包屑 ----------------
// ----------------------------------
const homePath = ref('/index/home')
const second = ref({
  path: null,
  title: null,
})
const lastTitle = ref(comments)
function backEvent(){
  router.back()
}

// ----------------------------------
// ---------- 搜索配置 ---------------
// ----------------------------------
// 搜索参数
const searchData = ref({})
// 表单项
const columns_search = ref(getSearchColumns())
function getSearchColumns() {
  let list = searchColumns.slice(0)

  // 前台不显示 是否审核搜索
  if (table.sfsh == '是' && !centerType) {
    list = list.filter(column => column.columnName != 'sfsh')
  }

  // 不同角色展示不同的搜索字段
  let role = localStorage.getItem('role')
  list = list.filter(column => {
    let { queryFlagInput = ['是'] } = column
    return queryFlagInput.includes('是') || queryFlagInput.includes(role)
  })

  return list
}

// 表单数据
const ruleForm = reactive(getRuleForm())
function getRuleForm() {
  let data = {}
  columns_search.value.forEach(column => {
    let { columnName } = column
    data[columnName] = ''
  })

  return data
}

// 搜索事件
function searchEvent() {
  let data = {}

  columns_search.value.forEach(column => {
    let { columnName, form_type } = column

    // 无值直接返回
    if (ruleForm[columnName] === '' || ruleForm[columnName] === undefined) {
      return
    }

    // 区间的--> 精准搜索，不带%
    if (column.isRangeSearch) {
      data[columnName] = ruleForm[columnName]
      return
    }

    // 根据form_type的值做一次转换
    switch (form_type) {
      // 文本框 --> 模糊搜索
      case 'YyText':
        data[columnName] = '%' + ruleForm[columnName] + '%'
        break

      // 多选
      case 'YyMultilSelect':
        data[columnName] = ruleForm[columnName]
          .split(',')
          .map(value => '%' + value + '%')
          .join(',')
        break

      default:
        data[columnName] = ruleForm[columnName]
        break
    }
  })

  searchData.value = data
}

// 按钮列表
let headerButtons_auth = headerButtons.filter(button => button.isPublic || isAuth(tableName, button.name, !centerType))
let headerEventMap = {
  add,
}
function headerButtonEvent(button) {
  let { key, title, type } = button

  if (type === 'statis') {
    // 其它表的统计
    return showChart(button)
  }

  // 根据key执行对应的key事件
  if (headerEventMap[key]) {
    return headerEventMap[key](button)
  }

  ElMessage.info(`【${title}】该功能暂时未添加`)
}

function add(button) {
  dialogTitle.value = button.title
  dialogComponent.value = ListEdit
  dialogClass.value = ''
  dialogData = {
    type: 'add', // add: 新增 update: 编辑 cross: 跨表
    id: '',
    tableName,
    defaultData: {
      ...route.params,
      ...route.query,
    },    
    okText: '提交',
    cancleText: '取消',
  }
  dialogVisible.value = true
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
// ------------ 分页 ----------------
// ----------------------------------
const currentPage = ref(1)
const pageSize = ref(12)
const total = ref(0)

// ----------------------------------
// ------------ 分类 ----------------
// ----------------------------------
const list_category = ref([])
const act_category = ref('')
const hasCategory = ref(false)
let categoryConfig = {
  refTable: '',
  refColumn: '',
  columnName: '',
}

initCategory()
// 初始化分类配置
function initCategory() {
  columns.forEach(column => {
    let { categoryFlag, refTable, refColumn, columnName } = column
    if (categoryFlag == '是' && refTable && refColumn) {
      hasCategory.value = true
      categoryConfig.refTable = refTable
      categoryConfig.refColumn = refColumn
      categoryConfig.columnName = columnName

      // 路由query是否有分类字段
      if (query && query[columnName]) {
        act_category.value = query[columnName]
      }
    }
  })
}
getCategoryList()
// 获取分类数据
async function getCategoryList() {
  let { refTable, refColumn } = categoryConfig
  if (!hasCategory.value) {
    return
  }
  let res = await getOptionAPI(refTable, refColumn)
  list_category.value = res.data
}
function categoryEvent(item) {
  act_category.value = item
}

// ----------------------------------
// ------------ 排序 ----------------
// ----------------------------------
const list_sort = ref(detailConfig.sortList || [])
const actItem_sort = ref({
  sort: '',
  order: '',
})
function sortEvent(item) {
  let newOrder = ''
  let { sort, order } = item
  if (actItem_sort.value.sort !== sort) {
    // 切换了排序的sort，默认从升序开始
    newOrder = 'asc'
  } else {
    // 同一sort，但order需要切换，升序asc  -> 降序desc -> 不排序
    switch (order) {
      case 'asc':
        newOrder = 'desc'
        break

      case 'desc':
        newOrder = ''
        break

      default:
        newOrder = 'asc'
        break
    }
  }

  // 更新sortData
  if (!newOrder) {
    actItem_sort.value = {}
  } else {
    actItem_sort.value = {
      sort,
      order: newOrder,
    }
  }

  // 更新sortList的order字段
  list_sort.value.forEach(item => {
    item.order = item.sort === sort ? newOrder : ''
  })
}

// 合并两个sort
let sortData = computed(() => {
  let { sortName, sortOrder } = detailConfig // 初始配置的
  let { sort, order } = actItem_sort.value // 用户点击的

  if (!sortName && !sort) {
    return {}
  }
  let newSorts = [],
    newOrder = []
  // 高权重
  if (sort) {
    newSorts.push(sort)
    newOrder.push(order)
  }
  // 低权重
  if (sortName) {
    newSorts.push(sortName)
    newOrder.push(sortOrder)
  }
  return {
    sort: newSorts.join(','),
    order: newOrder.join(','),
  }
})

// ----------------------------------
// ----------- 热门信息 --------------
// ----------------------------------
const hotData = ref({
  comments: '热门信息',
  tableName,
  subtitle: 'Hot',
  list: [],
})
getHotList()
async function getHotList() {
  if (!hasHot) {
    return
  }
  let apiParams = {
    limit: 6,
  }
  let res = await getAutoSort1API(tableName, apiParams)
  hotData.value.list = getUiList(detailConfig, res.data.list)
}

// ----------------------------------
// ------------ 提醒 ----------------
// ----------------------------------
let remindTitles = ref([]) // 数组嵌套数组,多个提醒
let remindColumnNames = ref([]) // 数组
function remindEvent() {
  let index = -1
  columns.forEach(async column => {
    let remind_type_map = {
      数: 1,
      日: 2,
      字: 3,
    }
    let type = remind_type_map[column.remind]
    // 是否有提醒功能
    if (!type) {
      return
    }

    index += 1 // 数组索引
    let columnIndex = index
    let { remindStart, remindEnd, columnName, comments, remindInput } = column
    remindColumnNames.value[columnIndex] = columnName
    remindTitles.value[columnIndex] = []

    let params = {}
    remindStart && (params.remindstart = remindStart)
    remindEnd && (params.remindend = remindEnd)

    // 请求统计count
    let res = await getRemindAPI(tableName, columnName, type, params)
    let { count } = res
    if (count > 0) {
      remindTitles.value[columnIndex] = res.data

      let nameStr = res.data.join('、')
      ElNotification({
        title: comments,
        message: `
          <div>${count}条数据到达预警线。</div>
          <p>${remindInput}</p>
          <p>${nameStr}</p>
        `,
        dangerouslyUseHTMLString: true,
        type: 'warning',
        duration: 1000 * 12,
      })
    }
  })
}

onMounted(() => {
  centerType && remindEvent()
})

// ----------------------------------
// ---------- 图表功能 ---------------
// ----------------------------------
function showChart(button) {
  let { title } = button
  dialogData = chartData.find(item => item.tableName === tableName && item.title == title)
  dialogData = {
    ...dialogData,
    title: ''
  }

  dialogClass.value = 'list-chart-wrapper'
  dialogComponent.value = ChartEntry
  dialogTitle.value = title
  dialogVisible.value = true
}


// ----------------------------------
// ----------- 拉取数据 --------------
// ----------------------------------
const isLoading = ref(false)
const listData = ref({
  comments,
  tableName,
  subtitle: tableName,
  list: [],
  sourceList: [],
})
async function fetchData(fetchParams) {
  isLoading.value = true
  try {
    let apiParams = {
      // 搜索
      ...searchData.value,

      // 排序
      ...sortData.value,

      // 分页
      limit: pageSize.value,
      page: currentPage.value,

      ...fetchParams,
    }

    // 上下架 + 前台
    if (hasOnshelves && !centerType) {
      apiParams.onshelves = 1
    }

    // 审核 + 前台
    if (table.sfsh == '是' && !centerType) {
      apiParams.sfsh = '是'
    }

    // 分类
    if (act_category.value) {
      apiParams[categoryConfig.columnName] = act_category.value
    }

    let api = query.centerType ? getPageAPI : getListAPI

    // 兼容特殊表: forum论坛
    if (tableName == 'forum') {
      apiParams.isdone = '开放'
      apiParams.delflag = 0
      if (apiParams.sort) {
        apiParams.sort = 'istop,toptime,' + apiParams.sort
        apiParams.order = 'desc,desc,' + apiParams.order
      }else{
         apiParams.sort = 'istop,toptime'
        apiParams.order = 'desc,desc'
      }
      api = getForumListAPI
    }

    let res = await api(tableName, apiParams)
    listData.value.list = getUiList(detailConfig, res.data.list)
    listData.value.sourceList = res.data.list

    // 修改分页
    total.value = res.data.total
  } catch (error) {}

  isLoading.value = false
}
watchEffect(() => {
  fetchData()
})

function detailEvent(tableName, id) {
  toDetailPage(tableName, id, centerType)
}

function moreEvent(tableName) {
  toListPage(tableName, centerType)
}

provide('listFront', {
  homePath,
  second,
  lastTitle,
  backEvent,

  list_category,
  act_category,
  categoryEvent,

  columns: columns_search,
  ruleForm,
  searchEvent,
  headerButtons: headerButtons_auth,
  headerButtonEvent,

  list_sort,
  actItem_sort,
  sortEvent,

  currentPage,
  pageSize,
  total,

  listData,
  isLoading,

  hasHot,
  hotData,
  detailEvent,
  moreEvent,
})

// 确保 BreadCrumb能复用 后台的
provide('header', {
  homePath,
  second,
  lastTitle,
  backEvent,
})
// 确保 list能复用 首页的
provide('start', {
  detailEvent,
  moreEvent,
})
provide('detail', {
  detailEvent,
  moreEvent,
})
</script>

<template>
  <div class="list-page" :data-key="tableName">
      <div class="forum-channel" v-if="isForumPage">
        <section class="forum-hero" :style="forumHeroStyle">
          <div class="forum-hero-copy">
            <span class="forum-kicker">健康问答 · 养宠经验 · 互动交流</span>
            <h1>把养宠问题拿出来讨论</h1>
            <p>集中展示社区帖子、发布人、互动数据和开放状态，让用户快速找到值得参与的讨论。</p>
          </div>
          <aside class="forum-card">
            <small>社区入口</small>
            <h2>先看热帖，再进讨论</h2>
            <div class="forum-row"><span>讨论内容</span><strong>健康 / 服务 / 日常</strong></div>
            <div class="forum-row"><span>检索方式</span><strong>标题搜索</strong></div>
            <div class="forum-row"><span>参与方式</span><strong>发帖与回复</strong></div>
          </aside>
        </section>

        <section class="forum-promises">
          <div class="forum-promise"><span>问</span><strong>问题集中</strong><em>把常见养宠问题沉淀在论坛里。</em></div>
          <div class="forum-promise"><span>答</span><strong>经验参考</strong><em>用户经验和平台内容共同补充。</em></div>
          <div class="forum-promise"><span>搜</span><strong>标题检索</strong><em>保留原有标题搜索和分页。</em></div>
          <div class="forum-promise"><span>聊</span><strong>进入讨论</strong><em>列表预览内容，详情页参与互动。</em></div>
        </section>
      </div>

      <div class="news-channel" v-if="isNewsPage">
        <section class="news-hero" :style="newsHeroStyle">
          <div class="news-hero-copy">
            <span class="news-kicker">平台公告 · 服务动态 · 宠物知识</span>
            <h1>快速了解平台最新消息</h1>
            <p>把重要通知、服务调整和宠物知识集中展示，用户可以快速浏览摘要并进入详情阅读。</p>
          </div>
          <aside class="news-card">
            <small>阅读重点</small>
            <h2>先看摘要，再进详情</h2>
            <div class="news-row"><span>内容类型</span><strong>公告 / 动态 / 知识</strong></div>
            <div class="news-row"><span>信息入口</span><strong>标题搜索</strong></div>
            <div class="news-row"><span>阅读方式</span><strong>列表预览</strong></div>
          </aside>
        </section>

        <section class="news-promises">
          <div class="news-promise"><span>告</span><strong>公告集中</strong><em>平台通知和服务安排统一展示。</em></div>
          <div class="news-promise"><span>读</span><strong>摘要清晰</strong><em>列表页直接查看标题和简介。</em></div>
          <div class="news-promise"><span>找</span><strong>标题检索</strong><em>保留原有标题搜索和分页。</em></div>
          <div class="news-promise"><span>藏</span><strong>收藏参考</strong><em>收藏数据辅助判断关注度。</em></div>
        </section>
      </div>

      <div class="gift-channel" v-if="isGiftPage">
        <section class="gift-hero" :style="giftHeroStyle">
          <div class="gift-hero-copy">
            <span class="gift-kicker">积分兑换 · 库存提醒 · 宠物好物</span>
            <h1>把积分换成实用礼品</h1>
            <p>集中展示兑换积分、库存、规格和礼品简介，让用户快速判断是否值得兑换。</p>
          </div>
          <aside class="gift-card">
            <small>兑换重点</small>
            <h2>先看积分，再看库存</h2>
            <div class="gift-row"><span>兑换方式</span><strong>积分抵扣</strong></div>
            <div class="gift-row"><span>库存提醒</span><strong>低库存优先关注</strong></div>
            <div class="gift-row"><span>兑换入口</span><strong>详情页提交</strong></div>
            <button type="button">查看积分礼品</button>
          </aside>
        </section>

        <section class="gift-promises">
          <div class="gift-promise"><span>分</span><strong>积分清晰</strong><em>每件礼品所需积分在卡片中直接展示。</em></div>
          <div class="gift-promise"><span>库</span><strong>库存可查</strong><em>库存数量前置，减少无效兑换。</em></div>
          <div class="gift-promise"><span>选</span><strong>分类筛选</strong><em>按礼品名称和类型快速查找。</em></div>
          <div class="gift-promise"><span>换</span><strong>在线兑换</strong><em>列表查看意向，详情页完成兑换。</em></div>
        </section>
      </div>

      <div class="adoption-channel" v-if="isAdoptionPage">
        <section class="adoption-hero" :style="adoptionHeroStyle">
          <div class="adoption-hero-copy">
            <span class="adoption-kicker">待领养 · 性格匹配 · 申请跟进</span>
            <h1>给宠物找到更合适的家</h1>
            <p>把品种、性别、年龄、性格特点和疫苗记录前置展示，帮助用户更认真地完成领养选择。</p>
          </div>
          <aside class="adoption-card">
            <small>领养前先了解</small>
            <h2>看性格，也看照护准备</h2>
            <div class="adoption-row"><span>基础档案</span><strong>品种 / 性别 / 年龄</strong></div>
            <div class="adoption-row"><span>健康参考</span><strong>疫苗记录</strong></div>
            <div class="adoption-row"><span>申请入口</span><strong>详情页提交</strong></div>
            <button type="button">查看可领养宠物</button>
          </aside>
        </section>

        <section class="adoption-promises">
          <div class="adoption-promise"><span>性</span><strong>性格透明</strong><em>性格特点前置，帮助判断是否适合家庭。</em></div>
          <div class="adoption-promise"><span>健</span><strong>健康参考</strong><em>疫苗记录作为领养前的基础参考。</em></div>
          <div class="adoption-promise"><span>审</span><strong>申请跟进</strong><em>详情页发起领养申请，后续统一处理。</em></div>
          <div class="adoption-promise"><span>爱</span><strong>理性领养</strong><em>先了解照护需求，再决定是否申请。</em></div>
        </section>
      </div>

      <div class="pet-sale-channel" v-if="isPetSalePage">
        <section class="pet-sale-hero" :style="petSaleHeroStyle">
          <div class="pet-sale-hero-copy">
            <span class="pet-sale-kicker">健康档案 · 待售状态 · 在线购买</span>
            <h1>更快找到合适的新成员</h1>
            <p>把品种、年龄、性别、健康记录和出售状态集中展示，帮助用户在列表页完成第一轮筛选。</p>
          </div>
          <aside class="pet-sale-card">
            <small>选购重点</small>
            <h2>先看健康，再看喜好</h2>
            <div class="pet-sale-row"><span>健康记录</span><strong>疫苗 / 驱虫</strong></div>
            <div class="pet-sale-row"><span>出售状态</span><strong>待出售优先</strong></div>
            <div class="pet-sale-row"><span>购买入口</span><strong>详情页下单</strong></div>
            <button type="button">查看在售宠物</button>
          </aside>
        </section>

        <section class="pet-sale-promises">
          <div class="pet-sale-promise"><span>档</span><strong>档案清晰</strong><em>基础信息、出生日期和健康记录前置。</em></div>
          <div class="pet-sale-promise"><span>筛</span><strong>快速筛选</strong><em>按昵称、品种、种类和状态查找。</em></div>
          <div class="pet-sale-promise"><span>健</span><strong>健康参考</strong><em>疫苗与驱虫记录辅助判断。</em></div>
          <div class="pet-sale-promise"><span>购</span><strong>在线购买</strong><em>列表查看意向，详情页完成购买。</em></div>
        </section>
      </div>

      <div class="boarding-channel" v-if="isBoardingPage">
        <section class="boarding-hero" :style="boardingHeroStyle">
          <div class="boarding-hero-copy">
            <span class="boarding-kicker">日托 · 短期寄养 · 全天候寄宿</span>
            <h1>让临时托管更安心</h1>
            <p>把寄养类型、适配宠物、包含项目和价格前置展示，帮助用户快速筛选合适的托管套餐。</p>
          </div>
          <aside class="boarding-plan-card">
            <small>寄养预约</small>
            <h2>按天数和宠物习惯选择</h2>
            <div class="plan-row"><span>照护模式</span><strong>日托 / 寄宿</strong></div>
            <div class="plan-row"><span>基础项目</span><strong>喂养、清洁、陪护</strong></div>
            <div class="plan-row"><span>预约入口</span><strong>详情页提交</strong></div>
            <button type="button">查看寄养套餐</button>
          </aside>
        </section>

        <section class="boarding-promises">
          <div class="boarding-promise"><span>住</span><strong>独立休息区</strong><em>按宠物体型与习惯安排托管空间。</em></div>
          <div class="boarding-promise"><span>喂</span><strong>按需喂养</strong><em>支持自带口粮和个性化照护记录。</em></div>
          <div class="boarding-promise"><span>看</span><strong>状态反馈</strong><em>寄养过程可通过详情和订单持续跟进。</em></div>
          <div class="boarding-promise"><span>约</span><strong>在线寄养</strong><em>列表筛选套餐，详情页完成预约。</em></div>
        </section>
      </div>

      <div class="service-channel" v-if="isServicePage">
        <section class="service-hero" :style="serviceHeroStyle">
          <div class="service-hero-copy">
            <span class="service-kicker">上门喂养 · 洗护护理 · 寄养照料</span>
            <h1>把宠物照护预约变得更清楚</h1>
            <p>围绕服务类型、宠物类型、服务范围和时长做集中展示，让用户在列表页就能快速判断适合的照护方案。</p>
          </div>
          <aside class="service-quick-card">
            <small>快速预约服务</small>
            <h2>先看范围，再选时间</h2>
            <div class="quick-row"><span>服务类型</span><strong>洗护 / 喂养 / 寄养</strong></div>
            <div class="quick-row"><span>宠物类型</span><strong>猫犬通用</strong></div>
            <div class="quick-row"><span>服务时长</span><strong>30-120 分钟</strong></div>
            <button type="button">查看可预约服务</button>
          </aside>
        </section>

        <section class="service-promises">
          <div class="service-promise"><span>护</span><strong>专人照护</strong><em>服务人员按类型与宠物情况匹配。</em></div>
          <div class="service-promise"><span>记</span><strong>过程记录</strong><em>洗护、喂养、寄养进度便于追踪。</em></div>
          <div class="service-promise"><span>约</span><strong>在线预约</strong><em>列表页强化预约入口，详情页完成提交。</em></div>
          <div class="service-promise"><span>评</span><strong>评价反馈</strong><em>浏览、收藏和评论数据辅助选择。</em></div>
        </section>
      </div>

      <div class="goods-channel" v-if="isGoodsPage">
        <section class="goods-hero" :style="goodsHeroStyle">
          <div class="goods-hero-copy">
            <span class="goods-kicker">精选粮食 · 零食 · 护理用品</span>
            <h1>给宠物的一站式补给清单</h1>
            <p>把商品筛选、热销推荐、库存和购买入口提前展示，让宠物用品页更像可下单的商城列表。</p>
          </div>
          <aside class="goods-deal">
            <small>今日推荐</small>
            <h2>全期猫粮家庭装</h2>
            <p>高复购主粮优先展示，适合首页和列表页联动推荐。</p>
            <div class="deal-price"><strong>¥129</strong><span>¥159</span></div>
            <button type="button">在线购买</button>
          </aside>
        </section>

        <section class="goods-promises">
          <div class="promise"><span>✓</span><strong>正品优选</strong><em>主粮、零食、护理用品统一筛选。</em></div>
          <div class="promise"><span>库</span><strong>库存可查</strong><em>库存紧张商品在卡片中提前提示。</em></div>
          <div class="promise"><span>购</span><strong>在线购买</strong><em>列表页强化购买入口，详情页完成下单。</em></div>
          <div class="promise"><span>服</span><strong>售后服务</strong><em>订单、发货和退款信息统一跟踪。</em></div>
        </section>
      </div>

      <BreadCrumb />

      <div class="list-box">

        <div class="left">
          <Search />
          <Sort />
          <Content :data="listData" :hideHeader="true" v-loading="isLoading" />
          <Pagination />
          <Custom />
        </div>

        <div class="right" v-if="hasCategory || hasHot">
          <Category v-if="hasCategory" />
          <Hot :data="hotData" v-if="hasHot"/>
        </div>
        
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
        @openDialog="openDialog"
      />
    </el-dialog>
  </div>
</template>
