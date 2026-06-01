
<script setup>
/**
 * @description 标题logo
 *
 * projectName 项目名
 * $projectImages.logo logo图片
 */
</script>
<template>
  <div class="register-title">
    <div class="logo" v-if="$projectImages.logo">
      <img :src="$projectImages.logo" draggable="false" />
    </div>

    <div class="title">{{ projectName }}</div>
  </div>
</template>

<style>
.register-title {
  padding: 0;
  margin: 0 0 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  .logo {
    width: 90px;
    height: 68px;
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  .title {
    color: #333;
    font-size: 22px;
    font-weight: 700;
    line-height: 1.5;
    padding: 0 20px 0 50px;
    text-align: center;
  }
}
</style>

  
