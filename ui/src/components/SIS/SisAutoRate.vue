<template>
  <div class="tip">
    # 自动评教默认打分为95分<br>
    # 评教一个个点
  </div><br>
    <el-collapse v-model="activeName" >
      <el-collapse-item v-for="rateterm in ratelist" name="1" >
        <template #title>
         {{ rateterm.batch + "&nbsp;&nbsp;&nbsp;&nbsp; " + rateterm.term }} 
        </template>
        <div v-if="rateterm.sublist.length == 0">
          No Course
        </div>
        <div v-else>
          <el-row>
            <el-col :span="4" class="center">序号</el-col>
            <el-col :span="4" class="center">课程</el-col>
            <el-col :span="4" class="center">教师</el-col>
            <el-col :span="4" class="center">分数</el-col>
            <el-col :span="4" class="center">是否已评教</el-col>
            <el-col :span="4" class="center">操作</el-col>
          </el-row>
            <el-row v-for="course,idx in rateterm.sublist" style="margin-top: 15px;">
              <el-col :span="4" class="center">{{ idx + 1 }}</el-col>
              <el-col :span="4" class="center">{{ course.course }}</el-col>
              <el-col :span="4" class="center">{{ course.teacher }}</el-col>
              <el-col :span="4" class="center">{{ course.score }}</el-col>
              <el-col :span="4" class="center">{{ course.finish }}</el-col>
              <el-col :span="4" class="center">
                  <el-button text style="color: #66b1ff;" @click="requestRate(course)">评教</el-button>
              </el-col>
          </el-row>
        </div>
      </el-collapse-item>
    </el-collapse>
    <div accordion v-loading="loading" class="loading"
    :element-loading-text="loadtext"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import {ElMessage} from 'element-plus'

const activeName = ref('0')
const ratelist = ref([])
const loading = ref(true)
const loadtext = ref("Loading...")

onMounted(()=>{
    fetch("http://localhost:8877/jwxt/pj/getlist").then(res=>res.json())
    .then(res=>{
      if(res.code == 1){
          ratelist.value = res.data
          loading.value = false
      }else{
        ElMessage({
            message: '获取评教列表失败',
            type: 'error'
          })
      }
        
    })
    .catch(err=>{
        console.log(err)
    })
})

function requestRate(row){
  loadtext.value = "Rating..."
  loading.value = true
  fetch("http://localhost:8877/jwxt/pj/rate",{
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "url": row.url,
    })
  }).then(res=>res.json())
  .then(res=>{
    if(res.code == 1){
      loading.value = false
      row.finish = "是"
      row.score = 95
      ElMessage({
        message: '评教成功',
        type: 'success'
      })
    }else{
      ElMessage({
        message: '评教失败',
        type: 'error'
      })
    }
      
  }).catch(err=>{
      console.log(err)
  })
}

</script>

<style scoped>
.loading{
    position: absolute;
    left: 50%;
    top: 50%;
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