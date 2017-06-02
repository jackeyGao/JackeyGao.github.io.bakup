[jackeygao.github.io](http://jackeygao.github.io)
----

## Packages

需要安装jinja2、misaka, pygments库

## 运行

```
mkdir ./markdown
echo -e "title: Hello\ndate: 2017-03-16 12:41:12\n---\nMy first post" >> ./markdown/hello.md
make deploy
```


## 渲染逻辑

```
├── scripts
│   ├── md.py     # 基于 misaka 的markdown定制
│   └── render.py # 渲染脚本, 更新md文件后执行
```

## make语句

```bash
# Generate stylesheets.
NOW = $(shell date '+%Y-%m-%d %H:%M:%S')

all: render

style:
    sass --update assets/scss:assets/stylesheets

render: style
    python scripts/render.py

watch:
    sass --watch assets/scss:assets/stylesheets

deploy:
    make render
    git add rss.xml
    git add '*.html'
    git add 'words/*.html'
    git commit -m "[UPDATE] $(NOW)"
    git push origin master
```

## License

MIT
