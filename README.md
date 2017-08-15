# API使用手册

## RESTful API

本 API 使用 RESTful API 风格编写，详情可以看看阮一峰的文章 [《RESTful API 设计指南》](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)。

网址：[api.txdna.cn](api.txdna.cn)

## 题目 problems

**数据库字段**

| 字段        | 类型         | 说明     |
| ---------- |------------:| :--------:|
| id         | int(11)      | 题号 |
| title      | varchar(128)  | 标题 |
| description   | text | 题目描述 |
| level   |  int(11) | 难度 |
| tag   | varchar(128)  | 标签 |
| accepted    | int(11) | 通过数 |
| submitted | int(11) | 提交数 |
| solution     | text  | 解决方法 |

**请求方法**

| 请求 | 后缀 | 说明 | Json格式 |
| ---- |----:| :------:| :------:|
| GET | /problems | 列出所有题目 | 无 |
| GET | /problems?page=xx&per_page=xx | 分页（page：页码，per_page：每页内容数量）                  | 无 |
| POST | /problems | 新建题目 | 必要参数{"title":"x", "description":"x", "level":"x", "tag":"x"} |
| GET | /problems/ID | 获取某个指定题目的信息 | 无 |
| PUT | /problems/ID | 更新某个指定题目的信息 | 除了 id 的任意参数（如{"title":"x", "description":"x"}） |
| DELETE | /problems/ID | 删除某个题目 | 无 |

**示例**

使用 Linux 下的 `curl` 命令，**分页列出题目**：

```bash
$ curl -i -X GET http://api.txdna.cn/problems?page=1&per_page=20
HTTP/1.1 200 OK
Server: nginx/1.13.4
Date: Tue, 15 Aug 2017 12:51:53 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 3684
Connection: keep-alive
Access-Control-Allow-Origin: *

[{"_sa_instance_state": null, "title": "Two Sum", "submitted": 0, "level": 1, "tag": "Array,Hash Table", "solution": null, "accepted": 0, "description": null, "id": 499}, ... ,{"_sa_instance_state": null, "title": "Add Two Numbers", "submitted": 0, "level": 2, "tag": "Linked List,Math", "solution": null, "accepted": 0, "description": null, "id": 498}]
```

**新建题目**（需要登录）：

```bash
curl -u admin:admin -i -H "Content-Type: application/json" -X POST -d '{"title":"test", "description":"test", "level":"1", "tag":"array"}' http://api.txdna.cn/problems
HTTP/1.0 201 CREATED
Content-Type: application/json
Location:http://api.txdna.cn/problems/501 # 头信息中的 Location，可重定向到题目详情
Access-Control-Allow-Origin: *
Content-Length: 38
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:38:21 GMT

{
  "msg": "ok", 
  "title": "test"
}
```

**获取某个指定题目的信息**：

```bash
curl -i -X GET http://api.txdna.cn/problems/1                           
HTTP/1.0 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 31105
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:43:30 GMT

{
  "_sa_instance_state": null,  # 无用字段
  "accepted": 0, 
  "description": ...,
  "id": 1, 
  "level": 2, 
  "solution": ...,
  "submitted": 0, 
  "tag": "Tree", 
  "title": "Print Binary Tree"
}
```

**更新某个指定题目的信息**（需要登录）：

```bash
curl -u admin:admin -i -H "Content-Type: application/json" -X PUT -d '{"title":"test modify"}' http://api.txdna.cn/problems/501
HTTP/1.0 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 19
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:46:16 GMT

{
  "msg": "yes"
}
```

**删除某个题目**（需要登录）：

```bash
curl -u admin:admin -i -X DELETE http://api.txdna.cn/problems/501       
HTTP/1.0 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 19
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:47:23 GMT

{
  "msg": "yes"
}
```

## 用户 users

**数据库字段**

| 字段  | 类型         | 说明                  |
| ----- |-----:| :--------------------:|
| id         | int(11)      | 用户ID |
| email      | varchar(64)  | 邮箱（不可更改）|
| password   | varchar(256) | 密码|
| username   | varchar(32)  | 用户名（不可更改）|
| realname   | varchar(32)  | 真名 |
| profile    | varchar(256) | 头像图片地址 |
| occupation | varchar(128) | 职业 |
| school     | varchar(64)  | 毕业学校 |
| company    | varchar(64)  | 公司 |
| about_me   | text         | 关于我 |
| blog       | varchar(64)  | 博客地址 |
| role       | int(11)      | 权限等级（0，1，2，3）|

