from . import index_blu


# 给蓝图注册路由
@index_blu.route('/')
@index_blu.route("/index")
def index():
    return 'index'