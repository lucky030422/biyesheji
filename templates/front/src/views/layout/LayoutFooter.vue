
<script setup>
import { inject } from 'vue'

/**
 * @description 底部
 * 
 * footerContent 底部html内容
 *
 */
let { footerContent } = inject('header')
</script>
<template>
  <div class="layout-footer">
    <div class="ql-snow ql-editor" v-html="footerContent"></div>
  </div>
</template>
<style>
.layout-footer {
  width:100%;
  margin:0 auto;
  background: #363636;
  color: #fff;
}
</style>  
  