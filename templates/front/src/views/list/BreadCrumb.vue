<script setup>
/**
 * @description 面包屑
 * homePath 首页路径
 * second 二级路径
 * lastTitle 当前页面名称
 */
import { inject } from 'vue'

const { homePath, second, lastTitle, backEvent } = inject('header')
</script>

<template>
  <div class="breadcrumb-toolbar">
    <el-breadcrumb class="app-breadcrumb" separator="›">
      <el-breadcrumb-item :to="{ path: homePath }">
        <span class="breadcrumb-home">
          <span class="breadcrumb-icon">
            <el-icon>
              <Location />
            </el-icon>
          </span>
          <span>首页</span>
        </span>
      </el-breadcrumb-item>

      <el-breadcrumb-item v-if="second.path" :to="second.path">
        {{ second.title }}
      </el-breadcrumb-item>

      <el-breadcrumb-item v-if="lastTitle">{{ lastTitle }}</el-breadcrumb-item>
    </el-breadcrumb>

    <button
      class="breadcrumb-back"
      type="button"
      title="上一页"
      aria-label="上一页"
      @click="backEvent"
    >
      <el-icon>
        <Back />
      </el-icon>
    </button>
  </div>
</template>

<style>
.breadcrumb-toolbar {
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  width: 100%;
  min-height: 58px;
  margin: 8px 0 16px;
  padding: 12px 16px;
  background: #fff;
  border: 1px solid #e2eadf;
  border-radius: 14px;
  box-shadow: 0 12px 28px rgba(31, 56, 37, .08);
}

.breadcrumb-toolbar * {
  box-sizing: border-box;
}

.app-breadcrumb {
  flex: 1 1 auto;
  min-width: 0;
  color: #4c594f;
  font-size: 15px;
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  line-height: 1.4;
}

.app-breadcrumb .el-breadcrumb__item {
  display: inline-flex;
  align-items: center;
  max-width: 100%;
}

.app-breadcrumb .el-breadcrumb__item .el-breadcrumb__inner {
  color: inherit;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-weight: 700;
}

.app-breadcrumb .el-breadcrumb__separator {
  margin: 0 9px;
  color: #a4afa6;
  font-weight: 800;
}

.app-breadcrumb .el-breadcrumb__inner.is-link {
  color: #1f2b22;
  font-weight: 800;
}

.app-breadcrumb .el-breadcrumb__inner.is-link:hover {
  color: #2f6f4e;
}

.breadcrumb-home {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.breadcrumb-icon {
  width: 28px;
  height: 28px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #edf6ee;
  color: #2f6f4e;
  font-size: 16px;
  flex: 0 0 auto;
}

.breadcrumb-back {
  box-sizing: border-box;
  width: 38px;
  height: 38px;
  min-width: 38px;
  min-height: 38px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
  padding: 0;
  border: 1px solid #dce5dc;
  border-radius: 50%;
  color: #415044;
  background: #fff;
  cursor: pointer;
  line-height: 1;
  outline: none;
  appearance: none;
  box-shadow: 0 8px 18px rgba(35, 63, 42, .08);
  transition: background-color .18s ease, border-color .18s ease, color .18s ease, box-shadow .18s ease;
}

.breadcrumb-back .el-icon,
.breadcrumb-back svg {
  font-size: 17px;
  pointer-events: none;
}

.breadcrumb-back:hover,
.breadcrumb-back:focus {
  border-color: #2f6f4e;
  color: #2f6f4e;
  background: #f3faf3;
}

@media (max-width: 560px) {
  .breadcrumb-toolbar {
    gap: 10px;
    min-height: 54px;
    margin: 6px 0 12px;
    padding: 10px 12px;
  }

  .app-breadcrumb {
    font-size: 14px;
  }

  .breadcrumb-icon {
    width: 26px;
    height: 26px;
  }

  .breadcrumb-back {
    width: 36px;
    height: 36px;
  }
}
</style>
