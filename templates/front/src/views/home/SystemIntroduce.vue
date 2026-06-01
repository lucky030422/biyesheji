<script setup>
/**
 * @description 关于我们
 * title 标题
 * subtitle 副标题
 * picture1 图1
 * picture2 图2
 * picture3 图4
 * content 内容
 */
import { inject, onUnmounted, ref } from 'vue'
import { useIntersectionObserver } from '@vueuse/core'
let { data } = defineProps(['data'])
let { aboutUsData } = inject('start')

const boxRef = ref(null)
const animateClass = ref('')
// 元素可见时，增加动画
let { stop: aboutusStop } = useIntersectionObserver(
  boxRef,
  ([{ isIntersecting }]) => {
    if (isIntersecting) {
      // 这里修改 动画，https://animate.style/
      animateClass.value = 'animate__animated animate__fadeInUp'

    }
    //else {
      //animateClass.value = ''
    //}
  },
  // 0.01 目标元素与视口的交叉比例达到 ‌1%‌ 时触发回调函数
  { threshold: 0 }
)
onUnmounted(() => {
  aboutusStop()
})

</script>

<template>
  <div class="introduction-default" ref="boxRef">
  
    <div class="biaoti">
      <div class="subtitle">{{ data.subtitle }}</div>
      <div class="title">{{ data.title }}</div>
      <i></i>
    </div>

    <div class="content">
      <div class="desc">
        <div class="ql-snow ql-editor" v-html="data.content"></div>
      </div>
      <div class="img-box">
        <img class="img1" :src="data.picture1" draggable="false" />
        <img class="img2" :src="data.picture2" draggable="false" />
        <img class="img3" :src="data.picture3" draggable="false" />
      </div>

    </div>
  </div>
</template>

<style>
.introduction-default {
  width: 100%;
  padding-top: 20px;
  padding-bottom: 30px;
  background: url() no-repeat center top / cover;
}

.introduction-default .content {
    width: 100%;
    height: auto;
    padding: 20px 10%;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    position:relative;
}

 .introduction-default .content .img-box {
    width: 50%;
    padding: 0 0 0 20px;
    margin: 0;
    display: flex;
    justify-content: space-between;
    gap: 0px;
    height: 300px;
}
.introduction-default .content .img-box .img1{
      flex: auto;
      width: 0;
      height: 100%;
      padding: 0;
      margin: 0% 0 0;
      object-fit: cover;
  }
.introduction-default .content .img-box .img2{
      flex: auto;
      width: 0;
      height: 100%;
      padding: 0;
      margin: 0;
      object-fit: cover;
  }
.introduction-default .content .img-box .img3{
      flex: auto;
      width: 0;
      height: 100%;
      padding: 0;
      margin: 0 0 0;
      object-fit: cover;
  }

.introduction-default .content .desc {
    width: 50%;
    flex:auto;
    padding: 0px;
    margin: 0;
    border: 0px solid #150572;
    color: #333;
    font-size: inherit;
  }
 .introduction-default .content .desc .ql-editor{
     line-height: 1.8;
     padding:0;
 }
</style>
