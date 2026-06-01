<script setup>
/**
 * @description 首页 - A方案业务转化型
 */
import '@/style/start.scss'

import { computed, onMounted, ref } from 'vue'

import { getDetailAPI, getListAPI } from '@/api/list'
import { getAutoSort1API, getAutoSort2API } from '@/api/front'
import { getFilePath, getFirstFilePath } from '@/utils/getFilePath'
import { toDetailPage, toListPage } from '@/utils/navigate'
import getUiList from '@/utils/getUiList'

const fallbackImages = {
  hero: getFilePath('upload/chongwufuwu_宠物犬上门洗护遛护套餐1.jpg'),
  profile: getFilePath('upload/chongwuxinxi_团团1.jpg'),
  news: getFilePath('upload/forum_猫咪结膜炎1.jpg'),
  serviceCat: getFilePath('upload/chongwufuwu_宠物猫上门洗护喂养套餐1.jpg'),
  serviceDaily: getFilePath('upload/chongwufuwu_日常萌宠喂养遛护服务1.jpg'),
  serviceSpecial: getFilePath('upload/chongwufuwu_异宠上门照料服务1.jpg'),
  goodsCat: getFilePath('upload/chongwuyongpin_全期猫粮1.jpg'),
  goodsCare: getFilePath('upload/chongwuyongpin_全价犬用磨牙棒1.jpg'),
  goodsSnack: getFilePath('upload/chongwuyongpin_冻干鸡肉猫零食1.jpg'),
}

const quickEntries = [
  {
    icon: '🏠',
    title: '寄养预约',
    desc: '日托、短期寄养、全天候寄宿。',
    tableName: 'jiyangfuwu',
  },
  {
    icon: '🛁',
    title: '宠物服务',
    desc: '洗护、遛护、上门照料与训练。',
    tableName: 'chongwufuwu',
  },
  {
    icon: '🛒',
    title: '宠物用品',
    desc: '猫粮犬粮、玩具、护理用品。',
    tableName: 'chongwuyongpin',
  },
  {
    icon: '🤝',
    title: '领养宠物',
    desc: '查看待领养宠物与申请进度。',
    tableName: 'lingyangchongwu',
  },
]

const serviceFallbacks = [
  {
    id: 8,
    tableName: 'chongwufuwu',
    img: fallbackImages.serviceCat,
    tag: '猫咪护理',
    title: '宠物猫上门洗护喂养套餐',
    desc: '适合出差、短途旅行期间的清洁与喂养照护。',
    price: '¥89 起',
  },
  {
    id: 3,
    tableName: 'chongwufuwu',
    img: fallbackImages.serviceDaily,
    tag: '日常照料',
    title: '日常萌宠喂养遛护服务',
    desc: '按时喂养、陪伴互动、遛护记录同步给用户。',
    price: '¥59 起',
  },
  {
    id: 5,
    tableName: 'chongwufuwu',
    img: fallbackImages.serviceSpecial,
    tag: '异宠照护',
    title: '异宠上门照料服务',
    desc: '覆盖兔、鸟、仓鼠等特殊照护需求。',
    price: '¥69 起',
  },
]

const goodsFallbacks = [
  {
    id: 5,
    tableName: 'chongwuyongpin',
    img: fallbackImages.goodsCat,
    tag: '猫粮',
    title: '全期猫粮',
    desc: '适合多阶段猫咪日常营养补充。',
    price: '¥129',
  },
  {
    id: 4,
    tableName: 'chongwuyongpin',
    img: fallbackImages.goodsCare,
    tag: '护理',
    title: '全价犬用磨牙棒',
    desc: '磨牙洁齿，适合服务后复购推荐。',
    price: '¥39',
  },
  {
    id: 7,
    tableName: 'chongwuyongpin',
    img: fallbackImages.goodsSnack,
    tag: '零食',
    title: '冻干鸡肉猫零食',
    desc: '训练奖励和日常互动都适用。',
    price: '¥49',
  },
]

