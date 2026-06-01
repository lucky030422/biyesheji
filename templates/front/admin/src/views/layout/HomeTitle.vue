<script setup>
/**
 * @description 头部标题logo
 *
 * projectName 项目名
 * $projectImages.logo logo图片
 */
</script>
<template>
  <div class="header-title">
    <div class="logo" v-if="$projectImages.logo">
      <img  :src="$projectImages.logo" draggable="false" />
    </div>

    <div class="title">{{ projectName }}</div>
  </div>
</template>
<style>
/* 标题 */
.header-title {
  color: #E5416A;
  font-size: 24px;
  font-weight: 400;
  width: auto;
  display: flex;
  align-items: center;
  .logo {
    img {
      width: 30px;
      height: 30px;
      object-fit: contain;
    }
  }
}
</style>
