<script setup>
/**
 * @description 选项卡
 *
 * menuList 数据列表
 * item.label 名称
 * item.path 路径
 * item.query 查询参数
 *
 * menuEvent 菜单列表的点击事件
 */
import { inject } from 'vue'

let { menuList, menuEvent } = inject('center')
// 采用自带icon
const iconList = [
  'Notification',
  'Connection',
  'ChatDotRound',
  'PieChart',
  'Message',
  'Notebook',
  'Postcard',
  'DataLine',
  'OfficeBuilding',
  'School',
  'Coin',
  'Calendar',
  'CreditCard',
  'Refrigerator',
  'Paperclip',
  'TakeawayBox',
  'Apple',
  'Orange',
  'Coffee',
  'MapLocation',
  'Film',
  'Monitor',
  'Iphone',
  'DocumentAdd',
  'Document',
  'Tickets',
  'Memo',
]
</script>

<template>
  <div class="centermenu">
    <div class="biaoti2">
       <div class="title">快捷入口<i></i></div>
    </div>
    <div class="list">
      <div v-for="(item, index) in menuList" :key="index" class="item" @click="menuEvent(item)">
        <el-icon>
          <component :is="iconList[index]" />
        </el-icon>

        <span>{{ item.label }}</span>
      </div>
    </div>
  </div>
</template>

<style>
.centermenu {
  padding: 26px 22px 22px;
  border: 1px solid #dfece3;
  border-radius: 8px;
  background: #ffffff;
  box-shadow: 0 18px 42px rgba(56, 83, 61, .10);
}
.centermenu .biaoti2{
    margin:0 0 18px;
  }

.centermenu .biaoti2 .title {
    font-size: 22px;
    color: #243b2a;
    font-weight: 900;
  }

.centermenu .list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}

.centermenu .list .item {
      cursor: pointer;
      min-height: 74px;
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-items: center;
      gap: 10px;
      background: #f5f8f3;
      border: 1px solid #dfece3;
      border-radius: 8px;
      color: #294634;
      transition: transform 0.24s ease, box-shadow 0.24s ease, background 0.24s ease;
      padding:14px 12px;
}

.centermenu .list .item:hover {
        color: #fff;
        background: #2f6f4e;
        box-shadow: 0 12px 24px rgba(47, 111, 78, .20);
        transform: translateY(-2px);

  }

.centermenu .list .item .el-icon {
      flex: none;
      font-size: 24px;
}

.centermenu .list .item span {
      line-height:1;
      min-width: 0;
      font-weight: 800;
      overflow-wrap: anywhere;
}

</style>
