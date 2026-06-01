<script setup>
/**
 * @description 标题 公共的
 * 很多子页面都会用这个标题组件: 
 * title 标题
 */
let { title } = defineProps(['title'])
</script>

<template>
  <div class="bt2">
    <div class="title">{{ title }}<i></i></div>
</div>
</template>

<style>
/* 通用标题 */
.bt2 {
  width: 100%;
  height: auto;
  padding: 0px 10%;
  position:relative;
  text-align:center;
  margin:20px auto;
}
.bt2 .title {
  display:inline-block;
  width:auto;
  text-align:center;
  font-size: 32px;
  color: #333;
  font-weight: 600;
  padding:0px 20px;
}
.bt2 i {
  display: none;
  width: 400px;
  height: 48px;
  background: url() no-repeat center center;
  margin:0px auto;
}
</style>