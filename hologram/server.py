from sanic import Blueprint, log
from sanic.response import json
from sanic_jinja2 import SanicJinja2
from hologram.connector import get_metadata, get_files
from hologram.datastore import get_all_sites

import os


server = Blueprint('server')
jinja = SanicJinja2()


@server.route("/")
async def index(request):
  sites = await get_all_sites()
  data = await get_metadata(os.getcwd())
  files = await get_files(os.getcwd())

  return jinja.render('index.pug', request, metadata=data, files=files)