const newsFallbacks = [
  {
    id: 'notice-1',
    title: '端午假期寄养预约开放通知',
    desc: '热门时间段建议提前 3 天预约。',
  },
  {
    id: 'notice-2',
    title: '新增异宠基础照护服务',
    desc: '覆盖仓鼠、鹦鹉、兔等常见异宠。',
  },
  {
    id: 'notice-3',
    title: '宠物论坛上线健康问答专区',
    desc: '用户可按宠物类型浏览经验分享。',
  },
]

const recommendList = ref([])
const newsData = ref({
  tableName: 'news',
  comments: '公告信息',
  sfsh: '否',
  subtitle: 'news',
  titleNames: ['title'],
  titleHeads: [''],
  imgName: 'picture',
  pubPeopleName: '',
  sortName: '',
  sortOrder: 'desc',
  list: [],
})
const systemIntroduceData = ref({})

const heroStyle = computed(() => ({
  backgroundImage: `linear-gradient(90deg, rgba(16, 33, 20, .82) 0%, rgba(16, 33, 20, .54) 45%, rgba(16, 33, 20, .18) 100%), url("${fallbackImages.hero}")`,
}))

const serviceCards = computed(() => buildCards('chongwufuwu', serviceFallbacks, '服务'))
const goodsCards = computed(() => buildCards('chongwuyongpin', goodsFallbacks, '商品'))

const newsItems = computed(() => {
  let list = newsData.value.list || []
  if (!list.length) {
    return newsFallbacks
  }

  return list.slice(0, 3).map((item, index) => ({
    id: item.id || `news-${index}`,
    title: getCardTitle(item, `平台公告 ${index + 1}`),
    desc: item.introduction || '查看平台最新通知、服务动态和宠物知识。',
  }))
})

const leadNews = computed(() => {
  let first = (newsData.value.list || [])[0]
  return {
    id: first?.id || 'lead-news',
    img: first?.img || fallbackImages.news,
    title: first ? getCardTitle(first, '猫咪眼部护理与日常观察') : '猫咪眼部护理与日常观察',
    desc: first?.introduction || '通过平台内容沉淀护理知识，提升用户对服务专业度的判断。',
  }
})

function buildCards(tableName, fallbacks, tagFallback) {
  let source = recommendList.value.find(item => item.tableName === tableName)
  let list = source?.list || []
  if (!list.length) {
    return fallbacks
  }

  return list.slice(0, 3).map((item, index) => ({
    id: item.id,
    tableName,
    img: item.img || fallbacks[index]?.img,
    tag: item.titles?.[1] || fallbacks[index]?.tag || tagFallback,
    title: getCardTitle(item, fallbacks[index]?.title || tagFallback),
    desc: tableName === 'chongwufuwu'
      ? '服务信息、预约时间和订单进度可在平台统一查看。'
      : '精选宠物用品，适合与服务预约一起完成选购。',
    price: item.price !== undefined ? `¥${item.price}` : fallbacks[index]?.price,
  }))
}

function getCardTitle(item, fallback) {
  return item?.titles?.filter(Boolean)?.[0] || item?.title || fallback
}

function goList(tableName) {
  toListPage(tableName)
}

function goDetail(card) {
  if (card.id && !String(card.id).includes('-')) {
    toDetailPage(card.tableName, card.id)
    return
  }
  toListPage(card.tableName)
}

