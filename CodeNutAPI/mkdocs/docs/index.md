# <center>Welcome to CodeNut API</center>

---

本 API 使用 RESTful 风格编写， [《RESTful API 设计指南》](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)，[《RESTful API 设计最佳实践》](https://www.oschina.net/translate/best-practices-for-a-pragmatic-restful-api)。

网址：[api.txdna.cn](http://api.txdna.cn)

返回格式注：

```json
# 所有成功格式都与下方类似，result 为数组形式
{
  "msg": "ok", 
  "result": [
    {
    ...
    }
  ]
}

# 失败
{"msg": "no", "error": "xx"}
```

---

## 用户

|          资源          |          说明     |
|-----------------------|-------------------|
|   [/tokens](#tokens)  |       登录、注销    |
|   [/users](#users)    |       用户操作     |

|          角色名称      |            权限                          |
|-----------------------|------------------------------------------|
|   user（默认）         |       编程 & 评论 & 写文章                 |
|   moderator           |       编程 & 评论 & 写文章 & 管理用户评论   |
|   sponsor             |       编程 & 评论 & 写文章 & 举办比赛       |
|   administrator       |              全部                         |

---

### tokens

1. [登录](#登录)

2. [注销](#注销)

---

##### [<font color=#FF0000 id="登录">登录</font> POST `/tokens`](#tokens)

|  请求参数    |        格式      |     必选    |         说明    |
|-------------|-----------------|-------------|----------------|
|   username  |       json      |     yes     |       用户名    |
|   password  |       json      |     yes     |       密码      |
|   duration  |       json      |     no      |   token有效期（默认5小时） |

|   返回值     |         说明          |
|-------------|-----------------------|
|   duration  |      token有效期       |
|   id        |     哈希过的id（下同）  |
|   token     |        token          |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
    "duration": 18000,
    "id": "GG", 
    "token": "eyJleHAiOjE1MDYzNTQzNzIsImFsZyI6IkhTMjU2IiwiaWF0IjoxNTA2MzM2MzcyfQ.eyJpZCI6Mn0.J-JTOcN4LVtWfH9pq15h4lWp_bLxBGnK_CV6Ptxw7S8"
  	}
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "login error"}
```

<br />

##### [<font color=#FF0000 id="注销">注销</font> DELETE `/tokens`](#tokens)

|  请求参数    |        格式      |     必选    |         说明    |
|-------------|-----------------|-------------|----------------|
|  无 |

* 成功返回值

```json
{"msg": "ok"}
```

---

### users

1. [创建用户](#创建用户)

2. [修改用户资料](#修改用户资料)

3. [修改用户密码](#修改用户密码)

4. [修改用户角色](#修改用户角色)

6. [修改用户头像](#修改用户头像) 

7. [删除用户](#删除用户)

8. [得到所有用户信息](#得到所有用户信息)

9. [得到具体用户信息](#得到具体用户信息)

10. [得到用户参加的所有比赛](#得到用户参加的所有比赛)

11. [得到用户举办的所有比赛](#得到用户举办的所有比赛)

12. [得到用户提交的程序](#得到用户提交的程序)

13. [得到用户收藏的题目](#得到用户收藏的题目)

---

##### [<font color=#FF0000 id="创建用户">创建用户</font> POST `/users`](#users)

|  请求参数    |        格式      |     必选    |       说明     |
|-------------|-----------------|-------------|---------------|
|   email     |       json      |     yes     |      邮箱      |
|   username  |       json      |     yes     |      用户名    |
|   password  |       json      |     yes     |      密码     |

|   返回值     |         说明          |
|-------------|-----------------------|
|   duration  |      token有效期       |
|   id        |         id            |
|   token     |        token          |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
    "duration": 18000,
    "id": "GG", 
    "token": "eyJleHAiOjE1MDYzNTQzNzIsImFsZyI6IkhTMjU2IiwiaWF0IjoxNTA2MzM2MzcyfQ.eyJpZCI6Mn0.J-JTOcN4LVtWfH9pq15h4lWp_bLxBGnK_CV6Ptxw7S8"
  	}
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "missing arguments, require: email, username, password"}
{"msg": "no", "error": "email format wrong"}
{"msg": "no", "error": "username: xx is already existed"}
{"msg": "no", "error": "email: xx is already existed"}
```

<br />

##### [<font color=#FF0000 id="修改用户资料">修改用户资料</font> PUT `/users/info`](#users)

|  请求参数    |        格式     |     必选    |       说明        |
|-------------|-----------------|------------|-------------------|
|   realname  |       json      |     no     |      真名         |
|   profile   |       json      |     no     |      头像存储地址  |
|   school    |       json      |     no     |      学校         |
|   about_me  |       json      |     no     |      关于我       |
|   tag       |       json      |     no     |      用户标签     |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值（出现不同于上述请求的参数）

```json
{"msg": "no", "error": "can not modify"}
```

<br />

##### [<font color=#FF0000 id="修改用户密码">修改用户密码</font> PUT `/users/password`](#users)

|  请求参数      |        格式     |     必选    |       说明        |
|---------------|-----------------|------------|-------------------|
|   oldpassword |       json      |     yes     |      旧密码      |
|   newpassword |       json      |     yes     |      新密码      |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "can not modify"}
{"msg": "no", "error": "old password not correct"}
```

<br />

##### [<font color=#FF0000 id="修改用户头像">修改用户头像</font> PUT `/users/profile`](#users)

|  请求参数    |        格式     |     必选    |       说明        |
|-------------|-----------------|------------|-------------------|
|   无（功能暂时无法使用）     |

* 成功返回值

```json
{"msg": "ok"}
```

<br />

##### [<font color=#FF0000 id="修改用户角色">修改用户角色</font> PUT `/users/<id>/role`（管理员权限）](#users)

|  请求参数      |        格式     |     必选    |       说明        |
|---------------|-----------------|------------|-------------------|
|   role        |       json      |     yes    |      角色名称      |

* 成功返回值

```json
{"msg": "ok"}
```

<br />

##### [<font color=#FF0000 id="删除用户">删除用户</font> DELETE `/users/<id>`（管理员权限）](#users)

|  请求参数      |        格式     |     必选    |       说明        |
|---------------|-----------------|------------|-------------------|
|  无      |

* 成功返回值

```json
{"msg": "ok"}
```

<br />

##### [<font color=#FF0000 id="得到所有用户信息">得到所有用户信息</font> GET `/users`（管理员权限）](#users)

|  请求参数      |        格式     |     必选    |           说明          |
|---------------|-----------------|------------|-------------------------|
|   page        |       string      |     no    |      页码（默认1）      |
|   per_page    |       string      |     no    |      每页限制（默认20） |

|    返回值       |         说明          |
|----------------|-----------------------|
|   about_me     |         关于我         |
|   accept_nums  |       编程通过数       |
|   create_time  |        注册时间        |
|   login_time   |        登陆时间        |
|   profile      |        头像存储地址    |
|   realname     |        真实姓名        |
|   school       |        学校            |
|   submit_nums  |        编程提交数      |
|   user_id      |        用户id          |
|   username     |        用户名          |
|   tag          |        标签           |
|   role         |        角色名称        |


* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "about_me": null, 
      "accept_nums": 0, 
      "create_time": "Mon, 25 Sep 2017 07:06:42 GMT", 
      "login_time": "Mon, 25 Sep 2017 07:06:42 GMT", 
      "profile": null, 
      "realname": "moderator", 
      "school": null, 
      "submit_nums": 0, 
      "user_id": "aG", 
      "username": "moderator",
	  "tag": "aa,bb",
	  "role": "moderator"
    }, 
    ......
  ]
}
```

<br />

##### [<font color=#FF0000 id="得到具体用户信息">得到具体用户信息</font> GET `/users/<id>`](#users)

|  请求参数      |        格式     |     必选    |           说明          |
|---------------|-----------------|------------|-------------------------|
|   无      |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "about_me": null, 
      "accept_nums": 2, 
      "create_time": "Mon, 25 Sep 2017 07:06:42 GMT", 
      "login_time": "Mon, 25 Sep 2017 07:06:42 GMT", 
      "profile": null, 
      "realname": "user", 
      "school": null, 
      "submit_nums": 2, 
      "user_id": "o6", 
      "username": "user",
	  "tag": "aa,bb",
	  "role": "user"
    }
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "user doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到用户参加的所有比赛">得到用户参加的所有比赛</font> GET `/users/<id>/contests_joined`](#users)

|  请求参数      |        格式     |     必选    |           说明          |
|---------------|-----------------|------------|-------------------------|
|   无      |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "auto_approve": true, 
      "description": "tYn6j78Mwap91HB3Of4IzkUSvRZLmhKAisruD0qlbWVXQPTcgx", 
      "end_time": "Wed, 20 Sep 2017 06:02:18 GMT", 
      "id": "6L", 
      "sponsor": "administrator", 
      "start_time": "Sun, 20 Aug 2017 06:02:18 GMT", 
      "title": "w4Dp2o9U", 
      "user_nums": 0
    }, 
    ......
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "user doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到用户举办的所有比赛">得到用户举办的所有比赛</font> GET `/users/<id>/contests_sponsor`](#users)

|  请求参数      |        格式     |     必选    |           说明          |
|---------------|-----------------|------------|-------------------------|
|   无      |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "auto_approve": true, 
      "description": "KlPv1dCiVMSBwLjaZkFxpDcy7fEqQTW49sAXnbOgeU5h2oGHrY", 
      "end_time": "Fri, 15 Sep 2017 06:02:18 GMT", 
      "id": "Mb", 
      "sponsor": "administrator", 
      "start_time": "Tue, 15 Aug 2017 06:02:18 GMT", 
      "title": "5ZuU6VN2", 
      "user_nums": 0
    }, 
    ......
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "user doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到用户提交的程序">得到用户提交的程序</font> GET `/users/<id>/codes_submitted`](#users)

|  请求参数      |        格式     |     必选    |           说明          |
|---------------|-----------------|------------|-------------------------|
|   无      |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "code_id": "xs", 
      "create_time": "Tue, 26 Sep 2017 01:39:03 GMT", 
      "language": "Python3", 
      "memory_used": 45523.0, 
      "problem_id": "nA", 
      "status": "Accepted", 
      "time_used": 1000.0, 
      "update_time": null, 
      "user_id": "o6"
    }, 
    ......
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "user doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到用户收藏的题目">得到用户收藏的题目</font> GET `/users/<id>/collections`](#users)

|  请求参数      |        格式     |     必选    |           说明          |
|---------------|-----------------|------------|-------------------------|
|   无     |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "problem": "title", 
      "problem_id": "xj", 
      "user_id": "o6", 
      "username": "user"
    }, 
    ......
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "user doesn't exist"}
```

---

## 题目

|          资源                   |          说明          |
|---------------------------------|-----------------------|
|   [/problems](#problems)        |       题目操作         |
|   [/problems](#users_problems)  |       用户题目操作     |

---

### problems

1. [得到所有题目信息](#得到所有题目信息)

2. [得到题目信息](#得到题目信息)

3. [得到题目解决方法](#得到题目解决方法)

4. [修改题目解决方法](#修改题目解决方法)

5. [创建题目](#创建题目)

6. [修改题目](#修改题目)

7. [删除题目](#删除题目)

8. [得到程序模版](#得到程序模版)

9. [运行代码](#运行代码)

10. [提交代码](#提交代码)

---

##### [<font color=#FF0000 id="得到所有题目信息">得到所有题目信息</font> GET `/problems`](#problems)

|  请求参数      |        格式     |     必选    |           说明             |
|---------------|-----------------|------------|----------------------------|
|   page        |       string      |     no    |      页码（默认1）         |
|   per_page    |       string      |     no    |      每页限制（默认20）     |
|   contest_id  |       string      |     no    |      所属比赛id（默认None） |

|    返回值       |         说明          |
|----------------|-----------------------|
|   accepted     |         通过该题人数    |
|   submitted    |         提交代码的人数  |
|   id           |         题目id         |
|   level        |         难度等级       |
|   like_nums    |         赞            |
|   hate_nums    |         倒            |
|   tag          |         标签          |
|   title        |         标题          |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "accepted": 0, 
      "hate_nums": 0, 
      "id": "Meq", 
      "level": 3, 
      "like_nums": 0, 
      "submitted": 0, 
      "tag": "YwTo", 
      "title": "W8CpyiJq"
    }, 
    ......
  ]
}
```

