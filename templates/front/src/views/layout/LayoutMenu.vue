<script setup>
import { ref, watch, inject } from 'vue'
import { useRoute } from 'vue-router'
/**
 * @description 菜单 (角色菜单也可以加到这里)
 *
 * menus 菜单列表
 * item.label 菜单名称
 * item.url 菜单地址 用于页面高亮和路由跳转
 * item.children 二级菜单
 *
 * clickEvent 菜单点击事件
 *
 * 角色菜单:
 * isLogin  是否已登录
 * roleMenus  角色菜单列表
 * roleMenuEvent  角色菜单点击事件
 *
 */

let { menus, clickEvent, isLogin, roleMenus, roleMenuEvent } = inject('header')

// 激活的菜单项,默认首页
const route = useRoute()
const defaultActive = ref('/home')
watch(
  () => route.path,
  newPath => {
    defaultActive.value = newPath
  },
  { immediate: true }
)
</script>

<template>
  <div class="menu-wrapper">
    <el-scrollbar>
      <el-menu :default-active="defaultActive" mode="horizontal" popper-class="menu-poper" :ellipsis="false">
        <template v-for="item in menus">
          <!-- 含有二级菜单 -->
          <el-sub-menu v-if="item.children" :index="item.url" @click="clickEvent(item)">
            <template #title>{{ item.label }}</template>
            <el-menu-item :key="item.url" :index="item.url" @click="clickEvent(item)">全部</el-menu-item>
            <el-menu-item v-for="i in item.children" :key="i.url" :index="i.url" @click="clickEvent(i)">
              {{ i.label }}
            </el-menu-item>
          </el-sub-menu>

          <!-- 一级菜单 -->
          <el-menu-item v-else :key="item.url" :index="item.url" @click="clickEvent(item)">
            {{ item.label }}
          </el-menu-item>
        </template>
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<style>
.menu-wrapper {
  width: auto;
  background: none;
  margin:0 20px;

  .el-menu {
    --el-menu-bg-color:none;
    --el-menu-hover-bg-color: var(--btn-bg-hover-color-);
    --el-menu-active-color: #fff;
    --el-menu-text-color: #fff;
    --el-menu-hover-text-color: #fff;
    --el-menu-base-level-padding: 0px;
  }
  .el-sub-menu {
    position: relative;
  }
  .el-menu-item::before,
  .el-sub-menu::before {
    position: absolute;
    right: 0;
    top: 12px;
    z-index: 1;
    content: '';
    background: url() no-repeat;
    width: 2px;
    height: 36px;
  }
}
</style>
