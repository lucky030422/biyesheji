
<script setup>
/**
 * @description 按钮
 *
 * payButtons 购物按钮列表
 * hasBuyInput 是否有数量输入框
 * buynumber 数量
 * payLoading 购物按钮加载中
 * shopEvent 购物按钮事件
 *
 * actionButtons 操作按钮列表
 * actionEvent 操作按钮事件
 */
import { inject } from 'vue'

let { payButtons, payLoading, hasBuyInput, buynumber, shopEvent, actionButtons, actionEvent } =
  inject('detail')
</script>
<template>
  <div class="detailbutton-wrapper">
    <!-- 购物按钮 -->
    <div class="btn-list" v-loading="payLoading">
      <el-input-number v-if="hasBuyInput" v-model="buynumber" :min="1" :step="1" :precision="0" />
      <el-button
        v-for="item in payButtons"
        :key="item.key"
        :data-key="item.key"
        :icon="item.iconName"
        @click="shopEvent(item.key)"
      >
        {{ item.title }}
      </el-button>
    </div>

    <!-- 操作按钮 -->
    <div class="btn-list" v-if="actionButtons.length">
      <el-button
        v-for="item in actionButtons"
        :key="item.key"
        :data-key="item.key"
        :icon="item.iconName"
        @click="actionEvent(item)"
      >
        {{ item.title }}
      </el-button>
    </div>
  </div>
</template>
<style>
.detailbutton-wrapper {
  margin-top: 18px;
  padding-top: 18px;
  border-top: 1px solid #edf1eb;

  .btn-list {
    display: flex;
    flex-wrap: wrap;
    padding-top: 10px;
    gap: 8px;
  }
  .el-button + .el-button {
    margin-left: 0;
    font-size:inherit;
  }
.el-button {
    min-height: 42px;
    padding: 0 18px;
    border-radius: 8px;
    font-size:inherit;
    font-weight: 700;
  }

  /* 添加到购物车 */
.el-button[data-key="cartBtn"]{
    border:0;
    background:var(--btn-bg-color-);
    color:#fff;
  }
.el-button[data-key="cartBtn"]:hover{
    background:var(--btn-bg-hover-color-);
  }
  /* 立即购买 */
.el-button[data-key="buyBtn"]{
    border:0;
    background:#51a2ee;
    color:#fff;
  }
.el-button[data-key="buyBtn"]:hover{
    background:#3480c6;
  }
  /* 积分兑换 */
.el-button[data-key="jfBtn"]{
    border:0;
    background:#4dd9ce;
    color:#fff;
  }
.el-button[data-key="jfBtn"]:hover{
    background:#2fb4aa;
  }
  /* 修改 */
.el-button[data-key="edit"]{
    border:0;
    background:#4fd69b;
    color:#fff;
  }
.el-button[data-key="edit"]:hover{
    background:#2fb47a;
  }
  /* 删除*/
.el-button[data-key="remove"]{
    border:0;
    background:#d64f50;
    color:#fff;
  }
.el-button[data-key="remove"]:hover{
    background:#b43839;
  }
  /* 私聊 */
.el-button[data-key="chat"]{
    border:0;
    background:#7164da;
    color:#fff;
  }
.el-button[data-key="chat"]:hover{
    background:#4c3eb2;
  }
  /* 跨表 */
.el-button[data-key="crossTable_0"]{
    border:0;
    background:#2f6f4e;
    color:#fff;
    box-shadow: 0 8px 18px rgba(47, 111, 78, .20);
  }
.el-button[data-key="crossTable_0"]:hover{
    background:#255d40;
  }
.el-button[data-key="crossTable_1"]{
    border:0;
    background:#dd9d36;
    color:#fff;
  }
.el-button[data-key="crossTable_1"]:hover{
    background:#b88128;
  }
  /* 审核 */
.el-button[data-key="sfsh"]{
    border:0;
    background:#f78138;
    color:#fff;
  }
.el-button[data-key="sfsh"]:hover{
    background:#d6621a;
  }
}
</style>
  
