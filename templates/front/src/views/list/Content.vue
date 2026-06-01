<script setup>
/**
 * @description 列表
 *
 * data.title 标题
 * data.subtitle 副标题
 * data.tableName 表名
 * data.list 单个列表的数据
 * data.hasMusic 音乐
 * data.musicEvent 音乐点击事件
 *
 * item.img 图片
 * item.titles 标题列表,可能多个标题
 * item.price 价格,可能没有 undefined判断
 * item.user 发布人,可能没有 undefined判断
 * item.addtime 发布时间
 * item.thumbsupnum 点赞,可能没有 undefined判断
 * item.storeupnum 收藏,可能没有 undefined判断
 * item.clicknum 查看量,可能没有 undefined判断
 * item.browseduration 浏览时长,可能没有 undefined判断
 *
 * hideHeader 隐藏头部
 * detailEvent 点击详情事件
 * moreEvent 更多事件
 */
import { computed, inject } from 'vue'
import dayjs from 'dayjs'

let { data, hideHeader } = defineProps(['data', 'hideHeader'])
let { detailEvent, moreEvent } = inject('start')
const isGoodsPage = computed(() => data.tableName === 'chongwuyongpin')
const isServicePage = computed(() => data.tableName === 'chongwufuwu')
const isBoardingPage = computed(() => data.tableName === 'jiyangfuwu')
const isPetSalePage = computed(() => data.tableName === 'zaishouchongwu')
const isAdoptionPage = computed(() => data.tableName === 'lingyangchongwu')
const isGiftPage = computed(() => data.tableName === 'jifenlipin')

function goodsPrice(item) {
  return item.sourceData?.jiage ?? item.price
}

function goodsStock(item) {
  return item.sourceData?.kucun
}

function goodsType(item) {
  return item.sourceData?.shangpinleixing || item.titles?.[1]
}

function goodsBrand(item) {
  return item.sourceData?.pinpai
}

function goodsIntro(item) {
  return item.sourceData?.shangpinjianjie || '精选宠物用品，适合日常喂养、护理和互动场景。'
}

function servicePrice(item) {
  return item.sourceData?.jifen ?? item.price
}

function serviceType(item) {
  return item.sourceData?.fuwuleixing || item.titles?.[1]
}

function servicePetType(item) {
  return item.sourceData?.chongwuleixing
}

function serviceDuration(item) {
  return item.sourceData?.fuwushizhang
}

function serviceRange(item) {
  return item.sourceData?.fuwufanwei
}

function serviceIntro(item) {
  return item.sourceData?.fuwujieshao || '专业宠物照护服务，适合日常喂养、洗护护理和临时托管。'
}

function boardingPrice(item) {
  return item.sourceData?.jifen ?? item.price
}

function boardingType(item) {
  return item.sourceData?.fuwuleixing || item.titles?.[1]
}

function boardingPetType(item) {
  return item.sourceData?.chongwuleixing
}

function boardingItems(item) {
  return item.sourceData?.baohanxiangmu || '喂养、清洁、陪护、基础状态观察。'
}

function boardingIntro(item) {
  return item.sourceData?.xiangqing?.replace(/<[^>]*>/g, '') || '适合出差、旅行和短期照护场景的宠物寄养服务。'
}

function petSalePrice(item) {
  return item.sourceData?.jifen ?? item.price
}

function petSaleBreed(item) {
  return item.sourceData?.chongwupinzhong || item.titles?.[1]
}

function petSaleType(item) {
  return item.sourceData?.zhonglei
}

function petSaleGender(item) {
  return item.sourceData?.xingbie
}

function petSaleBirthday(item) {
  return item.sourceData?.chushengriqi
}

function petSaleStatus(item) {
  return item.sourceData?.chushouzhuangtai || item.titles?.[3]
}

function petSaleHealth(item) {
  const vaccine = item.sourceData?.yimiaojilu
  const deworm = item.sourceData?.quchongjilu
  if (vaccine && deworm) return `疫苗：${vaccine}；驱虫：${deworm}`
  return vaccine || deworm || '可在详情页查看健康记录。'
}

function petSaleIntro(item) {
  const color = item.sourceData?.yanse
  const hobby = item.sourceData?.aihao
  if (color && hobby) return `${color}，${hobby}`
  return color || hobby || '性格与生活习惯可在详情页进一步了解。'
}

