from cryptography.fernet import Fernet
import os

# 生成密钥并保存到文件中
def generate_key():
    """生成新的密钥并保存到文件中"""
    if not os.path.exists("../key/secret.key"):
        key = Fernet.generate_key()
        with open("../key/secret.key", "wb") as key_file:
            key_file.write(key)

# 从文件中加载密钥
def load_key():
    """加载密钥文件"""
    generate_key()  # 如果密钥文件不存在，先生成它
    return open("../key/secret.key", "rb").read()

# 加密密码
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

# 解密密码
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode() 