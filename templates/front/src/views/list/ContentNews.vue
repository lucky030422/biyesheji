<script setup>
import { inject } from 'vue'
import dayjs from 'dayjs'

let { data } = defineProps(['data'])
let { detailEvent } = inject('start')
</script>

<template>
  <div class="newslist-default">
    <div class="item" v-for="item in data.list" :key="item.id" @click="detailEvent(data.tableName, item.id)">
      <div class="img-box" v-if="item.img"><img :src="item.img" draggable="false" /></div>
      <div class="info-box">
        <div class="news-label">公告信息</div>
        <div v-for="title in item.titles" class="text">{{ title }}</div>
        <div v-if="item.introduction !== undefined" class="introduction">{{ item.introduction }}</div>
        <div class="news-meta">
          <span>{{ dayjs(item.addtime).format('YYYY-MM-DD') }}</span>
          <span v-if="item.user !== undefined">发布人 {{ item.user }}</span>
          <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
          <span v-if="item.clicknum !== undefined">浏览 {{ item.clicknum }}</span>
        </div>
        <button type="button" class="read-more">查看详情</button>
      </div>
    </div>
  </div>
</template>

<style>
.newslist-default {
  width: 100%;
  height: auto;
  margin: 0;
  padding: 20px 0;
  background: transparent;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 16px;

  .item {
    flex: 0 0 auto;
    width: 100%;
    height: auto;
    padding: 16px;
    border: 1px solid #dfe6ef;
    border-radius: 8px;
    position: relative;
    cursor: pointer;
    transition: box-shadow 0.3s linear, transform 0.3s linear;
    display: flex;
    gap: 18px;
    background: #fff;
    box-shadow: 0 10px 28px rgba(24, 35, 52, 0.06);

    &:hover {
      box-shadow: 0 16px 34px rgba(24, 35, 52, 0.12);
      transform: translateY(-3px);
    }
  }

  .img-box {
    flex: none;
    width: 220px;
    overflow: hidden;
    border-radius: 8px;

    img {
      width: 100%;
      height: 150px;
      border-radius: 8px;
      object-fit: cover;
      display: block;
    }
  }

  .info-box {
    width: 100%;
    height: auto;
    margin: 0;
    padding: 0;
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;

    .news-label {
      padding: 4px 8px;
      border-radius: 6px;
      background: #eef4fb;
      color: #315f94;
      font-size: 13px;
      font-weight: 800;
    }

    .text {
      color: #182334;
      font-size: 22px;
      line-height: 1.35;
      font-weight: 800;
      margin: 10px 0 8px;
    }

    .introduction {
      color: #657387;
      font-size: 15px;
      line-height: 1.7;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 14px;
    }

    .news-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      color: #657387;
      font-size: 13px;
      margin-bottom: 14px;
    }

    .news-meta span {
      padding: 4px 8px;
      border-radius: 6px;
      background: #f5f7fa;
    }

    .read-more {
      margin-top: auto;
      min-height: 38px;
      padding: 8px 14px;
      border: 0;
      border-radius: 8px;
      background: #315f94;
      color: #fff;
      font-weight: 900;
      cursor: pointer;
    }
  }
}

@media (max-width: 720px) {
  .newslist-default {
    .item {
      flex-direction: column;
    }

    .img-box {
      width: 100%;
    }

    .img-box img {
      height: 210px;
    }

    .info-box .text {
      font-size: 19px;
    }

    .info-box .read-more {
      width: 100%;
    }
  }
}
</style>