async function getRecommendList() {
  let configs = [
    {
      tableName: 'chongwufuwu',
      comments: '宠物服务推荐',
      subtitle: 'chongwufuwu Recommend',
      isIntelRecom: true,
      titleNames: ['fuwumingcheng', 'fuwuleixing', 'jifen'],
      titleHeads: ['', '', '服务价格'],
      imgName: 'fuwufengmian',
      pubPeopleName: '',
      sortName: '',
      sortOrder: 'desc',
      list: [],
    },
    {
      tableName: 'chongwuyongpin',
      comments: '宠物用品推荐',
      subtitle: 'chongwuyongpin Recommend',
      isIntelRecom: true,
      titleNames: ['shangpinmingcheng', 'shangpinleixing', 'jiage'],
      titleHeads: ['', '', '价格'],
      imgName: 'shangpinfengmian',
      pubPeopleName: '',
      sortName: '',
      sortOrder: 'desc',
      list: [],
    },
  ]

  recommendList.value = configs

  configs.forEach(async item => {
    let apiParams = {
      limit: 3,
    }
    let res
    if (item.isIntelRecom && localStorage.getItem('Token')) {
      try {
        res = await getAutoSort2API(item.tableName, apiParams)
      } catch (error) {
      }
    }
    if (!res || res.code !== 0) {
      res = await getAutoSort1API(item.tableName, apiParams)
    }
    item.list = getUiList(item, res.data.list)
  })
}

async function getNewsList() {
  let res = await getListAPI(newsData.value.tableName, {
    limit: 3,
  })
  newsData.value.list = getUiList(newsData.value, res.data.list)
}

async function getIntroductionData() {
  let { data } = await getDetailAPI('systemintro', '1')
  data.picture1 = getFirstFilePath(data.picture1)
  data.picture2 = getFirstFilePath(data.picture2)
  data.picture3 = getFirstFilePath(data.picture3)
  systemIntroduceData.value = data
}

getRecommendList()
getNewsList()
getIntroductionData()

onMounted(() => {
  setTimeout(() => {
    let idle = window.requestIdleCallback || (callback => setTimeout(callback, 0))
    idle(() => {
      import('@/views/list/list.vue')
      import('@/views/detail/detail.vue')
    })
  }, 1000)
})
</script>