function adoptionBreed(item) {
  return item.sourceData?.chongwupinzhong || item.titles?.[1]
}

function adoptionGender(item) {
  return item.sourceData?.xingbie
}

function adoptionBirthday(item) {
  return item.sourceData?.chushengriqi
}

function adoptionStatus(item) {
  return item.sourceData?.lingyangzhuangtai || item.titles?.[2]
}

function adoptionPersonality(item) {
  return item.sourceData?.xinggetedian || '性格特点可在详情页进一步了解。'
}

function adoptionVaccine(item) {
  return item.sourceData?.yimiaojilu || '可在详情页查看疫苗记录。'
}

function giftPoints(item) {
  return item.sourceData?.duihuanjifen ?? item.price
}

function giftType(item) {
  return item.sourceData?.lipinleixing || item.titles?.[1]
}

function giftSpec(item) {
  return item.sourceData?.guige
}

function giftStock(item) {
  return item.sourceData?.kucun
}

function giftIntro(item) {
  return item.sourceData?.lipinjianjie || '精选宠物积分礼品，适合日常互动、护理和奖励场景。'
}
</script>

<template>
  <div class="listfront-default" :class="{ 'goods-listfront': isGoodsPage, 'service-listfront': isServicePage, 'boarding-listfront': isBoardingPage, 'pet-sale-listfront': isPetSalePage, 'adoption-listfront': isAdoptionPage, 'gift-listfront': isGiftPage }">
    <div
      class="item"
      v-for="item in data.list"
      :key="item.id"
      @click="detailEvent(data.tableName, item.id)"
    >
      <div class="item-inner">
        <div class="img-box" v-if="item.img || data.hasMusic">
          <img
            v-if="data.hasMusic"
            class="music"
            src="http://codegen.caihongy.cn/20251230/096adf8336ff4c9397450b81c24cc10f.png"
            @click.stop="data.musicEvent(item)"
          />
          <img class="cover" v-if="item.img" :src="item.img" draggable="false" />
        </div>
        <div class="info-box" v-if="!isGoodsPage && !isServicePage && !isBoardingPage && !isPetSalePage && !isAdoptionPage && !isGiftPage">
          <div class="goodtitle" v-for="title in item.titles">{{ title }}</div>
          <div class="price" v-if="item.price !== undefined">￥ {{ item.price }}</div>
          <div class="user" v-if="item.user !== undefined">
            <span>发布人:</span>
            <span>{{ item.user }}</span>
          </div>
          <div class="time">
            <span>发布时间:</span>
            <span>{{ dayjs(item.addtime).format('YYYY-MM-DD') }}</span>
          </div>
          <div class="other" v-if="item.thumbsupnum !== undefined">
            <span>点赞:</span>
            <span>{{ item.thumbsupnum }}</span>
          </div>
          <div class="other" v-if="item.storeupnum !== undefined">
            <span>收藏:</span>
            <span>{{ item.storeupnum }}</span>
          </div>
          <div class="other" v-if="item.clicknum !== undefined">
            <span>查看:</span>
            <span>{{ item.clicknum }}</span>
          </div>
          <div class="other" v-if="item.browseduration !== undefined">
            <span>时长:</span>
            <span>{{ item.browseduration }}</span>
          </div>
        </div>
        <div class="info-box gift-info" v-else-if="isGiftPage">
          <div class="gift-meta">
            <span>{{ giftType(item) || '积分礼品' }}</span>
            <span v-if="giftSpec(item)">{{ giftSpec(item) }}</span>
          </div>
          <div class="goodtitle">{{ item.titles?.[0] }}</div>
          <div class="gift-desc">{{ giftIntro(item) }}</div>
          <div class="gift-stats">
            <span v-if="giftStock(item) !== undefined">库存 {{ giftStock(item) }}</span>
            <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
            <span v-if="item.discussnum !== undefined">评论 {{ item.discussnum }}</span>
          </div>
          <div class="gift-exchange-row">
            <div class="points" v-if="giftPoints(item) !== undefined">{{ giftPoints(item) }} 积分</div>
            <button type="button" @click.stop="detailEvent(data.tableName, item.id)">在线兑换</button>
          </div>
        </div>
        <div class="info-box adoption-info" v-else-if="isAdoptionPage">
          <div class="adoption-meta">
            <span>{{ adoptionBreed(item) || '领养宠物' }}</span>
            <span v-if="adoptionStatus(item)" class="adoption-status">{{ adoptionStatus(item) }}</span>
          </div>
          <div class="goodtitle">{{ item.titles?.[0] }}</div>
          <div class="adoption-tags">
            <span v-if="adoptionGender(item)">{{ adoptionGender(item) }}</span>
            <span v-if="adoptionBirthday(item)">{{ dayjs(adoptionBirthday(item)).format('YYYY-MM-DD') }}</span>
          </div>
          <div class="adoption-desc">{{ adoptionPersonality(item) }}</div>
          <div class="adoption-health">疫苗：{{ adoptionVaccine(item) }}</div>
          <div class="adoption-stats">
            <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
            <span v-if="item.discussnum !== undefined">评论 {{ item.discussnum }}</span>
          </div>
          <div class="adoption-action-row">
            <button type="button" @click.stop="detailEvent(data.tableName, item.id)">领养申请</button>
          </div>
        </div>
        <div class="info-box pet-sale-info" v-else-if="isPetSalePage">
          <div class="pet-sale-meta">
            <span>{{ petSaleBreed(item) || '在售宠物' }}</span>
            <span v-if="petSaleStatus(item)" class="pet-sale-status">{{ petSaleStatus(item) }}</span>
          </div>
          <div class="goodtitle">{{ item.titles?.[0] }}</div>
          <div class="pet-sale-tags">
            <span v-if="petSaleType(item)">{{ petSaleType(item) }}</span>
            <span v-if="petSaleGender(item)">{{ petSaleGender(item) }}</span>
            <span v-if="petSaleBirthday(item)">{{ dayjs(petSaleBirthday(item)).format('YYYY-MM-DD') }}</span>
          </div>
          <div class="pet-sale-desc">{{ petSaleIntro(item) }}</div>
          <div class="pet-sale-health">{{ petSaleHealth(item) }}</div>
          <div class="pet-sale-stats">
            <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
            <span v-if="item.discussnum !== undefined">评论 {{ item.discussnum }}</span>
          </div>
          <div class="pet-sale-buy-row">
            <div class="price" v-if="petSalePrice(item) !== undefined">￥{{ petSalePrice(item) }}</div>
            <button type="button" @click.stop="detailEvent(data.tableName, item.id)">在线购买</button>
          </div>
        </div>
        <div class="info-box boarding-info" v-else-if="isBoardingPage">
          <div class="boarding-meta">
            <span>{{ boardingType(item) || '寄养服务' }}</span>
            <span v-if="boardingPetType(item)">{{ boardingPetType(item) }}</span>
          </div>
          <div class="goodtitle">{{ item.titles?.[0] }}</div>
          <div class="boarding-desc">{{ boardingIntro(item) }}</div>
          <div class="boarding-items">{{ boardingItems(item) }}</div>
          <div class="boarding-stats">
            <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
            <span v-if="item.discussnum !== undefined">评论 {{ item.discussnum }}</span>
          </div>
          <div class="boarding-book-row">
            <div class="price" v-if="boardingPrice(item) !== undefined">￥{{ boardingPrice(item) }}</div>
            <button type="button" @click.stop="detailEvent(data.tableName, item.id)">在线寄养</button>
          </div>
        </div>
        <div class="info-box service-info" v-else-if="isServicePage">
          <div class="service-meta">
            <span>{{ serviceType(item) || '宠物服务' }}</span>
            <span v-if="servicePetType(item)">{{ servicePetType(item) }}</span>
          </div>
          <div class="goodtitle">{{ item.titles?.[0] }}</div>
          <div class="service-desc">{{ serviceIntro(item) }}</div>
          <div class="service-stats">
            <span v-if="serviceRange(item)">范围 {{ serviceRange(item) }}</span>
            <span v-if="serviceDuration(item)">时长 {{ serviceDuration(item) }}</span>
            <span v-if="item.clicknum !== undefined">浏览 {{ item.clicknum }}</span>
            <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
          </div>
          <div class="service-book-row">
            <div class="price" v-if="servicePrice(item) !== undefined">￥{{ servicePrice(item) }}</div>
            <button type="button" @click.stop="detailEvent(data.tableName, item.id)">在线预约</button>
          </div>
        </div>
        <div class="info-box goods-info" v-else>
          <div class="goods-meta">
            <span>{{ goodsType(item) || '宠物用品' }}</span>
            <span v-if="goodsBrand(item)">{{ goodsBrand(item) }}</span>
          </div>
          <div class="goodtitle">{{ item.titles?.[0] }}</div>
          <div class="goods-desc">{{ goodsIntro(item) }}</div>
          <div class="goods-stats">
            <span v-if="goodsStock(item) !== undefined">库存 {{ goodsStock(item) }}</span>
            <span v-if="item.clicknum !== undefined">浏览 {{ item.clicknum }}</span>
            <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
          </div>
          <div class="goods-buy-row">
            <div class="price" v-if="goodsPrice(item) !== undefined">¥{{ goodsPrice(item) }}</div>
            <button type="button" @click.stop="detailEvent(data.tableName, item.id)">在线购买</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.listfront-default {
  width: 100%;
  height: auto;
  padding: 20px 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 20px;
  font-size: 14px;
}

