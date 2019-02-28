# Chapter01 Tips

1. 没有指定 flask 实例的情况下，Flask 会
    + 从当前目录找app.py和wsgi.py, 并从中寻找 app 或 application 实例
    + 从环境变量 FLASK_APP 找对应的值找 app 或 application
1. 安装了 python-dotenv 后， flask run 会自动加载 .flaskenv 和 .env
    + 优先级： 手动设置 > .env > .flaskenv
1. `flask run --host=0.0.0.0` 可以把服务暴露到内网，不过我本地测试失败
1. 页面 CSS/JS 缓存可以通过 `Ctrl/Shift + F5` 忽略缓存重新加载

## How To Run Chatper Sample

cd to chapter01 folder, run command `flask run`, app will start.