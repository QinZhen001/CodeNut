# CodeNutJudge 1.0

Judge for CodeNut

## Install

``sudo setup.py install``

## Usage:

``import CodeNutJudger``

```python3
cfg = {
        'args': ['xx.py', '1', '2'],  # 程序+输入参数
        'output': 'out_file',         # 输出文件名
        'language': 'Pyhon3',         # 源文件语言
        'time_limit': 1000,           # 时间限制(MS)
        'memory_limit': 65536,        # 内存限制(KB)
    }
```

``result = CodeNutJudger.run(cfg)``

结果也是一个python的dict类型变量:

```python3
result = {
	'status': 'Dangerous System Call', # 运行结果
	'time_used': 1.0,                  # 程序所占用的用户态时间
	'memory_used': 6424.0,             # 内存占用峰值
}
```

## Status

```text
System Error: 设置错误或其他问题
Accepted: 成功运行并得到了正确的结果
Wrong Answer: 成功运行但到得了错误的结果
Dangerous System Call: 程序因为危险的系统调用被终止
Runtime Error: 程序因为类似于堆栈溢出的错误而被系统终止，即运行错误
Compile Error: 源代码无法被正确编译
Time Limit Exceed: 超过时间限制
Memory Limit Exceed: 超过内存限制
Output Limit Exceed: 程序输出长度超过答案长度
Run Successfully: 运行成功但是不可预知的错误发生
```
