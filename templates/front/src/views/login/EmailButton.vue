
<script setup>
import { inject } from 'vue'
const { hasEmail, emailEvent, emailType } = inject('login')
</script>
<template>
  <el-button v-show="hasEmail" class="email-btn" @click="emailEvent">{{ emailType }}</el-button>
</template>

