import{_ as E,r as _,s as G,E as B,a as v,n as F,o as c,c as d,i as k,t as n,b as t,w as e,q as L,F as m,f as y,g as a,p as M,h as q,j as x}from"./index-151888fb.js";const T=u=>(M("data-v-900506c9"),u=u(),q(),u),U={class:"tip"},z=T(()=>k("br",null,null,-1)),A={key:0},H={key:1},J={key:0},K={key:1},O={accordion:"",class:"loading","element-loading-text":"Loading..."},P={__name:"SisGrade",setup(u){const w=_("0"),j=_([]),p=_({}),i=_(0),S=_(0),g=_([]),b=_(!0);return G(async()=>{fetch("http://localhost:8877/jwxt/cj/getrank").then(l=>l.json()).then(l=>{l.code==1?g.value=l.data:B({message:"获取排名失败",type:"error"})}).catch(l=>{console.log(l)}),fetch("http://localhost:8877/jwxt/cj/getlist").then(l=>l.json()).then(l=>{l.code==1?(i.value=l.data.length,j.value=l.data.slice(0,i.value-1).reverse(),p.value=l.data[i.value-1],S.value=p.value.sublist.length,b.value=!1):B({message:"获取成绩失败",type:"error"})}).catch(l=>{console.log(l)})}),(l,N)=>{const s=v("el-col"),f=v("el-row"),V=v("el-collapse-item"),C=v("el-collapse"),I=F("loading");return c(),d(m,null,[k("div",U,n(g.value[0]+"   "+g.value[1]),1),z,t(C,{modelValue:w.value,"onUpdate:modelValue":N[0]||(N[0]=o=>w.value=o),accordion:""},{default:e(()=>[(c(!0),d(m,null,y(j.value,(o,h)=>(c(),x(V,{name:h},{title:e(()=>[a(n(o.term),1)]),default:e(()=>[o.sublist.length==0?(c(),d("div",A," No Course ")):(c(),d("div",H,[t(f,{style:{"margin-top":"15px"}},{default:e(()=>[t(s,{span:3,class:"center"},{default:e(()=>[a("序号")]),_:1}),t(s,{span:3,class:"center"},{default:e(()=>[a("课程")]),_:1}),t(s,{span:3,class:"center"},{default:e(()=>[a("分数")]),_:1}),t(s,{span:3,class:"center"},{default:e(()=>[a("学分")]),_:1}),t(s,{span:3,class:"center"},{default:e(()=>[a("学时")]),_:1}),t(s,{span:3,class:"center"},{default:e(()=>[a("课程属性")]),_:1}),t(s,{span:3,class:"center"},{default:e(()=>[a("成绩标识")]),_:1})]),_:1}),(c(!0),d(m,null,y(o.sublist,(r,D)=>(c(),x(f,{style:{"margin-top":"15px"}},{default:e(()=>[t(s,{span:3,class:"center"},{default:e(()=>[a(n(D+1),1)]),_:2},1024),t(s,{span:3,class:"center"},{default:e(()=>[a(n(r.course),1)]),_:2},1024),t(s,{span:3,class:"center"},{default:e(()=>[a(n(r.score),1)]),_:2},1024),t(s,{span:3,class:"center"},{default:e(()=>[a(n(r.credit),1)]),_:2},1024),t(s,{span:3,class:"center"},{default:e(()=>[a(n(r.time),1)]),_:2},1024),t(s,{span:3,class:"center"},{default:e(()=>[a(n(r.type),1)]),_:2},1024),t(s,{span:3,class:"center"},{default:e(()=>[a(n(r.status),1)]),_:2},1024)]),_:2},1024))),256))]))]),_:2},1032,["name"]))),256)),t(V,{name:i.value,title:p.value.term},{default:e(()=>[S.value==0?(c(),d("div",J," No Course ")):(c(),d("div",K,[t(f,{style:{"margin-top":"15px"}},{default:e(()=>[t(s,{span:4,class:"center"},{default:e(()=>[a("序号")]),_:1}),t(s,{span:4,class:"center"},{default:e(()=>[a("开课学期")]),_:1}),t(s,{span:4,class:"center"},{default:e(()=>[a("课程名称")]),_:1}),t(s,{span:4,class:"center"},{default:e(()=>[a("成绩")]),_:1}),t(s,{span:4,class:"center"},{default:e(()=>[a("备注")]),_:1})]),_:1}),(c(!0),d(m,null,y(p.value.sublist,(o,h)=>(c(),x(f,{style:{"margin-top":"15px"}},{default:e(()=>[t(s,{span:4,class:"center"},{default:e(()=>[a(n(h+1),1)]),_:2},1024),t(s,{span:4,class:"center"},{default:e(()=>[a(n(o.time),1)]),_:2},1024),t(s,{span:4,class:"center"},{default:e(()=>[a(n(o.course),1)]),_:2},1024),t(s,{span:4,class:"center"},{default:e(()=>[a(n(o.score),1)]),_:2},1024),t(s,{span:4,class:"center"},{default:e(()=>[a(n(o.platform),1)]),_:2},1024)]),_:2},1024))),256))]))]),_:1},8,["name","title"])]),_:1},8,["modelValue"]),L(k("div",O,null,512),[[I,b.value]])],64)}}},R=E(P,[["__scopeId","data-v-900506c9"]]);export{R as default};
