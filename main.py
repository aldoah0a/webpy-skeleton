#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import config
from config import render

urls = (
  r'/', 'index'
)

class index:
  def GET(self):
    return render.index()

def notfound():
  return web.notfound(render.error_404())

def internalerror():
  return web.internalerror(render.error_500())

app = web.application(urls, globals())

app.notfound = notfound
app.internalerror = internalerror

if __name__ == "__main__":
  app.run()

