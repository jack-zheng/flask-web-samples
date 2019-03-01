# Chapter02 Tips

1. using `flask routes` to show all defined URLs
1. not sure how to use the `after_this_request` decorator, sample failed
1. chrome URL 地址栏左边的小叹号可以看cookie信息
1. cookie 很容易作伪，像登陆凭证社么的需要加密使用 - session
1. flask 的四种上下文变量: current_app, g, request, session
1. 科普了一下重定向漏洞及其解决方案
1. 科普了一下Web 安全
    + SQL 注入, 输入 "' or 1=1 --" 或者 "'; drop table student; --" 已达到返回所有值或者删除表的功能
    + 对策: ORM， 输入类型验证， 参数化查询(sql + ? 而不是拼接), 转义特殊字符
    + XSS(反射型/存储行)
    + 对策：HTML转义，输入验证
    + CSRF 攻击
    + 对策：使用正确的HTTP方法，CSRF令牌校验
## How To Run Chatper Sample

cd to chapter02 folder, run command `flask run`, app will start.