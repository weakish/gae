#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
# Copyright 2008 Weakish Jiang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Based on the guestbook sample in Google App Engine start guide and
# reST render written by Jiri Barton <jbar@hosting4u.cz>
# Jiri Barton <jbar@hosting4u.cz>

import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from docutils.core import publish_string

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<!DOCTYPE html 
     PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<head>

<title>reST renderer</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

</head>
<body>

<h1>reST to HTML conversion</h1>

<form action="/sign" method="post">
    <label>Type some reST into the box below:</label>
    <br /><br />
    <textarea name="content" rows="20" cols="80"></textarea>
    <br /><br />
    <input type="submit" value="Render" />
</form>

<hr />
<p><a href="http://bitbucket.org/weakish/weakishscripts/wiki/reSTRenderOnGAE" title="about this reSt render app">about...</a></p>
</body>
     
</html>
        
        """)

class Guestbook(webapp.RequestHandler):
  def post(self):
    self.response.out.write("""
<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<!DOCTYPE html 
     PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<head>

<title>reST renderer</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

</head>
<body>

<h1>reST to HTML conversion</h1>
    """)

    self.response.out.write('<h1>Preview:</h1>')
    self.response.out.write(render(self.request.get('content')))
    self.response.out.write("""
<hr />
<form action="/sign" method="post">
    <label>Type some reST into the box below:</label>
    <br /><br />
    <textarea name="content" rows="20" cols="80">""")
    self.response.out.write(cgi.escape(self.request.get('content')))
    self.response.out.write("""
    </textarea><br /><br />
    <input type="submit" value="Render" />
</form>

</body>
     
<hr />
<p><a href="http://bitbucket.org/weakish/weakishscripts/wiki/reSTRenderOnGAE" title="about this reSt render app">about...</a></p>
</html>

        """)

application = webapp.WSGIApplication(
                                     [('/rest.py', MainPage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def render(content=''):
    return publish_string(
        source=content,
        settings_overrides={'_disable_config': True, 'file_insertion_enabled': 0, 'raw_enabled': 0},
        writer_name='html')



def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()