<br />

##### [<font color=#FF0000 id="得到题目信息">得到题目信息</font> GET `/problems/<id>`](#problems)

|  请求参数      |        格式     |     必选    |           说明             |
|---------------|-----------------|------------|----------------------------|
|   无 |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "accepted": 0, 
      "description": "sjXmTEM4kYG17Qq69K0VgLISChadlDpniP2boRcNtZAxJf85BF", 
      "hate_nums": 0, 
      "id": "Meq", 
      "level": 3, 
      "like_nums": 0, 
      "submitted": 0, 
      "tag": "YwTo", 
      "title": "W8CpyiJq"
    }
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "problem doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到题目解决方法">得到题目解决方法</font> GET `/problems/<id>/solutions`](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   无   |

|    返回值       |         说明          |
|----------------|-----------------------|
|   solution     |         解决方法       |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
    "solution": "K2O8eZMo7GgrbJTQN5H4wyDax6tCzmjdVnf19iB3UALvIq0Slp"
    }
  ]
}
```

<br />

##### [<font color=#FF0000 id="修改题目解决方法">修改题目解决方法</font> PUT `/problems/<id>/solutions`（题目所有者）](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   solution      |       json      |     yes    |      解决办法            |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "do not modify other sponsor's solution"}
```

<br />

##### [<font color=#FF0000 id="创建题目">创建题目</font> POST `/problems/<id>/solutions`（举办比赛权限）](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   title         |       json      |     yes    |      标题             |
|   description   |       json      |     yes    |      描述             |
|   level         |       json      |     yes    |      难度             |
|   tag           |       json      |     yes    |      标签             |
|   code          |       json      |     yes    |      程序模板         |

