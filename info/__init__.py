import logging
from logging.handlers import RotatingFileHandler

from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config
from flask import Flask

# 数据库
db = SQLAlchemy()
redis_store = None

def setup_log(config_name):
    """配置日志"""
    # 设置日志记录的等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试DEBUG级别
    # 创建日志记录器，指明日志文件的保存路径、日志文件的最大大小、保存日志文件的数量上限
    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d%(message)s')
    # 为刚创建的日志记录器设置日志格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志记录工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

    # 配置日志
    setup_log(config_name)

    # 创建应用对象
    app = Flask(__name__)

    # 把蓝图注册到应用上
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    # 配置
    app.config.from_object(config[config_name])
    # 配置数据库
    db.init_app(app)
    # 配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启csrf保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    return app