.listfront-default .item {
  flex: 0 0 auto;
  width: calc(25% - 20px);
  height: auto;
  padding: 0px;
  border: 0px solid #eee;
  position: relative;
  cursor: pointer;
  background: #fff;
  transition: boxShadow 0.3s linear, transform 0.3s linear;
  border-radius: 6px;
}

.listfront-default .item .item-inner {
  display: block;
  gap: 0px;
}

.listfront-default .item .item-inner .img-box {
  width: 100%;
  max-height: 320px;
  overflow: hidden;
  position: relative;
  border-radius: 6px 6px 0 0;
  .music {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 60px;
    height: 60px;
    z-index: 9;
  }
}
.listfront-default .item .item-inner .img-box .cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 6px 6px 0 0;
}

.listfront-default .item .img-box .cover {
  width: 100%;
  height: 320px;
  object-fit: cover;
  transition: transform 0.3s linear;
}
.listfront-default .item:hover .img-box .cover {
  transform: scale(1.05);
}

.listfront-default .item .item-inner .info-box {
  width: 100%;
  height: auto;
  text-decoration: none;
  color: #333;
  cursor: pointer;
  text-indent: 1em;
  line-height: 24px;
  /*初始化隐藏多余文字*/
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  background: none;
  /* 背景变灰 */
  transition: all 0.6s;
}

