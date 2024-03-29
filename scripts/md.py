# -*- coding: utf-8 -*-
'''
File Name: markdown.py
Author: JackeyGao
mail: gaojunqi@outlook.com
Created Time: 五  8/12 09:59:17 2016
'''
import sys, re
import misaka as m
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

reload(sys)
sys.setdefaultencoding('utf-8')

cleanr =re.compile('<.*?>')

class HighlighterRenderer(m.HtmlRenderer):
    def blockcode(self, text, lang):
        if not lang:
            return '''<div class="code-wrapper">
          <span class="lang-label">Raw</span>
        \n<div class="highlight"><pre>{}</pre></div></div>\n'''.format(
                text.strip())


        try:
            lexer = get_lexer_by_name(lang, stripall=True)
            language = lexer.name
        except ClassNotFound:
            lexer = get_lexer_by_name('text', stripall=True)
            language = lang
            
        formatter = HtmlFormatter()
        content = highlight(text, lexer, formatter)
            
        langDiv = '<span class="lang-label">' + language + '</span>'
        return '<div class="code-wrapper">' + langDiv + content + '</div>'


    def blockquote(self, content):
        _real = re.sub(cleanr,'', content).strip()
        if _real.startswith('%center\n'):
            content = content.replace('%center', '')
            className = "blockquote-center"
        elif _real.startswith('%warning'):
            content = content.replace('%warning', '')
            className = "blockquote-warning"
        elif _real.startswith('%error'):
            content = content.replace('%error', '')
            className = "blockquote-error"
        else:
            content = content
            className = "blockquote-normal"
        
        content = content.replace('\n', '<br/>')
        content = content.replace('</p><br/>', '</p>')
        content = content.replace('<p><br/>', '<p>')

        return '''<blockquote class="%s">
                %s</blockquote>''' % (className, content)

    def image(self, link, title="", alt=''):
        link = link.replace('/uploads', 'http://orzdljguj.bkt.clouddn.com')
        if title:
            return  '''
                    <p class="hassubimage"><img src="%s" alt="%s"></p>
                    <p class="img-title">%s</p>''' % (link, alt, title)
        else:
            return '<p class="hassubimage"><img src="%s" alt="%s"></p>\n' % (link, alt)

    def table(self, content):
        return '<div class="table-wrapper"><table class="ui selectable celled table">'\
                + content + '</table></div>'


markdown = m.Markdown(
    HighlighterRenderer(),
    extensions=\
    m.EXT_FENCED_CODE |\
    m.EXT_TABLES |\
    m.EXT_QUOTE
)

#toc = m.Markdown(m.HtmlTocRenderer())

def markrender(content):
    return markdown(content)

if __name__ == '__main__':
    print markrender('''> %center''')
