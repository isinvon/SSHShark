from cryptography.fernet import Fernet
import os

from utils import logUtils

# 生成密钥并保存到文件中
def generate_key():
    """生成新的密钥并保存到文件中"""
    if not os.path.exists("../key/secret.key"):
        logUtils.logging_and_print("未检测到密钥文件,正在生成密钥文件...")
        key = Fernet.generate_key()
        with open("../key/secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        logUtils.logging_and_print("检测到密钥文件,正在加载密钥文件...")

# 从文件中加载密钥
def load_key():
    """加载密钥文件"""
    generate_key()  # 如果密钥文件不存在，先生成它
    return open("../key/secret.key", "rb").read()

# 加密密码
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    logUtils.logging_and_print("正在加密密码...")
    return f.encrypt(password.encode())

# 解密密码
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    logUtils.logging_and_print("正在解密密码...")
    return f.decrypt(encrypted_password).decode() 