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

app = web.application(urls, globals())

if __name__ == "__main__":
  app.run()

