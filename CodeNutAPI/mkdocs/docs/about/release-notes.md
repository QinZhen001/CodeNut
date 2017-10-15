# <center>Release Notes</center>

--------------------------------------------------------------------------------

## Plan

- docker 容器装载应用，redis 缓存热数据，分布式架构（[参考知乎](https://zhuanlan.zhihu.com/p/26418829?utm_source=qq&utm_medium=social)）

## Version 1.0

### 2017-10-15

1. 数据库 problems 表增加 input，output，program 字段，**创建/修改题目接口 PUT /problems/<id> 增加相应字段</id>**。
2. 开放用户修改头像接口（base64编码）。
3. 英文题目均已下线，上线5个已翻译的简单题目。
4. 运行代码接口改为真实判题，提交代码接口仍是随机数据。

### 2017-9-26

- 所有 API 均已测试并放在首页说明，可能使用过程还存在 Bug，请及时反馈:)
