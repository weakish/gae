# -*- coding: utf-8 -*-
# by weakish <weakish@gmail.com>, licensed under GPL v2.

import stupidm_py2 as stupidm
from bottle import get, post, request, default_app
from google.appengine.ext.webapp.util import run_wsgi_app

HEAD = unicode('''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"> 
        <title>簡化中文、傳統中文轉換易誤字標記</title>
    </head>
    <body>
        <h1>簡化中文、傳統中文轉換易誤字標記</h1>
''', encoding='utf-8')

FORM = unicode('''
    <form method="post">
        <textarea name="content" rows="20" cols="80"></textarea>
        <p>
            <select name="config">
                <option selected="selected" >傳統中文</option>
                <option>简化中文</option>
            </select>
            起始標籤 <input type="text" value="{" name="pre" />
            結束標籤 <input type="text" value="}" name="post" />
            <input type="submit" value="提交" />
        </p>
    </form>
''', encoding='utf-8')

FOOTER =unicode('''
    <hr />
    <p>Powered by <a href="http://gist.github.com/510960">stupidm</a>, 
    and <a href="http://code.google.com/p/open-chinese-convert/">opencc</a>.  <a href="http://validator.w3.org/check/referer">Valid html5</a>. <a href="http://flattr.com/thing/89312/stupidm">Flattr this!</a></p>
    </body>
    ''', encoding='utf-8')


@get('/zhtran')
def form():
    page = HEAD + FORM + FOOTER
    return page.encode('utf-8')

@post('/zhtran')
def submit():
    text = unicode(request.forms.get('content'), encoding='utf-8')
    option = unicode(request.forms.get('config'), encoding='utf-8')
    tablefile = 'st_multi.table' if option == unicode('傳統中文', encoding='utf-8') else 'ts_multi.table'
    table = stupidm.gen_table(tablefile)
    pre = unicode(request.forms.get('pre'), encoding='utf-8')
    post = unicode(request.forms.get('post'), encoding='utf-8')
    cooked_text = stupidm.markup(text, table, pre, post)
    page = HEAD + '<pre>' + cooked_text + '</pre>' + '<hr />' + FORM + FOOTER
    return page.encode('utf-8')

def main():
    run_wsgi_app(default_app())

if __name__ == "__main__":
    main()
