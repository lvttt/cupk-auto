<template>
    <el-collapse v-model="activeName" >
      <el-collapse-item v-for="rateterm in ratelist" name="1">
        <template #title>
         {{ rateterm.batch + "&nbsp;&nbsp;&nbsp;&nbsp; " + rateterm.term }} 
        </template>
        <div v-if="rateterm.sublist.length == 0">
          No Course
        </div>
      </el-collapse-item>
    </el-collapse>
    <div accordion v-loading="loading" class="loading"
    element-loading-text="Loading..."></div>
</template>

<script setup>
import { ref } from 'vue'

const activeName = ref('0')
const ratelist = ref([])
const loading = ref(true)

    fetch("http://localhost:8877/jwxt/pj/getlist").then(res=>res.json())
    .then(res=>{
        console.log(res)
        ratelist.value = res.data
        loading.value = false
    })
    .catch(err=>{
        console.log(err)
    })

</script>

<style scoped>
.loading{
    margin: 25% auto;
}

</style>