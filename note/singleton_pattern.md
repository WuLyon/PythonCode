# 装饰器实现单例模式
单例模式是确保一个类只有一个实例，若实例不存在，则创建新的实例，若实例已经存在，则直接返回之前的实例。无论创建多少次实例，都会返回同一个对象。
常见的实现方式主要有：
- 类变量实现
- 装饰器实现
- 元类实现

---
**综合比较**

| **对比维度**       | **类变量实现**                     | **装饰器实现**               | **元类实现**                     |
|--------------------|------------------------------------|------------------------------|----------------------------------|
| **实现难度**        | 简单                              | 中等                         | 较高                            |
| **代码复用性**      | 较低                              | 高                           | 高                              |
| **耦合性**          | 高                                | 低                           | 低                              |
| **扩展性**          | 较低                              | 中等                         | 高                              |
| **性能**            | 高                                | 中等                         | 略低                            |
| **适合场景**        | 小型项目，简单单例需求            | 中型项目，多个单例类的场景    | 大型项目，框架或复杂单例管理场景 |
---

## 装饰器实现
```python
def singleton(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        # 若实例不存在则创建新实例，若实例已存在则直接返回
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton
class MyClass:

    def __init__(self, value):
        self.value = value


myclass1 = MyClass(10)
print(myclass1.value)
myclass2 = MyClass(20)
print(myclass2.value)
print(myclass1 is myclass2)
```
- `_instances = {}`适用于多个类的单例模式，优于`_instances = None`的方式
- singleton中涉及到python闭包的知识

