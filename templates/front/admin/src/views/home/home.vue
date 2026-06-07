<script setup>
/**
 * @description 首页
 */
import '@/style/home.scss';
import { onMounted, ref, provide } from 'vue'

import HomeChart from './HomeChart.vue'
import HomeCount from './HomeCount.vue'
import HomeNews from './HomeNews.vue'
import Custom from './Custom.vue'

import chartData from '@/components/Echart/chartData'
import { isAuth } from '@/utils/auth';
import { getCountAPI, getPageAPI } from '@/api/list'

// ----------------------------------
// ----------- 总数统计 --------------
// ----------------------------------
let initCountList = [
  {
    tableName: 'fuwudingdan',
    comments: '服务订单',
    count: 0,
  },
  {
    tableName: 'jiyangdingdan',
    comments: '寄养订单',
    count: 0,
  },
  {
    tableName: 'chongwudingdan',
    comments: '宠物订单',
    count: 0,
  },
  {
    tableName: 'shangpindingdan',
    comments: '商品订单',
    count: 0,
  },
]
// 当前角色的总数统计 (鉴权)
initCountList = initCountList.filter(item => isAuth(item.tableName, '首页总数'))
const roleCountList = ref(initCountList)
getCountDatas()
function getCountDatas() {
  roleCountList.value.forEach(async item => {
    let res = await getCountAPI(item.tableName)
    item.count = res.data
  })
}

// ----------------------------------
// ----------- 首页图表 --------------
// ----------------------------------
// 当前角色的首页统计 (鉴权)
const roleChartList = chartData.filter(item => item.showHome).filter(item => isAuth(item.tableName, '首页统计'))

// ----------------------------------
// ----------- 新闻资讯 --------------
// ----------------------------------
const newsData = ref({
  title: '公告信息',
  list: [],
})
getNews()
async function getNews() {
  let res = await getPageAPI('news', {
    page: 1,
    limit: 6,
  })
  newsData.value.list = res.data.list
}

onMounted(() => {
  setTimeout(() => {
    requestIdleCallback(() => {
      // 提前加载 列表页
      import("@/views/list/list.vue");
    });
  }, 1000);
});

provide('home', {
  roleCountList,
  roleChartList,
  newsData,
})
</script>

<template>
  <div
    class="home-wrapper"
    :style="
      $projectImages.bIndexBackgroundImg
        ? `background-image: url(${$projectImages.bIndexBackgroundImg})`
        : ''
    "
  >
    <section class="home-hero">
      <div>
        <p class="home-kicker">运营概览</p>
        <h1>宠物服务管理后台</h1>
        <p class="home-subtitle">订单、服务、寄养、商品数据统一看板</p>
      </div>
      <div class="home-hero-meta">
        <span>实时数据</span>
        <strong>{{ roleCountList.length }}</strong>
        <em>个统计模块</em>
      </div>
    </section>

    <HomeCount />  

    <section class="home-dashboard">
      <HomeChart />
      <HomeNews />
    </section>

    <Custom />
  </div>
</template>
