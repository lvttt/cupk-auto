<template>
    <router-link to="/sis/home/qk" class="router-link">
        <el-menu-item index="/sis/home/qk">
            <el-icon><data-board /></el-icon>
            <template #title>抢课助手</template>
        </el-menu-item>
    </router-link>
    <router-link to="/sis/home/pj" class="router-link">
        <el-menu-item index="/sis/home/pj">
            <el-icon><star /></el-icon>
            <template #title>自动评教</template>
        </el-menu-item>
    </router-link>
    <router-link to="/sis/home/cj" class="router-link">
        <el-menu-item index="/sis/home/cj">
            <el-icon><reading /></el-icon>
            <template #title>成绩查询</template>
        </el-menu-item>
    </router-link>
</template>

<script setup>
import {DataBoard, Star, Reading} from '@element-plus/icons-vue'

</script>

<style scoped>
</style>