|    返回值       |         说明          |
|----------------|-----------------------|
|   id           |         题目id        |
|   title        |         标题          |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "id": "zaa", 
      "title": "test"
    }
  ]
}
```

<br />

##### [<font color=#FF0000 id="修改题目">修改题目</font> PUT `/problems/<id>`（题目所有者）](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   title         |       json      |     no    |      标题             |
|   description   |       json      |     no    |      描述             |
|   level         |       json      |     no    |      难度             |
|   tag           |       json      |     no    |      标签             |
|   code          |       json      |     no    |      程序模板         |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "do not modify other sponsor's problem"}
{"msg": "no", "error": "update error"}
{"msg": "no", "error": "title: xx is already existed"}
```

<br />

##### [<font color=#FF0000 id="删除题目">删除题目</font> DELETE `/problems/<id>`（题目所有者）](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   无     |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "do not delete other sponsor's problem"}
{"msg": "no", "error": "problem doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到程序模版">得到程序模版</font> GET `/problems/<id>/codes`](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   无   |

|    返回值       |         说明          |
|----------------|-----------------------|
|   code         |         程序模版       |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "code": "h2O7F0utCVLfbM8pUy3P"
    }
  ]
}
```

<br />

##### [<font color=#FF0000 id="运行代码">运行代码</font> PATCH `/problems/<id>/codes`（编程权限）](#problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   language      |       json      |     yes    |         编程语言         |
|   code          |       json      |     yes    |           代码          |
|   custom_input  |       json      |     no     |       用户自定义输入     |

|    返回值       |         说明          |
|----------------|-----------------------|
|   memory_used  |         耗费内存       |
|   output       |         程序输出       |
|   status       |         运行状态       |
|   time_used    |         耗费时间       |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "memory_used": 0.7620915240518614, 
      "output": "test", 
      "status": "Memory Limit Exceeded", 
      "time_used": 0.7325701808735701
    }
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "just require: language code custom_input"}
```

