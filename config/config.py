# coding=utf-8

login_url="http://cms.duoceshi.cn/cms/manage/loginJump.do"
login_headers={"Content-Type": "application/x-www-form-urlencoded"}
login_data={"userAccount": "admin",
            "loginPwd": "123456"}


query_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
query_headers={"Content-Type": "application/x-www-form-urlencoded"}
query_data={"startCreateDate":"",
            "endCreateDate":"",
            "searchValue":"",
            "page": 1}


saveuser_url="http://cms.duoceshi.cn/cms/manage/saveSysUser.do"
saveuser_data={ "id":"",
                "userName":"ddddd",
                "userSex":1,
                "userMobile":"13012345678",
                "userEmail":"13012345678@qq.com",
                "userAccount":"13012345678",
                "loginPwd":"13012345678",
                "confirmPwd":"13012345678"}


