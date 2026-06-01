<script setup>
import { inject } from 'vue'
import dayjs from 'dayjs'

let { data } = defineProps(['data'])
let { detailEvent } = inject('start')

function cleanIntro(item) {
  return item.introduction || item.sourceData?.content?.replace(/<[^>]*>/g, '') || '进入详情查看完整讨论内容。'
}

function forumStatus(item) {
  return item.sourceData?.isdone || '开放'
}

function isTop(item) {
  return Number(item.sourceData?.istop) === 1
}
</script>

<template>
  <div class="forumlist-default">
    <div class="item" v-for="item in data.list" :key="item.id" @click="detailEvent(data.tableName, item.id)">
      <div class="img-box" v-if="item.img"><img :src="item.img" draggable="false" /></div>
      <div class="info-box">
        <div class="forum-labels">
          <span v-if="isTop(item)" class="top">置顶</span>
          <span>{{ forumStatus(item) }}</span>
        </div>
        <div v-for="title in item.titles" class="text">{{ title }}</div>
        <div class="introduction">{{ cleanIntro(item) }}</div>
        <div class="forum-meta">
          <span v-if="item.user !== undefined">发布人 {{ item.user }}</span>
          <span>{{ dayjs(item.addtime).format('YYYY-MM-DD') }}</span>
          <span v-if="item.storeupnum !== undefined">收藏 {{ item.storeupnum }}</span>
          <span v-if="item.clicknum !== undefined">浏览 {{ item.clicknum }}</span>
        </div>
        <button type="button" class="join-discuss">进入讨论</button>
      </div>
    </div>
  </div>
</template>

<style>
.forumlist-default {
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
    border: 1px solid #dfe8df;
    border-radius: 8px;
    position: relative;
    cursor: pointer;
    transition: box-shadow 0.3s linear, transform 0.3s linear;
    display: flex;
    gap: 18px;
    background: #fff;
    box-shadow: 0 10px 28px rgba(35, 43, 37, 0.06);

    &:hover {
      box-shadow: 0 16px 34px rgba(35, 43, 37, 0.12);
      transform: translateY(-3px);
    }
  }

  .img-box {
    flex: none;
    width: 190px;
    overflow: hidden;
    border-radius: 8px;

    img {
      width: 100%;
      height: 132px;
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

    .forum-labels {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .forum-labels span {
      padding: 4px 8px;
      border-radius: 6px;
      background: #eef6ef;
      color: #2f6f4e;
      font-size: 13px;
      font-weight: 800;
    }

    .forum-labels .top {
      background: #fff3e9;
      color: #c15c32;
    }

    .text {
      color: #232b25;
      font-size: 21px;
      line-height: 1.35;
      font-weight: 800;
      margin: 10px 0 8px;
    }

    .introduction {
      color: #657064;
      font-size: 15px;
      line-height: 1.7;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 14px;
    }

    .forum-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      color: #657064;
      font-size: 13px;
      margin-bottom: 14px;
    }

    .forum-meta span {
      padding: 4px 8px;
      border-radius: 6px;
      background: #f4f8f4;
    }

    .join-discuss {
      margin-top: auto;
      min-height: 38px;
      padding: 8px 14px;
      border: 0;
      border-radius: 8px;
      background: #2f6f4e;
      color: #fff;
      font-weight: 900;
      cursor: pointer;
    }
  }
}

@media (max-width: 720px) {
  .forumlist-default {
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

    .info-box .join-discuss {
      width: 100%;
    }
  }
}
</style>
