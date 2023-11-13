<template>
    <router-link to="/sis/home/qk" class="router-link">
        <el-menu-item index="1">
            <el-icon><data-board /></el-icon>
            <template #title>抢课助手</template>
        </el-menu-item>
    </router-link>
</template>

<script setup>
import {DataBoard} from '@element-plus/icons-vue'

</script>

<style scoped>
.router-link{
    text-decoration: none;
}
</style>