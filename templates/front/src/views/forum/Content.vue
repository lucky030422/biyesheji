
<script setup>
/**
 * @description 说明
 * 
 * data.title 标题
 * data.user 发布人
 * data.addtime 时间
 * data.thumbsupnum 点赞量,可能没有
 * data.storeupnum 收藏量,可能没有
 * data.content 内容
 */
import { inject } from 'vue'
let { data, hasThumbsUp, hasStoreUp } = inject('detail')
</script>
<template>
  <div class="article-wrapper">
    <div class="article-title">{{ data.title }}</div>
    <div class="sub-box">
      <span>
        <el-icon><UserFilled /></el-icon>
        {{ data.user }}
      </span>
      <span>
        <el-icon><Timer /></el-icon>
        {{ data.addtime }}
      </span>
      <span v-if="hasThumbsUp">
        <el-icon>
          <svg t="1761288918326" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1572" width="256" height="256">
            <path
              d="M512 360.301714l-78.823619-78.823619a160.060952 160.060952 0 1 0-226.377143 226.377143L512 813.031619 817.176381 507.855238a160.060952 160.060952 0 1 0-226.377143-226.377143L512 360.301714z m0 535.698286L165.302857 549.327238A218.721524 218.721524 0 1 1 474.672762 240.006095l37.302857 37.327238 37.351619-37.327238 0.024381-0.024381A218.721524 218.721524 0 0 1 858.648381 549.302857L512 896z"
              p-id="1573"
            ></path>
          </svg>
        </el-icon>
        {{ data.thumbsupnum }}
      </span>
      <span v-if="hasStoreUp">
        <el-icon><StarFilled /></el-icon>
        {{ data.storeupnum }}
      </span>
    </div>
    <div class="ql-snow ql-editor" v-html="data.content"></div>
  </div>
</template>
  