.listfront-default .item .item-inner .info-box .goodtitle {
  width: 100%;
  font-size: 16px;
  color: #333;
  font-weight: 600;
  margin-bottom: 6px;
}
.listfront-default .item .item-inner .info-box .price {
  width: 100%;
  color: #e72c59;
  font-size: 16px;
  font-weight: 600;
  margin: 0 0 6px;
}
.listfront-default .item .item-inner .info-box .user {
  margin: 0 0 6px;
}
.listfront-default .item .item-inner .info-box .time {
  margin: 0 0 6px;
}
.listfront-default .item .item-inner .info-box .other {
  margin: 0 6px 6px 0;
  display: inline-block;
}

.goods-listfront {
  gap: 18px;
}

.goods-listfront .item {
  width: calc(33.333% - 12px);
  border: 1px solid #e4e8df;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(24, 43, 29, 0.06);
}

.goods-listfront .item:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(24, 43, 29, 0.12);
}

.goods-listfront .item .item-inner .img-box {
  aspect-ratio: 4 / 3;
  max-height: none;
  border-radius: 8px 8px 0 0;
}

.goods-listfront .item .img-box .cover,
.goods-listfront .item .item-inner .img-box .cover {
  height: 100%;
  border-radius: 8px 8px 0 0;
}

.goods-listfront .item .item-inner .goods-info {
  padding: 16px;
  text-indent: 0;
  white-space: normal;
  overflow: visible;
  line-height: 1.5;
}

.goods-listfront .goods-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #687064;
  font-size: 13px;
}

