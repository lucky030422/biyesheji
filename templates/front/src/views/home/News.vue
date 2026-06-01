<script setup>
/**
 * @description 新闻
 *
 * data.title 标题
 * data.subtitle 副标题
 * data.tableName 表名
 * data.list 列表数据
 *
 * item.titles 标题列表,可能多个标题
 * item.img 图片
 * item.user 发布人,可能没有 undefined判断
 * item.addtime 发布时间
 * item.thumbsupnum 点赞,可能没有 undefined判断
 * item.storeupnum 收藏,可能没有 undefined判断
 * item.clicknum 查看量,可能没有 undefined判断
 * item.browseduration 浏览时长,可能没有 undefined判断
 *
 * item.introduction 简介
 *
 * detailEvent 点击详情事件
 * moreEvent 更多事件
 */
import { inject, ref } from 'vue'
import dayjs from 'dayjs'

let { data } = defineProps(['data'])
let { detailEvent, moreEvent } = inject('start')

const actId = ref(null)
function textEvent(item) {
  actId.value = item.id
}
</script>

<template>
  <div class="news-default">
    <div class="inner">

    <div class="biaoti">
      <div class="subtitle">{{ data.subtitle }}</div>
      <div class="title">{{ data.comments }}</div>
      <i></i>
      <el-button class="more" color="#848C74" @click="moreEvent(data.tableName)">更多>></el-button>
    </div>

      <div class="content">
        <div class="item" v-for="item in data.list" :key="item.id" @click="detailEvent(data.tableName, item.id)">
          <div class="img-box">
            <img :src="item.img" draggable="false" />
          </div>
          <div class="info-box">
            <div v-for="title in item.titles" class="text">{{ title }}</div>

            <div class="introduction">{{ item.introduction }}</div>
            <div class="bottom-box">
              <span class="bottom-item" v-if="item.clicknum !== undefined">
                <el-icon><View /></el-icon>
                {{ item.clicknum }}
              </span>
              <span class="bottom-item">
                <el-icon><Clock /></el-icon>
                {{ dayjs(item.addtime).format('YYYY-MM-DD') }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.news-default {
  width: 100%;
  position:relative;
  padding-top: 20px;
  padding-bottom: 40px;
  background: url() no-repeat top center;

.biaoti .more{
  position:absolute;
  right:10%;
  top:25px;
  background:none;
  color:#666;
  border:0;
}

  .content {
    width: 100%;
    margin: 0 auto;
    padding: 20px 10%;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 30px;

    .item {
      width: 100%;
      height: auto;
      position: relative;
      cursor: pointer;
      overflow: hidden;
      border-radius: 8px;
      background-color: #fff;
      transition: transform 0.3s linear;

      &:hover {
        transform: translateY(-5px);
        .img-box img {
          transform: scale(1.08) rotate(0deg);
        }
        .info-box .text {
          color: var(--btn-bg-color-);
        }
      }
    }

    .img-box {
      width: 100%;
      overflow: hidden;
      img {
        width: 100%;
        height: 165px;
        object-fit: cover;
        transition: transform 0.3s ease-out;
      }
    }

    .info-box {
      width:100%;
      padding: 12px;

      .text {
        font-size: 16px;
        color: #383b53;
        line-height: 25px;
        font-weight: 600;
      }
      .introduction {
        font-size: 15px;
        line-height: 2em;
        -webkit-line-clamp: 3;
        color: #555;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }

    .bottom-box {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12px;
      color: #bbb;
      line-height: 1.5em;
    }
    .bottom-item {
      display: flex;
      align-items: center;
      gap: 4px;
    }
  }
}
</style>

