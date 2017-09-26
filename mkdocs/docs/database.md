# <center>Database</center>

---

update later

---

### User

1. [用户](#users)

2. [用户信息](#user_infos)

---

#####  [<font color=#FF0000 id="users">users</font>](#User)

|      字段      |     格式         | 说明                  |
| ------------- |------------------| ----------------------|
| id            | int(11)          | 用户ID                 |
| email         | varchar(64)      | 邮箱 （唯一）          |
| password      | varchar(256)     | 密码                   |
| username      | varchar(32)      | 用户名（不可更改，唯一） |

---

##### [<font color=#FF0000 id="user_infos">user_infos</font>](#User)

|      字段      |     格式         | 说明                  |
| ------------- |------------------| ----------------------|
| realname   | varchar(32)  | 真名 |
| profile    | varchar(256) | 头像图片地址 |
| school     | varchar(64)  | 毕业学校 |
| about_me   | text         | 关于我 |

---

### Problem

1. [题目信息](#problems)

---

##### problems

|      字段      |     格式         | 说明                  |
| ------------- |------------------| ----------------------|
| id         | int(11)      | 题号 |
| title      | varchar(128)  | 标题 |
| description   | text | 题目描述 |
| level   |  int(11) | 难度 |
| tag   | varchar(128)  | 标签 |
| accepted    | int(11) | 通过数 |
| submitted | int(11) | 提交数 |
| template     | text  | 模版代码 |
| solution     | text  | 解决方法 |