**请求方法**

| 请求 | 后缀 | 说明 | Json格式 |
| ---- |----:| :------:| :------:|
| GET | /users | 列出所有用户 | 无 |
| GET | /users?page=xx&per_page=xx | 分页（page：页码，per_page：每页内容数量）                  | 无 |
| POST | /users | 新建用户 | 必要参数{"email":"x", "password":"x", "username":"x"} |
| GET | /users/ID | 获取某个指定用户的信息 | 无 |
| PUT | /users/ID | 更新某个指定用户的信息 | 除了 id email username 的任意参数（如{"realname":"x", "school":"x"}） |
| DELETE | /users/ID | 删除某个用户 | 无 |

**分页列出用户**（需要登录）：

```bash
curl -u admin:admin -i -X GET http://api.txdna.cn/users?page=1&per_page=2
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 565
Access-Control-Allow-Origin: *
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:49:33 GMT

[{"_sa_instance_state": null, "email": "admin1@qq.com", "profile": null, "blog": null, "school": null, "about_me": null, "occupation": null, "role": null, "password": null, "username": "admin1", "realname": null, "id": 2, "company": null}, {"_sa_instance_state": null, "email": "admin@qq.com", "profile": "https://www.tupianku.com/view/large/13862/640.jpeg", "blog": "https://github.com", "school": "wyu", "about_me": "Code Nut admin", "occupation": "student", "role": null, "password": null, "username": "admin", "realname": "admin", "id": 1, "company": "anchor"}]
```

**新建用户**：

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"username":"admin","password":"admin","email":"admin@qq.com"}' http://api.txdna.cn/users
HTTP/1.0 201 CREATED
Content-Type: application/json
Location: http://api.txdna.cn/users/2 # 头信息中的 Location，可重定向到用户详情
Access-Control-Allow-Origin: *
Content-Length: 72
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:07:21 GMT

{
  "email": "admin@qq.com", 
  "msg": "ok", 
  "username": "admin"
}
```

**获取某个指定用户的信息**（需要登录）：

```bash
curl -u admin:admin -i -X GET  http://api.txdna.cn/users/1
HTTP/1.0 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 362
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:52:24 GMT

{
  "_sa_instance_state": null, 
  "about_me": "Code Nut admin", 
  "blog": "https://github.com", 
  "company": "anchor", 
  "email": "admin@qq.com", 
  "id": 1, 
  "occupation": "student", 
  "password": null, 
  "profile": "https://www.tupianku.com/view/large/13862/640.jpeg", 
  "realname": "admin", 
  "role": 3, 
  "school": "wyu", 
  "username": "admin"
}
```

**更新某个指定用户的信息**（需要登录）：

```bash
curl -u admin:admin -i -H "Content-Type: application/json" -X PUT -d '{"realname":"test modify"}' http://api.txdna.cn/users/2
HTTP/1.0 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 19
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:53:34 GMT

{
  "msg": "yes"
}
```

**删除某个用户**（需要登录）：

```bash
curl -u admin:admin -i http://api.txdna.cn/users/2
HTTP/1.0 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 19
Server: Werkzeug/0.12.2 Python/3.5.3
Date: Tue, 15 Aug 2017 13:54:12 GMT

{
  "msg": "yes"
}
```

## 搜索

必要参数：Json格式：{'target':'x', 'type':'x', 'content':'x'}

> **关键字说明**
> target：Python 中的 class 类，目前是：题目 Problem 类 和 用户 User 类（首字母大写）。
> type：class 类中的属性，即数据库中的字段。
> content：要搜索的内容。

**示例**

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"target":"Problem","content":"Binary Tree Inorder Traversal","type":"title"}' http://api.txdna.cn/search

HTTP/1.1 200 OK
Server: nginx/1.13.4
Date: Tue, 15 Aug 2017 12:58:15 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 197
Connection: keep-alive
Access-Control-Allow-Origin: *

[{"_sa_instance_state": null, "title": "Binary Tree Inorder Traversal", "submitted": 0, "level": 2, "tag": "Tree,Hash Table,Stack", "solution": null, "accepted": 0, "description": null, "id": 406}]
```
