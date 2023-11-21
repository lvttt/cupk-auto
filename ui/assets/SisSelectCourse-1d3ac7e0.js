import{_ as Y,r as i,a as d,o as g,c as F,b as l,w as r,i as u,d as B,F as Z,E as b,k as ee,g as f,j as y,p as le,h as ae,l as te}from"./index-151888fb.js";const m=x=>(le("data-v-1b2561a8"),x=x(),ae(),x),oe=m(()=>u("div",{class:"tip"},[f(" # 建议只使用"),u("em",null," 本学期计划选课 "),f("和"),u("em",null," 公选课选课 "),u("br"),f(" # "),u("em",null,"抢课过程中不要切换界面或进行其他操作")],-1)),se=m(()=>u("br",null,null,-1)),ne=m(()=>u("div",{class:"el-upload__text"},[f(" 拖拽上传 or "),u("em",null,"点击上传")],-1)),ue=m(()=>u("div",{class:"el-upload__tip"}," 仅支持xls文件，建议上传筛选后的文件，减少excel行数，不超过50行，否则会出现卡顿 ",-1)),ce=m(()=>u("br",null,null,-1)),re={class:"qkdiv"},ie=m(()=>u("span",{class:"tip"}," 失败循环抢课次数 ：",-1)),de=m(()=>u("br",null,null,-1)),pe=m(()=>u("br",null,null,-1)),ve=m(()=>u("br",null,null,-1)),_e={key:0,class:"demo-pagination-block"},fe={__name:"SisSelectCourse",setup(x){const k=i(1),I=i(8),E=i(1),S=i({}),w=i([]),V=i([]),j=i([]),z=i([]),D=i([]),c=i("可选课程"),a=i(w.value),N=i(0);function q(e){e=="可选课程"?a.value=w.value:e=="本学期计划选课"?a.value=V.value:e=="专业内跨年级选课"?a.value=j.value:e=="跨专业选课"?a.value=z.value:a.value=D.value}function O(e){if(S.value[e.courseId+e.classId]==1){b({message:"该课程已添加",type:"warning"});return}e.mode=="0"?V.value.push(e):e.mode=="1"?j.value.push(e):e.mode=="2"?z.value.push(e):e.mode=="3"&&D.value.push(e),S.value[e.courseId+e.classId]=1,N.value=a.value.length}function J(e,o){S.value[o.courseId+o.classId]=0,c.value=="本学期计划选课"?(V.value.splice(e,1),a.value=V.value):c.value=="专业内跨年级选课"?(j.value.splice(e,1),a.value=j.value):c.value=="跨专业选课"?(z.value.splice(e,1),a.value=z.value):(D.value.splice(e,1),a.value=D.value)}function M(e,o){e.code==1&&(w.value=e.data,a.value=w.value,N.value=a.value.length,e.data.forEach((p,_,t)=>{S.value[p.courseId+p.classId]=0}))}function Q(e){return new Promise(o=>setTimeout(o,e))}function R(e){return e=="本学期计划选课"?0:e=="专业内跨年级选课"?1:e=="跨专业选课"?2:3}async function A(){await fetch("http://localhost:8877/jwxt/xk/login").then(e=>e.json()).then(e=>{e.code!=1&&b({message:"进入选课系统失败",type:"error"})}).catch(e=>{console.log(e)})}async function P(e,o,p,_){await fetch("http://localhost:8877/jwxt/xk/selectCourse",{method:"POST",headers:{"Content-Type":"application/json;charset=UTF-8"},body:JSON.stringify({params:{kcxx:p,skls:"",skxq:"",skjc:"",sfym:"false",sfct:"false",sfxx:"false"},courselist:e,mode:o})}).then(t=>t.json()).then(t=>{t.code==1&&(_>-1?t.data[0].success&&(a.value[_].ready=1):t.data.forEach((h,s,C)=>{h.success&&(a.value[s].ready=1)}))}).catch(t=>{console.log(t)})}async function G(){await A();let e=["本学期计划选课","公选课选课","专业内跨年级选课","跨专业选课"];for(let o=0;o<e.length;o++){if(c.value=e[o],q(c.value),a.value.length==0){b({message:"没有可抢课程",type:"warning"});continue}let p=R(c.value);for(let _=0;_<E.value;_++){let t=[];if(a.value.forEach((s,C,v)=>{s.ready==0&&t.push(s.courseId+s.classId)}),b({message:`第${_+1}次抢课开始`,type:"success"}),await Q(1e3),p==0||p==3)await P(t,p,"");else for(let s=0;s<t.length;s++)await P([t[s]],p,t[s].substring(0,t[s].length-2),s);let h=!0;for(let s=0;s<a.value.length;s++)if(a.value[s].ready==0){h=!1;break}if(h){b({message:"本表所有课程已抢完",type:"success"});break}}}c.value="可选课程",q(c.value),b({message:"抢课结束",type:"success"})}const H=e=>{};function K(e){k.value=e,a.value=w.value.slice((k.value-1)*I.value,k.value*I.value),console.log(a.value)}return(e,o)=>{const p=d("el-icon"),_=d("el-upload"),t=d("el-radio-button"),h=d("el-radio-group"),s=d("el-input-number"),C=d("el-button"),v=d("el-table-column"),U=d("el-option"),L=d("el-select"),$=d("el-tag"),W=d("el-table"),X=d("el-pagination");return g(),F(Z,null,[oe,se,l(_,{class:"upload-demo",drag:"",action:"http://localhost:8877/jwxt/xk/upload",multiple:"",accept:".xls","on-success":M},{tip:r(()=>[ue]),default:r(()=>[l(p,{class:"el-icon--upload"},{default:r(()=>[l(ee(te))]),_:1}),ne]),_:1}),u("div",null,[l(h,{modelValue:c.value,"onUpdate:modelValue":o[0]||(o[0]=n=>c.value=n),size:"large",onChange:q},{default:r(()=>[l(t,{label:"可选课程"}),l(t,{label:"本学期计划选课"}),l(t,{label:"专业内跨年级选课"}),l(t,{label:"跨专业选课"}),l(t,{label:"公选课选课"})]),_:1},8,["modelValue"]),ce,u("div",re,[ie,l(s,{modelValue:E.value,"onUpdate:modelValue":o[1]||(o[1]=n=>E.value=n),min:1,max:10},null,8,["modelValue"]),l(C,{type:"primary",class:"qkbutton",onClick:G},{default:r(()=>[f("开始抢课")]),_:1})]),de]),pe,l(W,{ref:"tableRef",border:"",data:a.value,"max-height":"460px",style:{width:"100%"}},{default:r(()=>[l(v,{align:"center","show-overflow-tooltip":"",prop:"courseId",label:"课程代码"}),l(v,{align:"center","show-overflow-tooltip":"",prop:"classId",label:"教学班"}),l(v,{align:"center","show-overflow-tooltip":"",prop:"courseName",label:"课程名称"}),l(v,{align:"center","show-overflow-tooltip":"",prop:"teacher",label:"上课教师"}),l(v,{align:"center","show-overflow-tooltip":"",prop:"time",label:"上课时间"}),l(v,{align:"center","show-overflow-tooltip":"",prop:"class",label:"上课班级"}),l(v,{align:"center","show-overflow-tooltip":"",prop:"type",label:"课程属性"}),c.value=="可选课程"?(g(),y(v,{key:0,align:"center","show-overflow-tooltip":"",prop:"mode",label:"选课模式"},{default:r(n=>[l(L,{modelValue:n.row.mode,"onUpdate:modelValue":T=>n.row.mode=T,placeholder:"请选择"},{default:r(()=>[l(U,{label:"本学期计划选课",value:"0"}),l(U,{label:"专业内跨年级选课",value:"1"}),l(U,{label:"跨专业选课",value:"2"}),l(U,{label:"公选课选课",value:"3"})]),_:2},1032,["modelValue","onUpdate:modelValue"])]),_:1})):B("",!0),c.value!="可选课程"?(g(),y(v,{key:1,align:"center","show-overflow-tooltip":"",prop:"type",label:"抢课状态"},{default:r(n=>[n.row.ready==1?(g(),y($,{key:0,type:"success"},{default:r(()=>[f("已抢")]),_:1})):(g(),y($,{key:1,type:"danger"},{default:r(()=>[f("未抢")]),_:1}))]),_:1})):B("",!0),l(v,{align:"center",label:"添加选课"},{default:r(n=>[c.value=="可选课程"?(g(),y(C,{key:0,text:"",type:"primary",size:"small",onClick:T=>O(n.row)},{default:r(()=>[f("添加")]),_:2},1032,["onClick"])):(g(),y(C,{key:1,text:"",type:"danger",size:"small",onClick:T=>J(n.$index,n.row)},{default:r(()=>[f("删除")]),_:2},1032,["onClick"]))]),_:1})]),_:1},8,["data"]),ve,c.value=="可选课程"?(g(),F("div",_e,[l(X,{"current-page":k.value,"onUpdate:currentPage":o[2]||(o[2]=n=>k.value=n),"page-size":I.value,"onUpdate:pageSize":o[3]||(o[3]=n=>I.value=n),"pager-count":5,layout:"total, prev, pager, next, jumper",total:N.value,onSizeChange:H,onCurrentChange:K},null,8,["current-page","page-size","total"])])):B("",!0)],64)}}},ge=Y(fe,[["__scopeId","data-v-1b2561a8"]]);export{ge as default};
