
<script setup>
/**
 * @description 点赞、收藏
 *
 * hasThumbsUp 是否有点赞功能
 * thumbsUpId 是否已经点赞
 * thumbsUpEvent 点赞事件
 *
 * hasStoreUp 是否有收藏功能
 * storeUpId 是否已经收藏
 * storeUpEvent 收藏事件
 *
 * data.thumbsupnum 点赞数量
 * data.storeupnum 收藏数量
 * 
 * hasReport 是否有举报
 * reportEvent 举报事件
 *
 */
import { inject } from 'vue'

let {
  data,
  hasThumbsUp,
  thumbsUpId,
  thumbsUpEvent,
  hasStoreUp,
  storeUpId,
  storeUpEvent,
  hasReport,
  reportEvent,
} = inject('detail')
</script>

<template>
  <div class="buttonlist-view">
    <!-- 点赞 -->
    <div class="item" v-if="hasThumbsUp" @click="thumbsUpEvent">
      <!-- 已点赞的icon -->
      <el-icon v-if="thumbsUpId">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
          <path
            fill="currentColor"
            d="M313.6 924.48a70.4 70.4 0 0 1-74.152-5.365 70.4 70.4 0 0 1-27.992-68.875l37.888-220.928L88.96 472.96a70.4 70.4 0 0 1 3.788-104.225A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 100.246-28.595 70.4 70.4 0 0 1 25.962 28.595l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"
          ></path>
        </svg>
      </el-icon>

      <!-- 未点赞的icon -->
      <el-icon v-else>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
          <path
            fill="currentColor"
            d="m512 747.84 228.16 119.936a6.4 6.4 0 0 0 9.28-6.72l-43.52-254.08 184.512-179.904a6.4 6.4 0 0 0-3.52-10.88l-255.104-37.12L517.76 147.904a6.4 6.4 0 0 0-11.52 0L392.192 379.072l-255.104 37.12a6.4 6.4 0 0 0-3.52 10.88L318.08 606.976l-43.584 254.08a6.4 6.4 0 0 0 9.28 6.72zM313.6 924.48a70.4 70.4 0 0 1-102.144-74.24l37.888-220.928L88.96 472.96A70.4 70.4 0 0 1 128 352.896l221.76-32.256 99.2-200.96a70.4 70.4 0 0 1 126.208 0l99.2 200.96 221.824 32.256a70.4 70.4 0 0 1 39.04 120.064L774.72 629.376l37.888 220.928a70.4 70.4 0 0 1-102.144 74.24L512 820.096l-198.4 104.32z"
          ></path>
        </svg>
      </el-icon>
    </div>

    <div class="item" v-if="hasStoreUp" @click="storeUpEvent">
      <!-- 已点赞的icon -->
      <el-icon v-if="storeUpId">
        <svg
          t="1761288957004"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="1938"
          width="256"
          height="256"
        >
          <path
            d="M854.844952 236.178286a213.333333 213.333333 0 0 0-301.689904 0L512 277.333333l-41.155048-41.155047a213.333333 213.333333 0 0 0-301.714285 0L161.499429 243.809524a213.333333 213.333333 0 0 0 0 301.714286L512 896l350.47619-350.47619a213.333333 213.333333 0 0 0 0-301.714286l-7.631238-7.631238z"
            p-id="1939"
          ></path>
        </svg>
      </el-icon>

      <!-- 未点赞的icon -->
      <el-icon v-else>
        <svg
          t="1761288918326"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="1572"
          width="256"
          height="256"
        >
          <path
            d="M512 360.301714l-78.823619-78.823619a160.060952 160.060952 0 1 0-226.377143 226.377143L512 813.031619 817.176381 507.855238a160.060952 160.060952 0 1 0-226.377143-226.377143L512 360.301714z m0 535.698286L165.302857 549.327238A218.721524 218.721524 0 1 1 474.672762 240.006095l37.302857 37.327238 37.351619-37.327238 0.024381-0.024381A218.721524 218.721524 0 0 1 858.648381 549.302857L512 896z"
            p-id="1573"
          ></path>
        </svg>
      </el-icon>
    </div>
    <div v-if="hasReport" class="item" title="举报" @click="reportEvent">
      <!-- 举报 -->
      <el-icon>
        <svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1024 1024">
          <path
            fill="currentColor"
            d="M928.99 755.83 574.6 203.25c-12.89-20.16-36.76-32.58-62.6-32.58s-49.71 12.43-62.6 32.58L95.01 755.83c-12.91 20.12-12.9 44.91.01 65.03 12.92 20.12 36.78 32.51 62.59 32.49h708.78c25.82.01 49.68-12.37 62.59-32.49s12.92-44.91.01-65.03M554.67 768h-85.33v-85.33h85.33zm0-426.67v298.66h-85.33V341.32z"
          ></path>
        </svg>
      </el-icon>
    </div>
  </div>
</template>
<style>
.buttonlist-view {
  position: fixed;
  left: calc(50% - 550px);
  bottom: 100px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 6px 16px 0 rgba(0, 0, 0, 0.08), 0 3px 6px -4px rgba(0, 0, 0, 0.12),
    0 9px 28px 8px rgba(0, 0, 0, 0.05);
  background-color: #fff;
  border-radius: 8px;

  .el-icon {
    font-size: 20px;
  }

  .item {
    padding: 6px 10px;
    cursor: pointer;
    transition: all 0.3s linear;
    border-bottom: 1px solid rgba(5, 5, 5, 0.06);
    &:last-of-type {
      border-bottom: none;
    }
    &:hover {
      background-color: rgba(0, 0, 0, 0.06);
      color: var(--btn-bg-color-);
    }
  }
}
</style>  
  