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
    <div class="qkdiv">
        <span class="tip"> 失败循环抢课次数 ：</span>
        <el-input-number v-model="qkcount" :min="1" :max="10" />
        <el-button type="primary" class="qkbutton"  @click="startQk">开始抢课</el-button>
    </div>
    
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
    <el-table-column v-if="radio1 != '可选课程'" align="center" show-overflow-tooltip prop="type" label="抢课状态">
        <template #default="scope">
            <el-tag v-if="scope.row.ready == 1" type="success">已抢</el-tag>
            <el-tag v-else type="danger">未抢</el-tag>
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
const qkcount = ref(1)

// create a dictionary of course data key=courseId+classId, value=(1 or 0)
const courseDataDict = ref({})


const allCourseData = ref([])
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

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

function getmode(value){
    if(value == '本学期计划选课') return 0
    else if(value == '专业内跨年级选课') return 1
    else if(value == '跨专业选课') return 2
    else return 3
}

async function loginxk(){
    await fetch("http://localhost:8877/jwxt/xk/login").then(res=>res.json())
    .then(res=>{
        console.log(res);
    }).catch(err=>{
        console.log(err);
    })
}

async function requestSelectCourse(courselist, mode, courseid, idx){
    await fetch("http://localhost:8877/jwxt/xk/selectCourse", {
        method: "POST",
        headers: {
            "Content-Type": "application/json;charset=UTF-8"
        },
        body: JSON.stringify({
            "params" : {
                'kcxx': courseid,
                'skls': '',
                'skxq': '',
                'skjc': '',
                'sfym': 'false',
                'sfct': 'false',
                'sfxx': 'false',
            },
            "courselist": courselist,
            "mode": mode
        })
    }).then(res=>res.json())
    .then(res=>{
        if(res.code == 1){
            if(idx > -1){
                if(res.data[0].success)
                    courseData.value[idx].ready = 1
            }else{
                res.data.forEach((v, i, arr)=>{
                    if(v.success)
                        courseData.value[i].ready = 1
                })
            }
            
        }
    }).catch(err=>{
        console.log(err);
    })
}

async function startQk(){
    await loginxk()
    let order = ['本学期计划选课', '公选课选课','专业内跨年级选课', '跨专业选课']
    for(let i = 0; i < order.length; i++){
        radio1.value = order[i]
        radioChange(radio1.value)
        if(courseData.value.length == 0){
            ElMessage({
                message: '没有可抢课程',
                type: 'warning'
            })
            continue
        }
        let mode = getmode(radio1.value)
        let courselist = []
        courseData.value.forEach((v, i, arr)=>{
            courselist.push(v.courseId + v.classId)
        })
        for(let j = 0; j < qkcount.value; j++){
            
            ElMessage({
                message: `第${j+1}次抢课开始`,
                type: 'success'
            })
            await sleep(1000);
            
            // request
            if(mode == 0 || mode == 3) 
                await requestSelectCourse(courselist, mode, '')
            else{
                for(let k = 0; k < courselist.length; k++){
                    await requestSelectCourse([courselist[k]], mode, courselist[k].substring(0, courselist[k].length-2), k)
                }
            }

            let flag = true
            for(let k = 0; k < courseData.value.length; k++){
                if(courseData.value[k].ready == 0){
                    flag = false
                    break
                }
            }
            if(flag) {
                ElMessage({
                    message: '本表所有课程已抢完',
                    type: 'success'
                })
                break
            }
        }
    }
    radio1.value = '可选课程'
    radioChange(radio1.value)
    ElMessage({
        message: '抢课结束',
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
.qkdiv{
    position: absolute;
    right: 2%;
}
.qkbutton{
    margin-left: 10px;
}
</style>