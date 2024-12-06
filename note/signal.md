# 常见信号
`signal.SIGINT` Ctrl+C信号
```python
import signal
import time

def handler(signum, frame):
    print('SIGINT received! Exiting...')
    exit(0)

signal.signal(signal.SIGINT, handler)   # 检测到SIGINT信号时，执行handler函数

print('Running... Press Ctrl+c to stop.')

while True:
    time.sleep(1)

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
time.sleep(10)
```
`signal.SIGTERM` 终止信号
`signal.SIG_IGN` 忽略信号
```python
import signal
import time


```
