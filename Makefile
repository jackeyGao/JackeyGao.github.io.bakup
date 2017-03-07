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
	git pull coding master
