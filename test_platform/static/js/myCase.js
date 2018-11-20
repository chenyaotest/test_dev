// 获取指定case_id的用例信息
let CaseInit = function (case_id) {

    function getCaseInfo() {
        // 调用获取用例信息接口
        $.post("/interface/get_case_info/", {"caseId": case_id},
            function (resp) {
                if (resp.success === "true") {
                    let result = resp.data;
                    //window.alert("hello")
                    console.log("结果", result);
                    document.getElementById("req_name").value = result.name;
                    document.getElementById("req_url").value = result.url;
                    document.getElementById("req_header").value = result.req_header;
                    document.getElementById("req_parameter").value = result.req_parameter;

                    if (result.req_method == "post") {
                        document.getElementById("post").setAttribute("checked", "")
                    }
                    if (result.req_type == "json") {
                            document.getElementById("json").setAttribute("checked", "")
                        }
                        // 初始化菜单
                        ProjectInit('project_name', 'module_name', result.project_name, result.module_name);
                    }


                    else{window.alert("用例ID不存在！")}

                        //项目列表和模块列表的二级联动
                    ProjectInit('project_name', 'module_name');

            });
    }
    // 调用getCaseInfo函数
    getCaseInfo();

}
