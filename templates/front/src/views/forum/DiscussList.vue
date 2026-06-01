
<script setup>
/**
 * @description 说明
 * 
 * discussList 列表数据
 * item.img 头像
 * item.username 评论人
 * item.content 评论内容
 * item.addtime 时间
 * item.hasRemove 是否有删除权限
 * item.childs 二级评论列表数据
 * 
 * reply 回复事件
 * remove 删除事件
 */
import { inject } from 'vue'

let { discussList, remove, reply } = inject('detail')
</script>

<template>
  <div class="discusslist-forum">
    <div class="item" v-for="item in discussList" :key="item.id">
      <div class="item-left">
        <img class="img" :src="item.img" />
      </div>
      <div class="item-right">
        <div class="nickname">{{ item.username }}</div>

        <div class="content">
          <div class="ql-snow ql-editor" v-html="item.content"></div>
        </div>

        <div class="action">
          <div class="time">
            <span>{{ item.addtime }}</span>
          </div>
          <div class="btn">
            <el-button size="small" @click="reply(item)">回复</el-button>
            <el-button v-if="item.hasRemove" type="danger" size="small" @click="remove(item.id)">删除</el-button>
          </div>
        </div>
      </div>
      <div class="reply-box" v-if="item.childs">
        <div class="item" v-for="i in item.childs" :key="i.id">
          <div class="item-left">
            <img class="img" :src="i.img" />
          </div>
          <div class="item-right">
            <div class="nickname">{{ i.username }}</div>

            <div class="content">
              <div class="ql-snow ql-editor" v-html="i.content"></div>
            </div>

            <div class="action">
              <div class="time">
                <span>{{ i.addtime }}</span>
              </div>

              <div class="btn">
                <el-button v-if="i.hasRemove" type="danger" size="small" @click="remove(i.id)">删除</el-button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.discusslist-forum {
  .item {
    display: flex;
    flex-wrap: wrap;
    padding-top: 28px;
    font-size: 14px;
    color: #222;
    padding-bottom: 10px;
    border-bottom: 1px dashed #eee;
    &:last-of-type {
      border-bottom: none;
    }
    & > .item-left {
      flex: none;
      width: 64px;
    }
    & > .item-right {
      flex: 1 1 auto;
      width: 0;
    }
    & > .reply-box {
      width: 100%;
      padding-left: 64px;
    }
  }

  .img {
    width: 48px;
    height: 48px;
    border-radius: 50%;
  }
  .nickname {
    font-size: 13px;
    color: #222;
    font-weight: 600;
  }

  .action {
    display: flex;
    justify-content: space-between;
  }
  .time {
    font-size: 13px;
    color: #9195a3;
  }
}
</style>
  