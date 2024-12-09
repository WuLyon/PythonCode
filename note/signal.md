# 常见信号
`signal.SIGTERM` 终止信号
`signal.pause()` 等待接收信号
```python
import signal
import time

def handler(signum, frame):
    print('SIGTERM received! Exiting...')
    time.sleep(3)   # 模拟结束程序所需要的代码执行时间
    exit(0)

signal.signal(signal.SIGTERM, handler)   # 检测到SIGINT信号时，执行handler函数

print('Running...')
signal.pause()

```
`signal.SIGALRM` 定时信号
```python
import signal
import time


def timeout_handler(signum, frame):
    print('Timeout reached!')
    exit(0)


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(5) # 5s后发送定时信号

print('Waiting for the alarm to go off...')
signal.pause()
```
`signal.SIGINT` Ctrl+C信号
`signal.SIG_IGN` 忽略信号
```python
import signal
import time

signal.signal(signal.SIGINT, signal.SIG_IGN)

print('Running... Ctrl+C signal will be ignored.')

time.sleep(10)
```
`signal.raise_signal()`函数
```python
import signal
import time


def handler(signum, frame):
    print(f'Signal {signum} received.')


signal.signal(signal.SIGUSR1, handler)
signal.raise_signal(signal.SIGUSR1)

print('Signal raised.')
time.sleep(3)

```