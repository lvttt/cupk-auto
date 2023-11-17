import { ElMessage } from "element-plus"
export function changePwd(newPwd) {
    fetch("http://localhost:8877/rhmh/changePwd", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "newPassword": newPwd
        }),
    }).then(res=>res.json())
    .then(res=>{
        if(res.code == 1){
            ElMessage({
                type: "success",
                message: "修改成功"
            })
        }else{
            ElMessage({
                type: "error",
                message: "修改失败"
            })
        }
    }).catch(err=>{
        console.log(err);
    })
}