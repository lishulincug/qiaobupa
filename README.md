# qiaobupa 和 kanzhun 的咨询页面调整

执行下面语句可以获取http://cv.qiaobutang.com/knowledge/categories 下的所有文章,总计约5990篇
```
python request_categories.py
```

执行下面语句可以获取http://cv.qiaobutang.com/knowledge/intentions 下的所有文章,总计约560篇
```
python request_intentions.py
```

执行下面语句可以获取http://www.kanzhun.com/news/ 下的所有文章,大约15*261篇
```
python request_kanzhun.py
```



执行过程实际是两步

1. 获取全部链接
2. 下载指定链接的标题内容

返回数据为 json 格式,每一条数据都是title 和 content 的 kv形式,编码为 utf-8可能需要届时注意要再调整
