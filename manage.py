from flask import Flask

app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    # 工程配置信息
    # 设置日志等级
    DEBUG = True
    # SECRET_KEY用来生成加密令牌
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

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


app.config.from_object(Config)
# 关联app，实现ORM
db = SQLAlchemy(app)
# 通过StrictRedis指定端口和ip，即获得redis的连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 对于包含请求体的请求都开启了CSRF
CSRFProtect(app)
# 配置session
Session(app)
# 使用命令执行数据库迁移
manager = Manager(app)
# 集成flask-Migrate，实现数据库的迁移
Migrate(app=app, db=db)
# 把flask-Migrate集成到flask-script
manager.add_command('db', MigrateCommand)


@app.route('/')
@app.route('/index')
def index():
    return "index"


if __name__ == '__main__':
    app.run()
