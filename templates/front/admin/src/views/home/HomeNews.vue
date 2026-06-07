
<script setup>
import { inject, ref } from 'vue'

/**
 * @description 新闻资讯
 * newsData 新闻数据
 * newsData.tilte 新闻资讯 别名
 * newsData.list 新闻列表
 * item.addtime 发布时间
 * item.title 标题
 * item.introduction 简介
 * item.content 内容
 */

let { newsData } = inject('home')

const dialogVisible = ref(false)
const actData = ref({})
function showContent(item) {
  actData.value = item
  dialogVisible.value = true
}
</script>
<template>
  <div class="home-news">
    <div class="news-header">
      <div>
        <p>公告中心</p>
        <h2>{{ newsData.title }}</h2>
      </div>
      <span>{{ newsData.list.length }} 条</span>
    </div>
    <div class="list">
      <div v-for="(item, index) in newsData.list" :key="item.id" class="item" @click="showContent(item)">
        <span class="index">{{ String(index + 1).padStart(2, '0') }}</span>
        <span class="label">{{ item.title }}</span>
      </div>
      <el-empty v-if="!newsData.list.length" description="暂无公告" />
    </div>

    <el-dialog v-model="dialogVisible" :title="actData.title" width="80%">
      <div class="introduction">{{ actData.introduction }}</div>
      <div class="ql-snow ql-editor" v-html="actData.content"></div>
    </el-dialog>
  </div>
</template>
  
