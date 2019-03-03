# Chapter05 Tips

1. 一般不需要为所有的列创建索引， 一般只为使用频率高的，如 name, 或者经常作为排序依据的时间戳剑
1. show table creation sql:
    + from sqlalchemy.schema import CreateTable
    + print(CreateTable(Note.__table__))
1. 查询的常用模式: <模型类>.query.<过滤方法>.<查询方法>
1. filter 条件中需要添加 class name(Note.body==), filter_by 里面直接接属性名字(body=)
1. 像删除这种动作一定要用 post 完成， 安全考虑， CSRF 攻击
1. 做 update 操作的时候不需要显示的把对象加到 session 中去，赋值之后直接commit 就行了
    + note = Note.query.get(1); db.session.commit()
1. db.sesion.add_all([t1, t2]) 简化操作
1. app.shell_context_processor 简化 flask shell 对 DB model 的操作
1. foo.articles.remove(t1) / pop() 来移除外键联系
1. 避免使用 dynamic 动态加载，会有潜在的性能问题， 每次操作都会执行一次SQL查询
1. db 的这些关系类型真是让人瞬间有睿智的赶脚啊，蛋疼
1. db 中经常提到的标量关系是什么东西！？
1. 多对多的关系中需要用到关联表 - association table， 只存外键对应关系不存数据
1. sqlite 不支持删除/修改字段，所以他的工作流一般为 创建表 - 转移数据 - 删除旧表
1. 级联操作，简化是事物之间的联系，减少了手动操作， 类似删除文章，那么对应的评论也需要被删除一样