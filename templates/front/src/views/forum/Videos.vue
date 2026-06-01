
<script setup>
/**
 * @description 视频
 *
 * videoList 视频路径列表
 */
import { inject } from 'vue'

let { videoList } = inject('detail')
</script>

<template>
  <div class="videos-view-forum" v-if="videoList.length">
    <video
      v-for="src in videoList"
      :key="src"
      :src="src"
      :autoPlay="false"
      controls="controls"
    ></video>
  </div>
</template>
<style>
.videos-view-forum {
  width: 100%;
  margin-bottom: 20px;
  video {
    height: 400px;
    width: 100%;
  }
}
</style>

  