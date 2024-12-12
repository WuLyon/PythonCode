# python装饰器

## 前置知识
函数可以接受另一个函数作为参数
```python
def square(x):
    return x*x

def new_square(func, x):
    print(f'{func.__name__} is running.')
    return func(x)

result = print_square(square, 2)
print(result)
```

## 装饰器函数
装饰器的本质是一个接受函数作为参数并返回一个新函数的高阶函数
```python
import time

def decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f'{func.__name__} duration: {duration} seconds')
        return result

    return wrapper

@decorator
def square(x):
    return x*x

result = square(2)
print(result)
```
- decorator是一个装饰器函数，内部函数_decorator具体改变了被装饰函数的功能，在这里是额外计算了函数执行的时间
- _decorator(*args, **kwargs)的形式可以适配各种函数不同的形参
- _decorator改变了原函数的功能，但也要保证具备原函数的功能，因此要在_decorator中执行原函数并将原函数的结果返回
- 装饰器函数要返回内部函数，即被装饰后的原函数func
- 语法糖符号@后面期望收到的是一个可调用对象，改对象接受一个函数作为参数，然后返回一个新的函数
    - 这里采用语法糖@符号的形式等价于：`square = decorator(square)`

## 装饰器生成器
可以理解成带参数的装饰器，使用一个外层函数将装饰器进行封装
```python
import time

def timeout_check(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            print(f'{func.__name__} duration: {duration} seconds')
            if duration > threshold:
                print(f'timeout! Threshold: {threshold}')
            return result
    
        return wrapper
    
    return decorator


@timeout_check(0.2)
def sleep_04():
    time.sleep(0.4)


sleep_04()
```

## functoos.wraps(func)语句
原函数func经过装饰器修饰后会变成新函数wrapper，其元信息也很改变。例如`func.__name__`会变为`wrapper`而不是`func`，为了防止这种情况，可以在wrapper函数前面加上`@functools.wraps(func)`进行修饰
```python
import time
import functools

def timeout_check(threshold):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start_time
            print(f'{func.__name__} duration: {duration} seconds')
            if duration > threshold:
                print(f'timeout! Threshold: {threshold}')
            return result
    
        return wrapper
    
    return decorator

@timeout_check(0.2)
def sleep_04():
    time.sleep(0.4)

print(sleep_04.__name__)
```