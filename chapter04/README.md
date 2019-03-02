# Chapter04 Tips

1. fire flask shell and new a form object would be failed. you need to push a context for testing
    + `app.test_request_context()`; `ctx.push()`; `ctx.pop()`;
1. use `render_kw` to add extra attribute
1. 可以在页面 template 中给 form 设置属性
1. Post 表单通过 request.form 得到；Get 通过 request.args 得到
1. 表单阿雷自动识别 validate_xx 形式的函数做验证
1. 4.4.3 中的工厂模式 validator 感觉很玄幻啊
1. 上传文件时需要将 template 中的 enctype 改为 `multipart/form-data`, or only file name will pass to server side
1. use request.files to get the upload file content