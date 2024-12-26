from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from utils import logUtils
from datetime import datetime

Base = declarative_base()


class Credential(Base):
    """ 数据库模型 """
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    iv = Column(String, nullable=False)
    logins = relationship('LoginHistory', back_populates='credential')


class LoginHistory(Base):
    """ 数据库模型 """
    __tablename__ = 'login_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    credential_id = Column(Integer, ForeignKey(
        'credentials.id'), nullable=False)
    login_time = Column(DateTime, default=func.now())
    credential = relationship('Credential', back_populates='logins')


# 数据库初始化
current_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前文件所在完整路径
# DATABASE_URL = 'sqlite:///ssh_credentials.db' # 会生成到项目根目录下
DATABASE_URL = f'sqlite:///{os.path.join(current_dir, "ssh_credentials.db")}' # 会生成到当前项目同级的位置
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def generate_key(password, salt=None):
    """ 生成密钥 """
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt


def get_encryption_key():
    """ 获取主密码和盐值 """
    key_file = "key/encryption.key"
    salt_file = "key/salt.key"

    if os.path.exists(key_file) and os.path.exists(salt_file):
        with open(salt_file, "rb") as f:
            salt = f.read()
        with open(key_file, "rb") as f:
            master_key = f.read()
    else:
        master_password = base64.urlsafe_b64encode(os.urandom(32)).decode()
        master_key, salt = generate_key(master_password)
        with open(salt_file, "wb") as f:
            f.write(salt)
        with open(key_file, "wb") as f:
            f.write(master_key)
        # print(f"请安全保存你的主密码: {master_password}")

    return master_key


# 功能实现
def save_password(host, username, password):
    """ 保存密码 """
    session = SessionLocal()
    try:
        fernet = Fernet(get_encryption_key())
        iv = os.urandom(16).hex()
        encrypted_password = fernet.encrypt(password.encode()).decode()

        credential = session.query(Credential).filter_by(
            host=host, username=username).first()
        if not credential:
            credential = Credential(
                host=host, username=username, password=encrypted_password, iv=iv)
            session.add(credential)
        else:
            credential.password = encrypted_password
            credential.iv = iv

        session.commit()
        logUtils.logging_and_print(f"凭证保存成功: {host}, {username}")
    except Exception as e:
        session.rollback()
        logUtils.logging_and_print_error(f"保存密码时出错: {str(e)}")
    finally:
        session.close()


def get_password(host, username):
    """ 获取密码 """
    session = SessionLocal()
    try:
        credential = session.query(Credential).filter_by(
            host=host, username=username).first()
        if credential:
            fernet = Fernet(get_encryption_key())
            decrypted_password = fernet.decrypt(
                credential.password.encode()).decode()
            return decrypted_password
        else:
            logUtils.logging_and_print_warning(f"未找到保存的密码")
            return None
    except Exception as e:
        logUtils.logging_and_print_error(f"获取密码时出错: {str(e)}")
        return None
    finally:
        session.close()


def record_login(host, username):
    """ 记录登录历史 """
    session = SessionLocal()
    try:
        credential = session.query(Credential).filter_by(
            host=host, username=username).first()
        if credential:
            login = LoginHistory(credential=credential, login_time=datetime.now())
            session.add(login)
            session.commit()
            logUtils.logging_and_print(f"登录记录保存成功: {host}, {username}")
        else:
            logUtils.logging_and_print_warning(f"未找到相关凭证，无法记录登录")
    except Exception as e:
        session.rollback()
        logUtils.logging_and_print_error(f"记录登录历史时出错: {str(e)}")
    finally:
        session.close()


def get_server_list():
    """ 获取服务器列表 """
    session = SessionLocal()
    try:
        results = session.query(
            Credential.host,
            Credential.username,
            func.count(LoginHistory.id).label('login_count'),
            func.max(LoginHistory.login_time).label('last_login')
        ).outerjoin(LoginHistory).group_by(Credential.host, Credential.username).order_by(func.max(LoginHistory.login_time).desc()).all()

        if results:
            return results
        else:
            logUtils.logging_and_print_warning("没有保存的服务器记录")
            return []
    except Exception as e:
        logUtils.logging_and_print_error(f"获取服务器列表时出错: {str(e)}")
        return []
    finally:
        session.close()
