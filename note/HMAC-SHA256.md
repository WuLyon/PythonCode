在 Python 中，`hmac` 模块可以与 `hashlib` 模块结合，方便地使用 HMAC-SHA256 算法对消息进行加密。

下面是如何使用 Python 实现 HMAC-SHA256 加密的步骤：

### 代码示例

```python
import hmac
import hashlib

# 定义密钥和消息
key = b'secret_key'  # 使用字节格式的密钥
message = b'This is a message.'  # 使用字节格式的消息

# 生成 HMAC-SHA256 加密
hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()

print("HMAC-SHA256:", hmac_sha256)
```

### 代码解析
1. **导入模块**：
   - `hmac`：用于生成 HMAC 加密。
   - `hashlib`：提供不同的哈希算法，如 `sha256`。
  
2. **设置密钥和消息**：
   - `key` 是用于加密的密钥，类型为字节对象。密钥应足够复杂以提高安全性。
   - `message` 是要加密的消息，同样为字节对象。

3. **生成 HMAC-SHA256 加密**：
   - `hmac.new(key, message, hashlib.sha256)` 创建一个 HMAC 对象，使用 SHA256 作为哈希算法。
   - `.hexdigest()` 将加密结果转换为十六进制字符串，便于读取和传输。

### 注意事项
- **密钥**：HMAC 使用的密钥应保密且随机化，以确保加密的安全性。
- **消息格式**：`key` 和 `message` 都需是字节对象，因此若输入为字符串，需要用 `.encode()` 转换，例如 `key = 'secret_key'.encode()`。

### 运行结果
上述代码将输出类似以下格式的加密字符串：
```
HMAC-SHA256: 5f4d76ecf6b1b4d89f5f5d55b5f1c11a34cb4f65bb17a20e01b59ac10f9a0e1c
```

### HMAC-SHA256 应用场景
HMAC-SHA256 常用于验证数据完整性和身份认证，在 API 通信、数据签名和消息加密中被广泛应用。