<br />

##### [<font color=#FF0000 id="提交代码">提交代码</font> POST `/problems/<id>/codes`（编程权限）](#problems)

```json
与运行代码一致
```

> 目前沙箱还没完成，运行代码和提交代码的接口都是随机产生的值

### users_problems

1. [用户记笔记](#用户记笔记)

2. [得到用户笔记](#得到用户笔记)

3. [用户收藏题目](#用户收藏题目)

4. [用户取消收藏](#用户取消收藏)

5. [用户点赞](#用户点赞)

---

##### [<font color=#FF0000 id="用户记笔记">用户记笔记</font> PUT `/problems/<id>/notes`（编程权限）](#users_problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   text          |       json      |     yes    |    笔记（需要检查不为空） |

* 成功返回值

```json
{"msg": "ok"}
```

<br />

##### [<font color=#FF0000 id="得到用户笔记">得到用户笔记</font> GET `/problems/<id>/notes`（编程权限）](#users_problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   无  |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "text": "xx"
    }
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "note doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="用户收藏题目">用户收藏题目</font> POST `/problems/<id>/collections`（编程权限）](#users_problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   空   |

* 成功返回值

```json
{"msg": "ok"}
```

<br />

##### [<font color=#FF0000 id="用户取消收藏">用户取消收藏</font> DELETE `/problems/<id>/collections`（编程权限）](#users_problems)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   空   |

* 成功返回值

```json
{"msg": "ok"}
```

<br />

##### [<font color=#FF0000 id="用户点赞">用户点赞/倒/无感</font> PUT `/problems/<id>/likes`（编程权限）](#users_problems)

|        请求参数            |        格式       |     必选    |                 说明                     |
|---------------------------|-------------------|------------|------------------------------------------|
|   true_or_false_or_none   |       string      |     yes    |   true: like, false: hate, none: no feel |

* 成功返回值

```json
{"msg": "ok"}
```

## 比赛

|          资源                   |          说明          |
|---------------------------------|-----------------------|
|   [/contests](#contests)        |       比赛操作         |
|   [/contests](#users_contests)  |       用户比赛操作     |

---

### contests

1. [创建比赛](#创建比赛)

2. [更新比赛信息](#更新比赛信息)

3. [删除比赛](#删除比赛)

4. [得到所有比赛信息](#得到所有比赛信息)

5. [得到具体比赛信息](#得到具体比赛信息)

6. [得到所以参赛者](#得到所以参赛者)

7. [批准参赛](#批准参赛)

---

##### [<font color=#FF0000 id="创建比赛">创建比赛</font> POST `/contests`（举办比赛权限）](#contests)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   title         |       json      |     yes    |       标题              |
|   description   |       json      |     yes    |       描述              |
|   start_time    |       json      |     yes    |       开始时间           |
|   end_time      |       json      |     yes    |       结束时间           |
|   auto_approve  |       json      |     no     |       自动批准用户加入（默认自动） |
|   password      |       json      |     no     |       比赛密码（默认为空） |

|    返回值       |         说明          |
|----------------|-----------------------|
|   auto_approve  |         自动批准用户加入  |
|   description   |         描述             |
|   end_time      |         开始时间         |
|   start_time    |         结束时间          |
|   id            |         比赛id           |
|   sponsor       |         举办方名字       |
|   title         |         标题             |
|   user_nums     |         参加者人数       |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "auto_approve": true, 
      "description": "test", 
      "end_time": "2017-11-25 07:24:41", 
      "id": "dx", 
      "sponsor": "administrator", 
      "start_time": "2017-09-25 07:24:41", 
      "title": "test", 
      "user_nums": 0
    }
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "just require: title description start_time end_time auto_approve password"}
```

<br />

##### [<font color=#FF0000 id="更新比赛信息">更新比赛信息</font> PUT `/contests/<id>`（比赛所有者）](#contests)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   title         |       json      |     no     |       标题              |
|   description   |       json      |     no     |       描述              |
|   start_time    |       json      |     no     |       开始时间           |
|   end_time      |       json      |     no     |       结束时间           |
|   auto_approve  |       json      |     no     |       自动批准用户加入（默认自动） |
|   password      |       json      |     no     |       比赛密码（默认为空） |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "do not modify other sponsor's contest"}
{"msg": "no", "error": "just require: title description start_time end_time auto_approve password"}
{"msg": "no", "error": "update error"}
```

<br />

##### [<font color=#FF0000 id="删除比赛">删除比赛</font> DELETE `/contests/<id>`（比赛所有者）](#contests)

|    请求参数      |        格式     |     必选    |           说明          |
|-----------------|-----------------|------------|-------------------------|
|   空  |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "do not delete other sponsor's contest"}
{"msg": "no", "error": "contest doesn't exist"}
```

<br />

##### [<font color=#FF0000 id="得到所有比赛信息">得到所有比赛信息</font> GET `/contests`](#contests)

|  请求参数      |        格式     |     必选    |           说明             |
|---------------|-----------------|------------|----------------------------|
|   page        |       string      |     no    |      页码（默认1）         |
|   per_page    |       string      |     no    |      每页限制（默认20）     |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "auto_approve": true, 
      "description": "UsHG0FxwqrLofj5OhvBN3KDdAc7ETnm9pWSZMCX8RiQPytJuek", 
      "end_time": "Fri, 22 Sep 2017 06:02:18 GMT", 
      "id": "GG", 
      "sponsor": "administrator", 
      "start_time": "Tue, 12 Sep 2017 06:02:18 GMT", 
      "title": "dQIFUpcl", 
      "user_nums": 0
    }, 
	......
  ]
}
```

<br />

##### [<font color=#FF0000 id="得到具体比赛信息">得到具体比赛信息</font> GET `/contests/<id>`](#contests)

|  请求参数      |        格式     |     必选    |           说明             |
|---------------|-----------------|------------|----------------------------|
|   无     |

|    返回值       |         说明          |
|----------------|-----------------------|
|   is_join      |    用户是否已加入比赛（null: 没加入，true: 已加入，false: 拒绝加入）   |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "auto_approve": true, 
      "description": "DUKw58N620axWsvonMSbJipIRBjOdCtAeY3kL9VuXf4zZGQmFy", 
      "end_time": "Thu, 21 Sep 2017 06:02:18 GMT", 
      "id": "o6", 
	  "is_join": null,
      "sponsor": "administrator", 
      "start_time": "Mon, 11 Sep 2017 06:02:18 GMT", 
      "title": "AnDSxRib", 
      "user_nums": 0
    }
  ]
}
```

<br />

##### [<font color=#FF0000 id="得到所以参赛者">得到所以参赛者</font> GET `/contests/<id>/users`](#contests)

|  请求参数      |        格式     |     必选    |           说明             |
|---------------|-----------------|------------|----------------------------|
|   page        |       string      |     no    |      页码（默认1）         |
|   per_page    |       string      |     no    |      每页限制（默认20）     |
|   is_join     |       string      |     no    |      批准参赛（默认True） |

|    返回值       |         说明          |
|----------------|-----------------------|
|   is_join      |         批准参赛       |
|   user         |         用户名         |
|   user_id      |         用户id        |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "is_join": true, 
      "user": "administrator", 
      "user_id": "GG"
    },
	......
  ]
}
```

<br />

##### [<font color=#FF0000 id="批准参赛">批准参赛</font> PUT `/contests/<id>/users`（比赛所有者）](#contests)

|  请求参数      |        格式     |     必选    |           说明             |
|---------------|-----------------|------------|----------------------------|
|   user_id     |       json      |     yes    |            用户id          |

|    返回值       |         说明          |
|----------------|-----------------------|
|   is_join      |         目前参赛情况   |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "is_join": true, 
    }
  ]
}
```

---

### users_contests

1. [加入比赛](#加入比赛)

2. [退出比赛](#退出比赛)

---

##### [<font color=#FF0000 id="加入比赛">加入比赛</font> POST `/contests/<id>/users`（编程权限）](#users_contests)

|  请求参数      |        格式     |     必选    |           说明                     |
|---------------|-----------------|------------|------------------------------------|
|   password    |       json      |     yes    |       比赛密码（为空时也要发null）    |

|    返回值       |         说明          |
|----------------|-----------------------|
|   is_join      |         是否成功参赛   |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      "is_join": true, 
    }
  ]
}
```

* 失败返回值

```json
{"msg": "no", "error": "password wrong"}
```

<br />

##### [<font color=#FF0000 id="退出比赛">退出比赛</font> DELETE `/contests/<id>/users`（已加入比赛者）](#users_contests)

|  请求参数      |        格式     |     必选    |           说明                     |
|---------------|-----------------|------------|------------------------------------|
|   无    |

* 成功返回值

```json
{"msg": "ok"}
```

* 失败返回值

```json
{"msg": "no", "error": "out contest wrong"}
```

## 搜索

|          资源                   |          说明          |
|---------------------------------|-----------------------|
|   [/search](#search)            |       搜索操作         |

---

### search

##### [<font color=#FF0000 id="搜索">搜索</font> POST `/search`](#search)

|  请求参数      |        格式     |     必选    |                     说明                      |
|---------------|-----------------|------------|-----------------------------------------------|
|   target      |       json      |     yes    |       查询对象（User，Problem等，对应数据库模型）|
|   type        |       json      |     yes    |       模型属性（usrname，title等）             |
|   content     |       json      |     yes    |       查询内容                                 |

* 成功返回值

```json
{
  "msg": "ok", 
  "result": [
    {
      ......
    }
  ]
}
```