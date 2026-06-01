
<script setup>
/**
 * @description 选项卡
 *
 * tabs 数据列表
 * item.label 名称
 * item.name 组件名称 有值: 点击后当前页面显示的 为空: 要跳转到其它页面的
 * item.tableName 表名
 *
 * tabEvent tab点击事件
 */
import { inject } from 'vue'

let { tabs, tabEvent, centerTabActiveName } = inject('center')
</script>

<template>
  <div class="centertab">
    <div class="biaoti2">
       <div class="title">我的功能<i></i></div>
    </div>
    <el-tabs v-model="centerTabActiveName" type="border-card" @tab-click="tabEvent">
      <el-tab-pane
        v-for="(item, index) in tabs"
        :label="item.label"
        :name="index"
        :key="item.label"
      >
        <component v-if="item.name && centerTabActiveName === index" :is="item.name" />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<style>
.centertab {
  width:100%;
  --el-color-primary: #2f6f4e;
  padding: 30px 34px 34px;
  border: 1px solid #e5ece2;
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 0 18px 42px rgba(56, 83, 61, .10);
}
.centertab .el-tabs__item{
  height: 52px;
  padding: 0 28px;
  font-size:16px;
  font-weight: 800;
}
.centertab .el-tabs {
    --el-tabs-header-height: 50px;
    border: 0;
    box-shadow: none;
    background: transparent;
}
.centertab .el-tabs__header {
    border: 0;
    background: transparent;
}
.centertab .el-tabs__nav {
    display: flex;
    gap: 12px;
    border: 0 !important;
}
.centertab .el-tabs__item {
    border: 1px solid #dfebdf !important;
    border-radius: 8px;
    background: #f5f8f3;
    color: #547161;
}
.centertab .el-tabs__item.is-active {
    background: #2f6f4e;
    border-color: #2f6f4e !important;
    color: #fff;
}
.centertab .el-tabs__content {
    padding: 28px 0 0;
}

.centertab .biaoti2{
    margin:0 0 20px;
}
.centertab .biaoti2 .title {
    font-size: 22px;
    color: #243b2a;
    font-weight: 900;
}
</style>  
  
