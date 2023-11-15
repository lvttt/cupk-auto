<template>
    <div class="tip">
        {{ rank[0] + '&nbsp;&nbsp;&nbsp;' + rank[1]}}
    </div><br>
    <el-collapse v-model="activeName" accordion>
        <el-collapse-item v-for="term,idx in gradelist" :name="idx" >
            <template #title>
            {{ term.term }} 
            </template>
            <div v-if="term.sublist.length == 0">
            No Course
            </div>
            <div v-else>
                <el-row style="margin-top: 15px;">
                    <el-col :span="3" class="center">序号</el-col>
                    <el-col :span="3" class="center">课程</el-col>
                    <el-col :span="3" class="center">分数</el-col>
                    <el-col :span="3" class="center">学分</el-col>
                    <el-col :span="3" class="center">学时</el-col>
                    <el-col :span="3" class="center">课程属性</el-col>
                    <el-col :span="3" class="center">成绩标识</el-col>
                </el-row>
                <el-row  v-for="course,idx in term.sublist" style="margin-top: 15px;">
                    <el-col :span="3" class="center">{{ idx + 1 }}</el-col>
                    <el-col :span="3" class="center">{{ course.course }}</el-col>
                    <el-col :span="3" class="center">{{ course.score }}</el-col>
                    <el-col :span="3" class="center">{{ course.credit }}</el-col>
                    <el-col :span="3" class="center">{{ course.time }}</el-col>
                    <el-col :span="3" class="center">{{ course.type }}</el-col>
                    <el-col :span="3" class="center">{{ course.status }}</el-col>
                </el-row>
            </div>
            
        </el-collapse-item>
        <el-collapse-item :name="len" :title="gradelist2.term">
            <div v-if="len2 == 0">
                <!-- 不知道什么bug，用len2 代替 gradelist2.sublist.length -->
            No Course
            </div>
            <div v-else>
                <el-row style="margin-top: 15px;">
                    <el-col :span="4" class="center">序号</el-col>
                    <el-col :span="4" class="center">开课学期</el-col>
                    <el-col :span="4" class="center">课程名称</el-col>
                    <el-col :span="4" class="center">成绩</el-col>
                    <el-col :span="4" class="center">备注</el-col>
                </el-row>
                <el-row v-for="course,idx in gradelist2.sublist" style="margin-top: 15px;">
                    <el-col :span="4" class="center">{{ idx + 1 }}</el-col>
                    <el-col :span="4" class="center">{{ course.time }}</el-col>
                    <el-col :span="4" class="center">{{ course.course }}</el-col>
                    <el-col :span="4" class="center">{{ course.score }}</el-col>
                    <el-col :span="4" class="center">{{ course.platform }}</el-col>
                </el-row>
            </div>
            
        </el-collapse-item>
    </el-collapse>
    <div accordion v-loading="loading" class="loading"
    element-loading-text="Loading..."></div>
</template>

<script setup>
import { onBeforeMount, onMounted, ref } from 'vue'
import {ElMessage} from 'element-plus'

const activeName = ref('0')
const gradelist = ref([])   // 其余课程成绩
const gradelist2 = ref({})  // 形势与政策成绩
const len = ref(0)
const len2 = ref(0)   
const rank = ref([])
const loading = ref(true)

onBeforeMount(async ()=>{
    fetch("http://localhost:8877/jwxt/cj/getrank").then(res=>res.json())
    .then(res=>{
        if(res.code == 1){
            rank.value = res.data
        }else{
            ElMessage({
                message: "获取排名失败",
                type: 'error'
            })
        }
    }).catch(err=>{
        console.log(err)
    })

    fetch("http://localhost:8877/jwxt/cj/getlist").then(res=>res.json())
    .then(res=>{
        if(res.code == 1){
            len.value = res.data.length
            gradelist.value = res.data.slice(0, len.value-1).reverse()
            gradelist2.value = res.data[len.value-1]
            len2.value = gradelist2.value.sublist.length
            loading.value = false
        }else{
            ElMessage({
                message: "获取成绩失败",
                type: 'error'
            })
        }
    })
    .catch(err=>{
        console.log(err)
    })
})

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