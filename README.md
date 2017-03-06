[jackeygao.github.io](http://jackeygao.github.io)
----

## Packages

需要安装jinja2、misaka, pygments库

## 渲染逻辑

```
├── scripts
│   ├── md.py     # 基于 misaka 的markdown定制
│   └── render.py # 渲染脚本, 更新md文件后执行
```

## make语句

```bash
all: render

style:
    sass --update assets/scss:assets/stylesheets

render: style
    python scripts/render.py

watch:
    sass --watch assets/scss:assets/stylesheets
```

暂时没有做deploy的定义

## License

MIT
