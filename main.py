#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

urls = (
  r'/', 'index'
)

render = web.template.render('templates/', base='layout')

class index:
  def GET(self):
    return render.index()

app = web.application(urls, globals())

if __name__ == "__main__":
  app.run()

