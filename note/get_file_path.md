在 Python 中，你可以使用 `os` 模块或者 `pathlib` 模块来获取当前执行的脚本的路径。

### 方法 1：使用 `os` 模块

`os.path` 可以获取当前脚本的路径。具体的代码如下：

```python
import os

# 获取当前脚本文件的绝对路径
current_script_path = os.path.abspath(__file__)

# 获取当前脚本文件所在的目录
current_script_dir = os.path.dirname(current_script_path)

print("Current script path:", current_script_path)
print("Current script directory:", current_script_dir)
```

#### 解释：
- `__file__`：表示当前脚本的路径。
- `os.path.abspath(__file__)`：返回当前脚本的绝对路径。
- `os.path.dirname(current_script_path)`：获取当前脚本所在的目录。

### 方法 2：使用 `pathlib` 模块

`pathlib` 是 Python 3.4 引入的现代路径操作库，它提供了更加面向对象的方式来操作文件路径。

```python
from pathlib import Path

# 获取当前脚本文件的路径
current_script_path = Path(__file__).resolve()

# 获取当前脚本文件所在的目录
current_script_dir = current_script_path.parent

print("Current script path:", current_script_path)
print("Current script directory:", current_script_dir)
```

#### 解释：
- `Path(__file__).resolve()`：返回当前脚本的绝对路径。
- `current_script_path.parent`：获取当前脚本文件所在的目录。

### 选择哪个方法？
- 如果你更喜欢函数式编程或已经习惯了 `os.path`，可以使用第一个方法。
- 如果你更喜欢面向对象的方式，或者在项目中已经使用 `pathlib`，则推荐使用第二个方法。

### 示例输出：
假设当前脚本的路径为 `/home/user/scripts/myscript.py`，那么执行上面任何一个方法都会输出：
```
Current script path: /home/user/scripts/myscript.py
Current script directory: /home/user/scripts
```

这两种方法都能够获取到当前脚本的位置，非常适用于需要读取或操作相对路径的场景。
