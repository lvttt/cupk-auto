<template>
  <div class="tip">
    # 自动评教默认打分为95分
  </div><br>
    <el-collapse v-model="activeName" >
      <el-collapse-item v-for="rateterm in ratelist" name="1" >
        <template #title>
         {{ rateterm.batch + "&nbsp;&nbsp;&nbsp;&nbsp; " + rateterm.term }} 
        </template>
        <div v-if="rateterm.sublist.length == 0">
          No Course
        </div>
        <el-row v-else v-for="course,idx in rateterm.sublist" style="margin-top: 15px;">
            <el-col :span="4" class="center">{{ idx + 1 }}</el-col>
            <el-col :span="4" class="center">{{ course.course }}</el-col>
            <el-col :span="4" class="center">{{ course.teacher }}</el-col>
            <el-col :span="4" class="center">{{ course.score }}</el-col>
            <el-col :span="4" class="center">{{ course.finish }}</el-col>
            <el-col :span="4" class="center">
                <el-button text style="color: #66b1ff;" @click="requestRate(course)">评教</el-button>
            </el-col>
        </el-row>
      </el-collapse-item>
    </el-collapse>
    <div accordion v-loading="loading" class="loading"
    element-loading-text="Loading..."></div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import {ElMessage} from 'element-plus'

const activeName = ref('0')
const ratelist = ref([])
const loading = ref(true)

onMounted(()=>{
    fetch("http://localhost:8877/jwxt/pj/getlist").then(res=>res.json())
    .then(res=>{
        ratelist.value = res.data
        ratelist.value[0].sublist = [{
            "course": "计算机系统基础",
            "teacher": "XXX",
            "score": 0,
            "finish": "未评教"
        },{
            "course": "离散数学",
            "teacher": "XXX",
            "score": 0,
            "finish": "已评教"
        }]
        loading.value = false
    })
    .catch(err=>{
        console.log(err)
    })
})

function requestRate(row){
  row.finish = "已评教"
  row.score = 95
  ElMessage({
    message: '评教成功',
    type: 'success'
  })
}

</script>

<style scoped>
.loading{
    margin: 25% auto;
}
.tip{
    margin-top: 10px;
    font-size: 12px;
    text-align: left;
}
.center{
  margin: auto;
}
</style>