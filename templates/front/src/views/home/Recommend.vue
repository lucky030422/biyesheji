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
import { inject, onUnmounted, ref } from 'vue'
import { useIntersectionObserver } from '@vueuse/core'
import dayjs from 'dayjs'

let { data, hideHeader } = defineProps(['data', 'hideHeader'])
let { detailEvent, moreEvent } = inject('start')

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
  <div class="goods-6" ref="boxRef">
    <div class="biaoti">
      <div class="subtitle">{{ data.subtitle }}</div>
      <div class="title">{{ data.comments }}</div>
      <i></i>
      <el-button class="more" color="#848C74" @click="moreEvent(data.tableName)">更多>></el-button>
    </div>

    <div class="content">
      <div
        class="item"
        v-for="item in data.list"
        :key="item.id"
        @click="detailEvent(data.tableName, item.id)"
      >
        <div class="img-box" v-if="item.img || data.hasMusic">
          <img
            v-if="data.hasMusic"
            class="music"
            src="http://codegen.caihongy.cn/20251230/096adf8336ff4c9397450b81c24cc10f.png"
            @click.stop="data.musicEvent(item)"
          />
          <img class="cover" v-if="item.img" :src="item.img" draggable="false" />
        </div>
        <div class="info-box">
          <div class="text" v-for="title in item.titles">{{ title }}</div>
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
      </div>
    </div>
  </div>
</template>

<style>
.goods-6 {
  width: 100%;
  margin: 0 auto 40px;
  padding: 20px 0 20px;
  background: url() fixed no-repeat center top / cover;
  position: relative;
  color: #999;
}

.goods-6 .biaoti .more {
  position: absolute;
  right: 10%;
  top: 25px;
  background: none;
  color: #666;
  border: 0;
}

.goods-6 .content {
  width: 100%;
  height: auto;
  padding: 20px 10%;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 30px;
}
.goods-6 .content .item {
  width: 100%;
  height: auto;
  background: #fff;
  padding: 0px;
  border: 0px solid #eee;
  cursor: pointer;
  position: relative;
  border-radius: 6px;
}
.goods-6 .content .item .img-box {
  width: 100%;
  height: 320px;
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
.goods-6 .content .item .img-box .cover {
  width: 100%;
  height: 320px;
  object-fit: cover;
  transition: transform 0.3s linear;
}
.goods-6 .content .item:hover .img-box .cover {
  transform: scale(1.05);
}
.goods-6 .content .item .info-box {
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

.goods-6 .content .item .info-box .text {
  width: 100%;
  font-size: 16px;
  color: #333;
  font-weight: 500;
  margin-bottom: 6px;
}
.goods-6 .content .item:hover .info-box .text {
}
.goods-6 .content .item .info-box .price {
  width: 100%;
  font-size: 16px;
  color: #e72c59;
  font-weight: 600;
  margin-bottom: 6px;
}
.goods-6 .content .item .info-box .user {
  width: 100%;
  margin: 0 0 6px;
}
.goods-6 .content .item .info-box .time {
  width: 100%;
  margin: 0 0 6px;
}
.goods-6 .content .item .info-box .other {
  margin: 0 6px 6px 0;
  display: inline-block;
}
</style>
