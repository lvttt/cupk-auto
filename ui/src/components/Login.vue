<template>
    <el-select v-model="value" class="m-2" placeholder="Select" size="large">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value"
    />
  </el-select><br><br>
  <el-button type="primary" size="large" round @click="handleClick">登录</el-button>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const value = ref(1)
const router = useRouter()


const options = [{
  "value": 1,
  "label": "教务系统"
},{
  "value": 2,
  "label": "融合门户"
}]

function handleClick() {
  if(value.value === 1){
      // 登录教务系统
      fetch("http://localhost:8877/jwxt/login").then(res=>res.json())
      .then(res=>{
          if(res.code === 1){
              ElMessage({
                  message: '登录成功',
                  type: 'success'
              })
              // props: {page: 'SIS'}
              router.push({path: "/home", query: {page: "SIS"}})
          }else{
              ElMessage.error(res.msg)
          }
      })
      .catch(err=>{
        console.log(err)
      })
  }else if(value.value === 2){
      // 登录融合门户
      ElMessage({
          message: '登录成功',
          type: 'success'
      });
      router.push({path: "/home", query: {page: "FusionPortal"}})
  }
}

</script>

<style scoped>

</style>
