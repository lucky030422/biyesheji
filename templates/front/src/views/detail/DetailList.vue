<script setup>
/**
 * @description 商品属性
 */
import { inject } from 'vue'

let { detailColumns, data } = inject('detail')
</script>
<template>
  <div class="detail-list">
    <div class="item" v-for="column in detailColumns" :key="column.columnName">
      <component
        :key="column.columnName"
        :is="column.detail_type"
        :column="column"
        :data="data"
        :value="data[column.columnName]"
        :label="column.comments"
      />
    </div>
  </div>
</template>

<style>
.detail-list {
  margin-top: 0;
  background: #fff;
  display: flex;
  flex-direction: column;
  gap: 0;
  padding: 0;
  border-radius: 8px;
  overflow: hidden;
}
.detail-list .item {
  border-bottom: 1px solid #edf1eb;
  padding: 14px 4px;
}
.detail-list .item:last-child {
  border-bottom: 0;
}
.detail-list .item .label {
  min-width: 96px;
  color: #81907e;
  margin-right: 20px;
  font-size: inherit;
  flex: none;
}
.detail-list .item .detail-title {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 18px;
  padding-bottom: 6px;
}
.detail-list .item .detail-title .title {
  color: #183122;
  font-size: 26px;
  line-height: 1.25;
  font-weight: 800;
}
.detail-list .item .detail-text,
.detail-list .item .detail-price {
  display: flex;
  align-items: flex-start;
  line-height: 1.75;
}
.detail-list .item .detail-text .text {
  min-width: 0;
  color: #2f3d33;
  overflow-wrap: anywhere;
}
.detail-list .item .detail-price .price {
  color: #d85f32;
  font-weight: 800;
  font-size: 22px;
  line-height: 1.35;
}
.detail-list .item .detail-title .storeup {
  flex: none;
  padding: 7px 11px;
  border-radius: 999px;
  background: #edf5ea;
  color: #55764f;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
}
.detail-list .item .detail-reversetime {
  display: flex;
}
.detail-list .item .detail-text a{
  font-size: inherit;
}
.detail-list .item .detail-text .el-tag{
  height:auto;
  padding:5px 10px;
  font-size: inherit;
}
@media (max-width: 560px) {
  .detail-list .item .detail-text,
  .detail-list .item .detail-price {
    display: block;
  }

  .detail-list .item .label {
    display: block;
    margin: 0 0 4px;
  }
}
</style>
