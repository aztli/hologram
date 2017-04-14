from blitzdb import Document, FileBackend

import os

datastore = FileBackend(os.path.join(os.getcwd(),'.datastore.db'))


class DataFile(Document):
    pass

class Files(Document):
    pass

class Metadata(Document):
    pass

class Site(Document):
    pass

async def get_all_sites():
  return datastore.filter(Site, {})