.goods-listfront .item .item-inner .goods-info .goodtitle {
  min-height: 52px;
  margin: 10px 0 8px;
  color: #1f241f;
  font-size: 19px;
  line-height: 1.35;
}

.goods-listfront .goods-desc {
  min-height: 44px;
  margin-bottom: 12px;
  color: #687064;
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.goods-listfront .goods-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 13px;
  color: #687064;
  font-size: 13px;
}

.goods-listfront .goods-stats span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #f5f6f1;
}

.goods-listfront .goods-buy-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.goods-listfront .item .item-inner .goods-info .price {
  width: auto;
  margin: 0;
  color: #d85d3f;
  font-size: 23px;
  font-weight: 900;
}

.goods-listfront .goods-buy-row button {
  min-height: 38px;
  padding: 8px 13px;
  border: 0;
  border-radius: 8px;
  background: #2f6f4e;
  color: #fff;
  font-weight: 900;
  cursor: pointer;
}

.service-listfront {
  gap: 18px;
}

.service-listfront .item {
  width: calc(33.333% - 12px);
  border: 1px solid #dce8e7;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(21, 55, 58, 0.07);
}

.service-listfront .item:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(21, 55, 58, 0.13);
}

.service-listfront .item .item-inner .img-box {
  aspect-ratio: 4 / 3;
  max-height: none;
  border-radius: 8px 8px 0 0;
}

.service-listfront .item .img-box .cover,
.service-listfront .item .item-inner .img-box .cover {
  height: 100%;
  border-radius: 8px 8px 0 0;
}

.service-listfront .item .item-inner .service-info {
  padding: 16px;
  text-indent: 0;
  white-space: normal;
  overflow: visible;
  line-height: 1.5;
}

.service-listfront .service-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #617172;
  font-size: 13px;
}

.service-listfront .item .item-inner .service-info .goodtitle {
  min-height: 52px;
  margin: 10px 0 8px;
  color: #182a2d;
  font-size: 19px;
  line-height: 1.35;
}

.service-listfront .service-desc {
  min-height: 44px;
  margin-bottom: 12px;
  color: #617172;
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.service-listfront .service-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 13px;
  color: #617172;
  font-size: 13px;
}

.service-listfront .service-stats span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #f0f7f6;
}

.service-listfront .service-book-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.service-listfront .item .item-inner .service-info .price {
  width: auto;
  margin: 0;
  color: #d46b4e;
  font-size: 23px;
  font-weight: 900;
}

.service-listfront .service-book-row button {
  min-height: 38px;
  padding: 8px 13px;
  border: 0;
  border-radius: 8px;
  background: #1f7a75;
  color: #fff;
  font-weight: 900;
  cursor: pointer;
}

.boarding-listfront {
  gap: 18px;
}

.boarding-listfront .item {
  width: calc(33.333% - 12px);
  border: 1px solid #eadfce;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(70, 48, 25, 0.07);
}

.boarding-listfront .item:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(70, 48, 25, 0.13);
}

.boarding-listfront .item .item-inner .img-box {
  aspect-ratio: 4 / 3;
  max-height: none;
  border-radius: 8px 8px 0 0;
}

.boarding-listfront .item .img-box .cover,
.boarding-listfront .item .item-inner .img-box .cover {
  height: 100%;
  border-radius: 8px 8px 0 0;
}

.boarding-listfront .item .item-inner .boarding-info {
  padding: 16px;
  text-indent: 0;
  white-space: normal;
  overflow: visible;
  line-height: 1.5;
}

.boarding-listfront .boarding-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #776a5d;
  font-size: 13px;
}

.boarding-listfront .item .item-inner .boarding-info .goodtitle {
  min-height: 52px;
  margin: 10px 0 8px;
  color: #2b2319;
  font-size: 19px;
  line-height: 1.35;
}

.boarding-listfront .boarding-desc {
  min-height: 44px;
  margin-bottom: 10px;
  color: #776a5d;
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.boarding-listfront .boarding-items {
  min-height: 38px;
  margin-bottom: 12px;
  padding: 9px 10px;
  border-radius: 8px;
  background: #fbf6ed;
  color: #5d4b35;
  font-size: 13px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.boarding-listfront .boarding-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 13px;
  color: #776a5d;
  font-size: 13px;
}

.boarding-listfront .boarding-stats span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #f3eadc;
}

