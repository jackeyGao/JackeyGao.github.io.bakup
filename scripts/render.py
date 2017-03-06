# -*- coding: utf-8 -*-
import jinja2
import os
import sys
from os.path import splitext
from datetime import datetime
from md import markrender

reload(sys)
sys.setdefaultencoding('utf-8')

template_loader = jinja2.FileSystemLoader(searchpath="templates")
template_env = jinja2.Environment(loader=template_loader)
WORD_TEMPLATE_FILE = "word.html"
WORDS_TEMPLATE_FILE = "words.html"
RSS_TEMPLATE_FILE = 'rss.xml'

markdown_files = os.listdir('markdown')


words = []

for file in markdown_files:
    with open("markdown/%s" % file) as f:
        content = f.read()

    title = ' '.join(word.title() for word in file[:-3].split('-'))
    filename = splitext(file)[0]

    headers = content.split('---')[0]
    content = '---'.join(content.split('---')[1:])

    for line in headers.splitlines():
        if line.startswith('title'):
            title = ':'.join(line.split(':')[1:]).strip()
        if line.startswith('date'):
            date = ':'.join(line.split(':')[1:]).strip()

    if not title or not date:
        print("%s 头信息解析失败" % filename)
        continue

    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    words.append({
        'filename': filename,
        'title': title,
        'date': date
    })
    
    md = markrender(content)

    template = template_env.get_template(WORD_TEMPLATE_FILE)
    output = template.render(title=title, content=md, date=date)

    html_filename = splitext(file)[0] + '.html'
    with open('words/%s' % html_filename, 'w') as f:
        f.write(output)


words = sorted(words, key=lambda x: x["date"], reverse=True)
template = template_env.get_template(WORDS_TEMPLATE_FILE)
output = template.render(words=words)
with open('words.html', 'w') as f: f.write(output)


template = template_env.get_template(RSS_TEMPLATE_FILE)
output = template.render(words=words)
with open('rss.xml', 'w') as f: f.write(output)
