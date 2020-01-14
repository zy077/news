import redis
import logging


class Config(object):
    # 工程配置信息
    # SECRET_KEY用来生成加密令牌
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    # 默认日志等级
    LOG_LEVEL = logging.DEBUG

    # 数据库的配置信息
    SQLAlCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/news"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


class DevelopmentConfig(Config):
    """开发配置环境"""
    DEBUG = True


class ProductionConfig(Config):
    """生产配置环境"""
    LOG_LEVEL = logging.ERROR


# 定义配置字典
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}