<template>
  <div class="home-page home-business-a">
    <section class="home-hero" :style="heroStyle">
      <div class="home-shell hero-layout">
        <div class="hero-copy">
          <span class="home-kicker">今日可预约 18 个寄养名额</span>
          <h1>让每一次托付都有记录可查</h1>
          <p>面向宠物寄养、上门喂养、洗护服务、宠物用品与领养信息的一站式预约平台，帮助用户快速找到合适服务。</p>
          <div class="hero-actions">
            <button class="home-btn primary" @click="goList('jiyangfuwu')">预约寄养服务</button>
            <button class="home-btn ghost" @click="goList('zaishouchongwu')">查看在售宠物</button>
          </div>
        </div>

        <aside class="booking-card">
          <h2>快速匹配服务</h2>
          <div class="booking-grid">
            <div class="booking-field"><span>服务类型</span><strong>上门喂养</strong></div>
            <div class="booking-field"><span>宠物类型</span><strong>猫 / 犬 / 异宠</strong></div>
            <div class="booking-field"><span>预约时间</span><strong>今天 14:00 后</strong></div>
            <div class="booking-field"><span>服务范围</span><strong>附近门店</strong></div>
          </div>
          <button class="home-btn primary block" @click="goList('chongwufuwu')">查看可预约档期</button>
        </aside>
      </div>
    </section>

    <div class="home-shell metric-grid" aria-label="平台数据">
      <div class="metric-card"><strong>8+</strong><span>服务品类</span></div>
      <div class="metric-card"><strong>1200+</strong><span>累计预约</span></div>
      <div class="metric-card"><strong>96%</strong><span>好评反馈</span></div>
      <div class="metric-card"><strong>24h</strong><span>在线客服响应</span></div>
    </div>

    <section class="home-section">
      <div class="home-shell">
        <div class="section-head">
          <div>
            <h2>常用入口</h2>
            <p>把首页最关键的交易入口提前，减少用户寻找服务的时间。</p>
          </div>
          <button class="home-btn" @click="goList('chongwufuwu')">全部服务</button>
        </div>
        <div class="quick-grid">
          <button
            v-for="entry in quickEntries"
            :key="entry.tableName"
            class="quick-card"
            @click="goList(entry.tableName)"
          >
            <span class="quick-icon">{{ entry.icon }}</span>
            <strong>{{ entry.title }}</strong>
            <span>{{ entry.desc }}</span>
          </button>
        </div>
      </div>
    </section>

    <section class="home-section">
      <div class="home-shell">
        <div class="section-head">
          <div>
            <h2>精选宠物服务</h2>
            <p>优先展示可转化的热门服务，卡片信息聚焦价格、场景和行动按钮。</p>
          </div>
          <button class="home-btn" @click="goList('chongwufuwu')">查看更多</button>
        </div>
        <div class="card-grid">
          <article
            v-for="card in serviceCards"
            :key="card.id"
            class="home-card"
            @click="goDetail(card)"
          >
            <img :src="card.img" :alt="card.title" draggable="false" />
            <div class="home-card-body">
              <span class="home-tag">{{ card.tag }}</span>
              <h3>{{ card.title }}</h3>
              <p>{{ card.desc }}</p>
              <div class="price-row">
                <span class="price">{{ card.price }}</span>
                <span>预约</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="home-section process-band">
      <div class="home-shell split-layout">
        <img class="process-image" :src="fallbackImages.profile" alt="平台宠物档案" draggable="false" />
        <div>
          <div class="section-head compact">
            <div>
              <h2>预约流程更清晰</h2>
              <p>用简单流程解释服务闭环，让用户知道下单后会发生什么。</p>
            </div>
          </div>
          <div class="step-list">
            <div class="step-card"><span>1</span><div><h3>选择服务与宠物信息</h3><p>填写宠物类型、年龄、健康备注和服务时间。</p></div></div>
            <div class="step-card"><span>2</span><div><h3>匹配门店或服务人员</h3><p>系统根据范围、档期和服务类型推荐可选项。</p></div></div>
            <div class="step-card"><span>3</span><div><h3>完成预约并跟踪记录</h3><p>服务过程、订单状态和反馈统一在个人中心查看。</p></div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="home-section">
      <div class="home-shell">
        <div class="section-head">
          <div>
            <h2>宠物用品推荐</h2>
            <p>把用品销售与服务预约放在同一消费路径里。</p>
          </div>
          <button class="home-btn" @click="goList('chongwuyongpin')">进入商城</button>
        </div>
        <div class="card-grid">
          <article
            v-for="card in goodsCards"
            :key="card.id"
            class="home-card"
            @click="goDetail(card)"
          >
            <img :src="card.img" :alt="card.title" draggable="false" />
            <div class="home-card-body">
              <span class="home-tag">{{ card.tag }}</span>
              <h3>{{ card.title }}</h3>
              <p>{{ card.desc }}</p>
              <div class="price-row">
                <span class="price">{{ card.price }}</span>
                <span>加入购物车</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="home-section">
      <div class="home-shell">
        <div class="section-head">
          <div>
            <h2>公告与宠物知识</h2>
            <p>保留原首页资讯属性，但降低干扰，把内容作为信任补充。</p>
          </div>
          <button class="home-btn" @click="goList('news')">全部公告</button>
        </div>
        <div class="news-grid">
          <article class="lead-news" @click="goList('news')">
            <img :src="leadNews.img" :alt="leadNews.title" draggable="false" />
            <div class="home-card-body">
              <span class="home-tag">健康知识</span>
              <h3>{{ leadNews.title }}</h3>
              <p>{{ leadNews.desc }}</p>
            </div>
          </article>
          <div class="news-list">
            <article
              v-for="item in newsItems"
              :key="item.id"
              class="news-item"
              @click="goList('news')"
            >
              <h3>{{ item.title }}</h3>
              <p>{{ item.desc }}</p>
            </article>
          </div>
        </div>

        <div class="home-cta">
          <div>
            <h2>准备给宠物安排一次安心照护？</h2>
            <p>从预约、服务到售后记录，首页直接引导用户完成关键动作。</p>
          </div>
          <button class="home-btn light" @click="goList('jiyangfuwu')">立即预约</button>
        </div>
      </div>
    </section>
  </div>
</template>
