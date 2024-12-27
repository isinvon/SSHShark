<img src="image/sshsk ico.png"/>

SSHShark 是一个优雅的 SSH 命令行工具，提供了便捷的服务器管理、文件传输功能，并支持密码安全存储 ^_^

### 特性 ✨

- 📝 自动保存和管理 SSH 登录凭据
- 📊 显示服务器列表和登录历史
- 🔒 安全的密码加密存储
- 📤 文件上传下载功能
- 🖥️ 交互式 SSH 终端
- 🌈 支持 Windows 和 Unix 系统
- 📒日志记录 (于项目的`logs/`下, 根据日期切割)

### 安装 🚀

#### window

```bash
git clone https://github.com/isinvon/SSHShark.git

cd ./SSHShark

./scripts/install.bat
```

#### linux/macos

```bash
git clone https://github.com/isinvon/SSHShark.git

cd ./SSHShark

./scripts/install.sh
```

### 效果 🌸

<img src="image/sshsk help.png"/>
<img src="image/ssh connect server.png"/>
<img src="image/sshsk login.png"/>
<img src="image/sshsk about.png"/>
<img src="image/sshsk select theme.png"/>
<img src="image/sshsk login after select theme.png"/>
<img src="image/sshsk about after select theme.png"/>
<img src="image/sshsk about after select theme lightcyan.png"/>

### 服务器管理 ⚙️

- 首次连接服务器时，会自动保存加密后的密码
- 后续连接同一服务器时将自动使用保存的密码
- 如果保存的密码失效，会提示输入新密码
- 可以通过序号快速选择已保存的服务器

### 详细功能说明 📘

#### 1. 服务器列表管理

- 首次登录时自动保存服务器信息
- 显示服务器列表包含：
  - 序号
  - 主机地址
  - 用户名
  - 登录次数
  - 最后登录时间

#### 2. 密码管理

- 首次登录后自动加密保存密码
- 后续登录自动使用已保存密码
- 密码验证失败时可以输入新密码
- 新密码验证成功后自动更新存储

#### 3. 文件传输

- 支持进度条显示
- 自动使用已保存的服务器凭据
- 传输失败时提供错误提示

## 安全性 🔐

- 所有密码都使用 Fernet 加密后存储
- 加密密钥单独存储在本地文件中
- 不会明文存储任何密码

### 密码存储 🔑

- 使用 Fernet 对称加密算法
- 加密密钥单独存储
- 数据库使用 SQLite 存储加密后的凭据

### 数据位置 🌐

- 数据库文件：`ssh_credentials.db`
- 加密密钥：`encryption.key`
- 建议定期备份这些文件

## 技术依赖 📦

- paramiko: SSH 协议实现
- cryptography: 密码加密
- tqdm: 进度条显示
- sqlite3: 数据存储

## 许可证 📄

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 作者 👨‍💻

Sinvon <2021469084@qq.com>

如果觉得这个项目有帮助，欢迎给个 Star ⭐️
