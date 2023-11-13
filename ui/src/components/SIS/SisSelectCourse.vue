<template>
    <el-upload
    class="upload-demo"
    drag
    action="http://localhost:8877/jwxt/xk/upload"
    multiple
    accept=".xls"
    :on-success="getCourseData"
  >
    <el-icon class="el-icon--upload"><upload-filled /></el-icon>
    <div class="el-upload__text">
      拖拽上传 or <em>点击上传</em>
    </div>
    <template #tip>
      <div class="el-upload__tip">
        仅支持xls文件，建议上传筛选后的文件，减少excel行数，不超过50行，否则会出现卡顿
      </div>
    </template>
  </el-upload>
  <div>
    <el-radio-group v-model="radio1" size="large" @change="radioChange">
      <el-radio-button label="可选课程" />
      <el-radio-button label="本学期计划选课" />
      <el-radio-button label="专业内跨年级选课" />
      <el-radio-button label="跨专业选课" />
      <el-radio-button label="公选课选课" />
    </el-radio-group>
    <el-button type="primary" class="qkbutton" @click="startQk">开始抢课</el-button>
    <br>
        <div class="tip">建议只使用<em> 本学期计划选课 </em>和<em> 公选课选课 </em></div>
  </div><br>
  <el-table ref="tableRef" border :data="courseData" max-height="460px" style="width: 100%">
    <el-table-column align="center" show-overflow-tooltip prop="courseId" label="课程代码" />
    <el-table-column align="center" show-overflow-tooltip prop="classId" label="教学班"/>
    <el-table-column align="center" show-overflow-tooltip prop="courseName" label="课程名称"/>
    <el-table-column align="center" show-overflow-tooltip prop="teacher" label="上课教师"/>
    <el-table-column align="center" show-overflow-tooltip prop="time" label="上课时间"/>
    <el-table-column align="center" show-overflow-tooltip prop="class" label="上课班级"/>
    <el-table-column align="center" show-overflow-tooltip prop="type" label="课程属性"/>
    <el-table-column v-if="radio1 == '可选课程'" align="center" show-overflow-tooltip prop="mode" label="选课模式">
        <template #default="scope">
            <el-select v-model="scope.row.mode" placeholder="请选择">
                <el-option label="本学期计划选课" value="0"></el-option>
                <el-option label="专业内跨年级选课" value="1"></el-option>
                <el-option label="跨专业选课" value="2"></el-option>
                <el-option label="公选课选课" value="3"></el-option>
            </el-select>
        </template>
    </el-table-column>
    <el-table-column align="center" label="添加选课">
        <template #default="scope">
            <el-button text type="primary" size="small" v-if="radio1 == '可选课程'" @click="addCourse(scope.row)">添加</el-button>
            <el-button text type="danger" size="small" v-else @click="deleteCourse(scope.$index, scope.row)">删除</el-button>
        </template>
    </el-table-column>
  </el-table><br>
  <div v-if="radio1 == '可选课程'" class="demo-pagination-block">
        <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="pagesize"
        :pager-count="5"
        layout="total, prev, pager, next, jumper"
        :total= "datalength"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        />
    </div>
</template>

<script setup>
import { UploadFilled } from '@element-plus/icons-vue'
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const currentPage = ref(1)
const pagesize = ref(8)

// create a dictionary of course data key=courseId+classId, value=(1 or 0)
const courseDataDict = ref({})


const allCourseData = ref([{
    courseId: '123',
    courseName: '计算机网络',
    classId: '01',
    teacher: '张三',
    time: '周一 1-2节',
    class: '计算机科学与技术1班',
    type: '专业必修课',
    mode: ''
},{
    courseId: '456',
    courseName: '计算机组成原理',
    classId: '02',
    teacher: '李四',
    time: '周二 3-4节',
    class: '计算机科学与技术2班',
    type: '专业选修课',
    mode: ''
}])
const courseData01 = ref([])
const courseData02 = ref([])
const courseData03 = ref([])
const courseData04 = ref([])

const radio1 = ref('可选课程')
const courseData = ref(allCourseData.value)
const datalength = ref(0)

function radioChange(value){
    if(value == "可选课程"){
        courseData.value = allCourseData.value
    }else if(value == "本学期计划选课"){
        courseData.value = courseData01.value
    }else if(value == "专业内跨年级选课"){
        courseData.value = courseData02.value
    }else if(value == "跨专业选课"){
        courseData.value = courseData03.value
    }else{
        courseData.value = courseData04.value
    }
}

function addCourse(row){
    if(courseDataDict.value[row.courseId+row.classId] == 1){
        ElMessage({
          message: '该课程已添加',
          type: 'warning'
        })
        return
    }
    if(row.mode == '0')
        courseData01.value.push(row)
    else if(row.mode == '1')
        courseData02.value.push(row)
    else if(row.mode == '2')
        courseData03.value.push(row)
    else if(row.mode == '3')
        courseData04.value.push(row)
    courseDataDict.value[row.courseId+row.classId] = 1
    datalength.value = courseData.value.length
}

function deleteCourse(index, row){
    courseDataDict.value[row.courseId+row.classId] = 0
    if(radio1.value == '本学期计划选课'){
        courseData01.value.splice(index, 1)
        courseData.value = courseData01.value
    } 
    else if(radio1.value == '专业内跨年级选课'){
        courseData02.value.splice(index, 1)
        courseData.value = courseData02.value

    }  
    else if(radio1.value == '跨专业选课'){
        courseData03.value.splice(index, 1)
        courseData.value = courseData03.value

    }
    else{
        courseData04.value.splice(index, 1)
        courseData.value = courseData04.value
    }
}

function getCourseData(res, file){
    if(res.code == 1){
        allCourseData.value = res.data
        courseData.value = allCourseData.value
        datalength.value = courseData.value.length
        res.data.forEach((v,i,arr)=>{
            courseDataDict.value[v.courseId+v.classId] = 0
        })
    }
}

function startQk(){
    if(courseData.value.length == 0){
        ElMessage({
          message: '请先上传课程数据',
          type: 'warning'
        })
        return
    }
    ElMessage({
      message: '开始抢课',
      type: 'success'
    })
}

const handleSizeChange = (val) => {

}

function handleCurrentChange(val){
    currentPage.value = val
    courseData.value = allCourseData.value.slice((currentPage.value-1)*pagesize.value, currentPage.value*pagesize.value)
    console.log(courseData.value);
}

</script>
<style scoped>
.tip{
    margin-top: 10px;
    font-size: small;
}
.tip em{
    color: red;
}
.el-pagination{
    justify-content: center;
}
.qkbutton{
    position: absolute;
    right: 2%;
}
</style>