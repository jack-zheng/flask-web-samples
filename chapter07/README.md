# Tips of Chapter07

In this chapter, it gives a sample of orgnize a simple flask project.  
here is some records about how to use the extension of flask-moment and bootstrap-flask

1. 使用 datetime.utcnow() 记录时间，在template里面调用moment(time).xx 自动帮你更具时区做矫正
2. 用了 flask-boostrap, 感觉确实可以减少很多UI设计工作，但是扩展性一般， 就做到制式化，主要靠 bootstrap 网站去copy/paste
3. try about faker lib, and it's quick easy to use