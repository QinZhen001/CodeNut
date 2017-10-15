# <center>Database</center>

--------------------------------------------------------------------------------

## 说明

与 API 有关的所有数据库

--------------------------------------------------------------------------------

## user

1. [角色](#user_roles)
2. [用户](#users)
3. [信息](#user_infos)
4. [通过代码](#user_accept_codes)
5. [提交代码](#user_submit_codes)
6. [收藏的题目](#user_collections)
7. [参加的比赛](#user_join_contests)
8. [点赞的题目](#user_like_problems)
9. [题目下的笔记](#user_notes)

--------------------------------------------------------------------------------

### [<font color="#FF0000" id="user_roles">user_roles</font>](#user)

Field       | Type        | Null | Key | Default | Extra          | Description
----------- | ----------- | ---- | --- | ------- | -------------- | -----------
id          | int(11)     | NO   | PRI | NULL    | auto_increment | id
name        | varchar(64) | YES  | UNI | NULL    |                | 角色名
default     | tinyint(1)  | YES  | MUL | NULL    |                | 是否使用默认权限
permissions | int(11)     | YES  |     | NULL    |                | 权限

### [<font color="#FF0000" id="users">users</font>](#user)

Field         | Type         | Null | Key | Default | Extra          | Description
------------- | ------------ | ---- | --- | ------- | -------------- | -----------
id            | int(11)      | NO   | PRI | NULL    | auto_increment | id
email         | varchar(64)  | NO   | UNI | NULL    |                | 邮箱
username      | varchar(32)  | NO   | UNI | NULL    |                | 用户名
password_hash | varchar(256) | NO   |     | NULL    |                | 密码哈希值
role_id       | int(11)      | YES  | MUL | NULL    |                | 角色id

### [<font color="#FF0000" id="user_infos">user_infos</font>](#user)

Field       | Type         | Null | Key | Default | Extra          | Description
----------- | ------------ | ---- | --- | ------- | -------------- | -----------
id          | int(11)      | NO   | PRI | NULL    | auto_increment | id
user_id     | int(11)      | YES  | MUL | NULL    |                | 用户id
realname    | varchar(32)  | YES  |     | NULL    |                | 真名
profile     | text         | YES  |     | NULL    |                | 头像bas64
school      | varchar(64)  | YES  |     | NULL    |                | 学校
about_me    | varchar(512) | YES  |     | NULL    |                | 关于我
tag         | varchar(128) | YES  |     | NULL    |                | 标签
create_time | datetime     | YES  |     | NULL    |                | 注册时间
login_time  | datetime     | YES  |     | NULL    |                | 最近登录时间

### [<font color="#FF0000" id="user_accept_codes">user_accept_codes</font>](#user)

Field      | Type    | Null | Key | Default | Extra          | Description
---------- | ------- | ---- | --- | ------- | -------------- | -----------
id         | int(11) | NO   | PRI | NULL    | auto_increment | id
user_id    | int(11) | YES  | MUL | NULL    |                | 用户id
problem_id | int(11) | YES  | MUL | NULL    |                | 题号
code       | text    | YES  |     | NULL    |                | 代码

### [<font color="#FF0000" id="user_submit_codes">user_submit_codes</font>](#user)

Field       | Type        | Null | Key | Default | Extra          | Description
----------- | ----------- | ---- | --- | ------- | -------------- | -----------
id          | int(11)     | NO   | PRI | NULL    | auto_increment | id
user_id     | int(11)     | YES  | MUL | NULL    |                | 用户id
problem_id  | int(11)     | YES  | MUL | NULL    |                | 题号
code_id     | int(11)     | YES  | MUL | NULL    |                | 代码id
status      | varchar(64) | NO   |     | NULL    |                | 状态
language    | varchar(64) | NO   |     | NULL    |                | 编程语言
time_used   | float       | NO   |     | NULL    |                | 耗时
memory_used | float       | NO   |     | NULL    |                | 耗内存
create_time | datetime    | YES  |     | NULL    |                | 提交时间
update_time | datetime    | YES  |     | NULL    |                | 更新通过代码时间

### [<font color="#FF0000" id="user_collections">user_collections</font>](#user)

Field      | Type    | Null | Key | Default | Extra          | Description
---------- | ------- | ---- | --- | ------- | -------------- | -----------
id         | int(11) | NO   | PRI | NULL    | auto_increment | id
user_id    | int(11) | YES  | MUL | NULL    |                | 用户id
problem_id | int(11) | YES  | MUL | NULL    |                | 题号

### [<font color="#FF0000" id="user_join_contests">user_join_contests</font>](#user)

Field      | Type       | Null | Key | Default | Extra          | Description
---------- | ---------- | ---- | --- | ------- | -------------- | -----------
id         | int(11)    | NO   | PRI | NULL    | auto_increment | id
user_id    | int(11)    | YES  | MUL | NULL    |                | 用户id
contest_id | int(11)    | YES  | MUL | NULL    |                | 比赛id
is_join    | tinyint(1) | YES  |     | NULL    |                | 是否已加入

### [<font color="#FF0000" id="user_like_problems">user_like_problems</font>](#user)

Field      | Type       | Null | Key | Default | Extra          | Description
---------- | ---------- | ---- | --- | ------- | -------------- | -----------
id         | int(11)    | NO   | PRI | NULL    | auto_increment | id
user_id    | int(11)    | YES  | MUL | NULL    |                | 用户id
problem_id | int(11)    | YES  | MUL | NULL    |                | 题号
is_like    | tinyint(1) | YES  |     | NULL    |                | 是否喜欢

### [<font color="#FF0000" id="user_notes">user_notes</font>](#user)

Field      | Type    | Null | Key | Default | Extra          | Description
---------- | ------- | ---- | --- | ------- | -------------- | -----------
id         | int(11) | NO   | PRI | NULL    | auto_increment | id
user_id    | int(11) | YES  | MUL | NULL    |                | 用户id
problem_id | int(11) | YES  | MUL | NULL    |                | 题号
text       | text    | YES  |     | NULL    |                | 笔记

--------------------------------------------------------------------------------

## problem

1. [题目信息](#problems)

--------------------------------------------------------------------------------

### [<font color="#FF0000" id="problems">problems</font>](#problem)

Field       | Type         | Null | Key | Default | Extra          | Description
----------- | ------------ | ---- | --- | ------- | -------------- | -----------
id          | int(11)      | NO   | PRI | NULL    | auto_increment | 题号
title       | varchar(128) | NO   | UNI | NULL    |                | 标题
level       | smallint(6)  | NO   |     | NULL    |                | 难度
tag         | varchar(128) | NO   |     | NULL    |                | 标签
accepted    | int(11)      | YES  |     | NULL    |                | 通过数
submitted   | int(11)      | YES  |     | NULL    |                | 提交数
description | text         | NO   |     | NULL    |                | 题目描述
code        | text         | NO   |     | NULL    |                | 模版代码
solution    | text         | YES  |     | NULL    |                | 解决方法
contest_id  | int(11)      | YES  | MUL | NULL    |                | 所属比赛id
user_id     | int(11)      | YES  | MUL | NULL    |                | 所属用户id
input       | text         | NO   |     | NULL    |                | 官方输入
output      | text         | NO   |     | NULL    |                | 官方输出
program     | text         | NO   |     | NULL    |                | 官方C++代码

## contest

1. [比赛信息](#contests)

--------------------------------------------------------------------------------

### [<font color="#FF0000" id="contests">contests</font>](#contest)

Field        | Type         | Null | Key | Default | Extra          | Description
------------ | ------------ | ---- | --- | ------- | -------------- | -----------
id           | int(11)      | NO   | PRI | NULL    | auto_increment | 比赛id
user_id      | int(11)      | YES  | MUL | NULL    |                | 举办方id
title        | varchar(128) | NO   | UNI | NULL    |                | 标题
description  | text         | NO   |     | NULL    |                | 描述
start_time   | datetime     | NO   |     | NULL    |                | 开始时间
end_time     | datetime     | NO   |     | NULL    |                | 结束时间
auto_approve | tinyint(1)   | YES  |     | NULL    |                | 自动批准
password     | varchar(32)  | YES  |     | NULL    |                | 密码
