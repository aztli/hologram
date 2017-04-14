from sanic import Blueprint, log
from sanic.response import json
from sanic_jinja2 import SanicJinja2
from hologram.connector import get_metadata, get_files, get_data
from hologram.datastore import get_all_sites, datastore, Site

import os


server = Blueprint('server')
jinja = SanicJinja2()


@server.route("/")
async def index(request):
  #site = Site({'title': 'opensource.guide', 'path': '/home/meliodas/code/ewok/Hologram/examples/opensource.guide'})
  #datastore.save(site)
  sites = await get_all_sites()
  #datastore.commit()
  sites_dict = {}
  for site in sites:
      sites_dict[site.title] = {}
      sites_dict[site.title]['metadata'] = await get_metadata(site.path)
      sites_dict[site.title]['files'] = await get_files(site.path)
      sites_dict[site.title]['data'] = await get_data(site.path)
  return jinja.render('index.pug', request, sites_dict=sites_dict)
