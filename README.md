# Realtime Python （rtpy.py） 使用说明
---

## 概述

`Realtime Python（rtpy.py）` 是一个 Python 脚本，旨在根据配置文件的设定频率，自动执行指定的 Python 程序。该工具适用于需要频繁调试的代码。

## 文件结构

- **rtpy.py**: 主程序文件，负责读取配置文件并定期运行指定的 Python 脚本。
- **py文件**: 包含 执行频率 和 Python解释器路径 以及 脚本。

## py文件格式

py文件必须包含以下两行：
1. 执行频率（公式：停顿时间 * 60）。
2. Python 解释器的路径。
3. Python 脚本

示例配置文件内容：
```
# 120
# C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python311\\python.exe
a = input("what is your name? ")
print("hello " + a + "!")
```
其中，第一行使得 Python Realtime 每2秒执行一次代码，第二行是 Python 解释器的路径，第三行和以后是 Python 脚本。

## 使用方法

1. 使用已打包的 EXE 文件（rtpy.exe）：
   ```bash
   rtpy <脚本文件路径>
   ```
   例如：
   ```bash
   rtpy text.py
   ```

2. 程序将读取文件中的执行频率和 Python 解释器路径，并根据设定的频率定期运行指定的 Python 脚本。

## 主要功能

- **读取配置文件**: `read_config(path)` 负责读取文件，并返回执行频率和 Python 解释器路径。
- **执行脚本**: `job(path, py_path)` 根据文件中的解释器路径执行指定的 Python 脚本。
- **定期执行**: `run()` 是主函数，它读取命令行参数，获取配置文件路径，并启动定期执行任务的循环。

## 注意事项

- 确保py文件格式正确，否则程序会提示格式错误。
- 该脚本只经过 Windows11 的测试，其余系统没经测试，可能需要略微调整。
