<script setup>
/**
 * @description 总数统计
 * @param { Array } roleCountList 列表数据
 * @param { object } item 数据
 * @param { string } item.comments 表名
 * @param { number } item.count 数量
 */
import { inject } from 'vue'
const { roleCountList } = inject('home')
const statIcons = ['DocumentChecked', 'House', 'ShoppingBag', 'Goods']
</script>
<template>
  <div class="statis-wrapper" v-if="roleCountList.length">
    <div v-for="(item, index) in roleCountList" :key="item.comments" class="statis-box-common" :class="'statis-box' + (index + 1)">
      <!-- 图标 -->
      <div class="icon-box" :class="'icon-box' + (index + 1)">
        <el-icon>
          <component :is="statIcons[index] || 'DataAnalysis'" />
        </el-icon>
      </div>

      <!-- 文字 -->
      <div class="info-box">
        <div class="label">
          {{ item.comments }}
          <span>总数</span>
        </div>
        <div class="count">{{ item.count }}</div>
      </div>
    </div>
  </div>
</template>
<style>

.statis-box2{
}
.statis-box3{
}
.statis-box4{
}

</style>