.boarding-listfront .boarding-book-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.boarding-listfront .item .item-inner .boarding-info .price {
  width: auto;
  margin: 0;
  color: #bd643f;
  font-size: 23px;
  font-weight: 900;
}

.boarding-listfront .boarding-book-row button {
  min-height: 38px;
  padding: 8px 13px;
  border: 0;
  border-radius: 8px;
  background: #7a5833;
  color: #fff;
  font-weight: 900;
  cursor: pointer;
}

.pet-sale-listfront {
  gap: 18px;
}

.pet-sale-listfront .item {
  width: calc(33.333% - 12px);
  border: 1px solid #dde3f0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(31, 38, 58, 0.07);
}

.pet-sale-listfront .item:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(31, 38, 58, 0.13);
}

.pet-sale-listfront .item .item-inner .img-box {
  aspect-ratio: 4 / 3;
  max-height: none;
  border-radius: 8px 8px 0 0;
}

.pet-sale-listfront .item .img-box .cover,
.pet-sale-listfront .item .item-inner .img-box .cover {
  height: 100%;
  border-radius: 8px 8px 0 0;
}

.pet-sale-listfront .item .item-inner .pet-sale-info {
  padding: 16px;
  text-indent: 0;
  white-space: normal;
  overflow: visible;
  line-height: 1.5;
}

.pet-sale-listfront .pet-sale-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #667086;
  font-size: 13px;
}

.pet-sale-listfront .pet-sale-status {
  padding: 2px 7px;
  border-radius: 6px;
  background: #eef3ff;
  color: #3459a3;
  font-weight: 800;
}

.pet-sale-listfront .item .item-inner .pet-sale-info .goodtitle {
  min-height: 52px;
  margin: 10px 0 8px;
  color: #1f263a;
  font-size: 19px;
  line-height: 1.35;
}

.pet-sale-listfront .pet-sale-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
  color: #4f5d76;
  font-size: 13px;
}

.pet-sale-listfront .pet-sale-tags span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #f2f5fb;
}

.pet-sale-listfront .pet-sale-desc {
  min-height: 32px;
  margin-bottom: 10px;
  color: #667086;
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.pet-sale-listfront .pet-sale-health {
  min-height: 42px;
  margin-bottom: 12px;
  padding: 9px 10px;
  border-radius: 8px;
  background: #f7f9fd;
  color: #4f5d76;
  font-size: 13px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.pet-sale-listfront .pet-sale-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 13px;
  color: #667086;
  font-size: 13px;
}

.pet-sale-listfront .pet-sale-stats span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #eef3ff;
}

.pet-sale-listfront .pet-sale-buy-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.pet-sale-listfront .item .item-inner .pet-sale-info .price {
  width: auto;
  margin: 0;
  color: #d35a45;
  font-size: 23px;
  font-weight: 900;
}

.pet-sale-listfront .pet-sale-buy-row button {
  min-height: 38px;
  padding: 8px 13px;
  border: 0;
  border-radius: 8px;
  background: #385aa8;
  color: #fff;
  font-weight: 900;
  cursor: pointer;
}

.adoption-listfront {
  gap: 18px;
}

.adoption-listfront .item {
  width: calc(33.333% - 12px);
  border: 1px solid #dce8df;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(30, 45, 38, 0.07);
}

.adoption-listfront .item:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(30, 45, 38, 0.13);
}

.adoption-listfront .item .item-inner .img-box {
  aspect-ratio: 4 / 3;
  max-height: none;
  border-radius: 8px 8px 0 0;
}

.adoption-listfront .item .img-box .cover,
.adoption-listfront .item .item-inner .img-box .cover {
  height: 100%;
  border-radius: 8px 8px 0 0;
}

.adoption-listfront .item .item-inner .adoption-info {
  padding: 16px;
  text-indent: 0;
  white-space: normal;
  overflow: visible;
  line-height: 1.5;
}

.adoption-listfront .adoption-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #647267;
  font-size: 13px;
}

.adoption-listfront .adoption-status {
  padding: 2px 7px;
  border-radius: 6px;
  background: #eef7f1;
  color: #2f7b52;
  font-weight: 800;
}

