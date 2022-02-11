# coding=utf-8

login_url="http://cms.duoceshi.cn/cms/manage/loginJump.do"
login_data={"userAccount": "admin",
            "loginPwd": "123456"}


query_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
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


findtext_url="http://cms.duoceshi.cn/cms/manage/findCategoryByPage.do"
findtext_data={"parentId":5,
               "categoryName":"",
               'page':1}

savetext_url="http://cms.duoceshi.cn/cms/manage/saveModuleCategory.do"
savetext_data={"id":"",
                "categoryName":"1656123132",
                "parentId":5,
                "parentId":"",
                "categoryCode":"4651212",
                "categoryDesc":"5+6+24651",
                "keyTitle":"46551",
                "keyWords":"456231",
                "keyDesc":"45612"}

deluser_url="http://cms.duoceshi.cn/cms/manage/deleteByIds.do"
deluser_data={"ids":125967}

deltext_url="http://cms.duoceshi.cn/cms/manage/deleteCategoryByIds.do"
deltext_data={"ids":1665}



