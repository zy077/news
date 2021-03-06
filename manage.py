from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

# 创建 app，并传入配置模式：development / production
app = create_app("development")

# 添加扩展命令行
manager = Manager(app)

# 集成flask-Migrate，实现数据库的迁移
Migrate(app=app, db=db)
# 把flask-Migrate集成到flask-script
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