.adoption-listfront .item .item-inner .adoption-info .goodtitle {
  min-height: 52px;
  margin: 10px 0 8px;
  color: #1e2d26;
  font-size: 19px;
  line-height: 1.35;
}

.adoption-listfront .adoption-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 10px;
  color: #536257;
  font-size: 13px;
}

.adoption-listfront .adoption-tags span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #f0f6f2;
}

.adoption-listfront .adoption-desc {
  min-height: 42px;
  margin-bottom: 10px;
  color: #647267;
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.adoption-listfront .adoption-health {
  min-height: 38px;
  margin-bottom: 12px;
  padding: 9px 10px;
  border-radius: 8px;
  background: #f8fbf8;
  color: #536257;
  font-size: 13px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.adoption-listfront .adoption-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 13px;
  color: #647267;
  font-size: 13px;
}

.adoption-listfront .adoption-stats span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #eef7f1;
}

.adoption-listfront .adoption-action-row {
  display: flex;
}

.adoption-listfront .adoption-action-row button {
  width: 100%;
  min-height: 40px;
  padding: 8px 13px;
  border: 0;
  border-radius: 8px;
  background: #2f7b52;
  color: #fff;
  font-weight: 900;
  cursor: pointer;
}

.gift-listfront {
  gap: 18px;
}

.gift-listfront .item {
  width: calc(33.333% - 12px);
  border: 1px solid #e5dded;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(55, 38, 72, 0.07);
}

.gift-listfront .item:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 34px rgba(55, 38, 72, 0.13);
}

.gift-listfront .item .item-inner .img-box {
  aspect-ratio: 4 / 3;
  max-height: none;
  border-radius: 8px 8px 0 0;
}

.gift-listfront .item .img-box .cover,
.gift-listfront .item .item-inner .img-box .cover {
  height: 100%;
  border-radius: 8px 8px 0 0;
}

.gift-listfront .item .item-inner .gift-info {
  padding: 16px;
  text-indent: 0;
  white-space: normal;
  overflow: visible;
  line-height: 1.5;
}

.gift-listfront .gift-meta {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  color: #74657e;
  font-size: 13px;
}

.gift-listfront .item .item-inner .gift-info .goodtitle {
  min-height: 52px;
  margin: 10px 0 8px;
  color: #372648;
  font-size: 19px;
  line-height: 1.35;
}

.gift-listfront .gift-desc {
  min-height: 44px;
  margin-bottom: 12px;
  color: #74657e;
  font-size: 14px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.gift-listfront .gift-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 13px;
  color: #74657e;
  font-size: 13px;
}

.gift-listfront .gift-stats span {
  padding: 4px 8px;
  border-radius: 6px;
  background: #f7f1fb;
}

.gift-listfront .gift-exchange-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.gift-listfront .points {
  color: #c15c32;
  font-size: 23px;
  font-weight: 900;
}

.gift-listfront .gift-exchange-row button {
  min-height: 38px;
  padding: 8px 13px;
  border: 0;
  border-radius: 8px;
  background: #714596;
  color: #fff;
  font-weight: 900;
  cursor: pointer;
}

@media (max-width: 980px) {
  .goods-listfront .item,
  .service-listfront .item,
  .boarding-listfront .item,
  .pet-sale-listfront .item,
  .adoption-listfront .item,
  .gift-listfront .item {
    width: calc(50% - 9px);
  }
}

@media (max-width: 620px) {
  .goods-listfront .item,
  .service-listfront .item,
  .boarding-listfront .item,
  .pet-sale-listfront .item,
  .adoption-listfront .item,
  .gift-listfront .item {
    width: 100%;
  }

  .goods-listfront .goods-buy-row,
  .service-listfront .service-book-row,
  .boarding-listfront .boarding-book-row,
  .pet-sale-listfront .pet-sale-buy-row,
  .gift-listfront .gift-exchange-row {
    align-items: flex-start;
    flex-direction: column;
  }

  .goods-listfront .goods-buy-row button,
  .service-listfront .service-book-row button,
  .boarding-listfront .boarding-book-row button,
  .pet-sale-listfront .pet-sale-buy-row button,
  .gift-listfront .gift-exchange-row button {
    width: 100%;
  }
}
</style>
