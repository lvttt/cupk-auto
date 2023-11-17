<template>
    <router-link to="/fp/home/main" class="router-link">
        <el-menu-item index="/fp/home/main">
            <el-icon><house /></el-icon>
            <template #title>主页</template>
        </el-menu-item>
    </router-link>
    <el-menu-item @click="isopen = true">
        <el-icon><data-board /></el-icon>
        <template #title>修改密码</template>
    </el-menu-item>
    <el-drawer v-model="isopen" :with-header="false" :before-close="beforeClose">
        <div class="tip">
            # 密码修改规则：非空即可
        </div>
        <div class="pwd-div">
            <el-input class="pwd-input" v-model="oldPwd" placeholder="请输入新密码" show-password/><br>
            <el-button color="rgb(217,71,60)" @click="changePwd(oldPwd)">确认修改</el-button>
        </div>
    </el-drawer>
</template>

<script setup>
import {DataBoard, House} from '@element-plus/icons-vue'
import {ref} from 'vue'
import {changePwd} from './modules/changePwd.js'

const isopen = ref(false)
const oldPwd = ref('')
function beforeClose(done) {
    oldPwd.value = ''
    done()
}
</script>

<style scoped>
.pwd-input{
    width: 200px;
    margin-bottom: 10px;
}
.pwd-div{
    margin-top: 80%;
}
.tip{
    margin-top: 10%;
    font-size: 13px;
}
</style>