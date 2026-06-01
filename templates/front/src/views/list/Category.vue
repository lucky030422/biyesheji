
<script setup>
/**
 * @description 分类
 * @param { Array } list_category 列表
 * @param { String } act_category 激活
 * @param { Function } categoryEvent 点击事件
 */
import { inject } from 'vue'
let { list_category, act_category, categoryEvent } = inject('listFront')
</script>

<template>
  <div class="category-view">
    <div class="item" :class="{ act: act_category == '' }" @click="categoryEvent('')">全部</div>
    <div
      v-for="item in list_category"
      :key="item"
      class="item"
      :class="{ act: act_category === item }"
      @click="categoryEvent(item)"
    >
      {{ item }}
    </div>
  </div>
</template>

<style>
.category-view {
  width:100%;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding: 10px;
  margin:0 0 20px;
  background:#fff;
  border:1px solid #ddd;

  .item {
    width:100%;
    cursor: pointer;
    border-radius: 0px;
    padding: 10px 10px;
    border-bottom:1px solid #eee;

    &:hover {
      color: #fff;
      background-color: var(--btn-bg-color-);
    }
  }
  .act {
    color: #fff;
    background-color: var(--btn-bg-color-);
  }
}
</style>

  