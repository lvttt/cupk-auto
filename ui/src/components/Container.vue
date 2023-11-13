<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <!-- header -->
                <el-row>
                    <el-col :span="8" ><el-image
                            style="width: 90%; height: 80%"
                            :src="page == '教务系统' ? jwxtLogo : fpLogo"
                            :zoom-rate="1.2"
                            :max-scale="7"
                            :min-scale="0.2"
                            :initial-index="4"
                            fit="cover"
                            />
                    </el-col>
                    <el-col :span="2" :offset="14"><el-button :icon="House" class="logout" @click="logout">退出</el-button></el-col>
                </el-row>
            </el-header>
            <el-container>
                <el-aside width="el_menu_width">
                    <!-- aside -->
                    <el-menu
                        default-active="1"
                        class="el-menu-vertical"
                        :collapse="isCollapse"
                    >   
                    <br>
                        <el-button plain :icon="Expand" circle @click="changeCollapse" v-if="isCollapse" />
                        <el-button plain :icon="Fold" circle @click="changeCollapse" v-else /><br><br>
                            <sis-aside v-if="page == '教务系统'"></sis-aside>
                            <fp-aside v-else-if="page == '融合门户'"></fp-aside>
                    </el-menu>
                </el-aside>
                <el-main>
                    <!-- main -->
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup>
import SisAside from './SIS/SisAside.vue'
import FpAside from './FusionPortal/FpAside.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import {
    Fold,
    Expand,
    House
} from '@element-plus/icons-vue'
import jwxtLogo from '../assets/jwxt_logo.gif'
import fpLogo from '../assets/rhmh_logo.png'

const isCollapse = ref(false)
const router = useRouter()

function changeCollapse(){
    isCollapse.value = ! isCollapse.value;
}

function logout(){
    router.push({path: "/"})
}

// props
defineProps({
  page: String
})
</script>

<style scoped>
.el-menu-vertical:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
.el-aside{
    max-width: 300px;
}
.el-menu{
    height: 90vh;
}
.el-header{
    border-bottom: 1px solid #ebeef5;
}
.logout{
    margin:10% auto;
}
</style>