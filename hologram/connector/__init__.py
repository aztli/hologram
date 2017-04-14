from hologram.connector.jekyll import Jekyll

async def get_metadata(path):
  j = Jekyll(path)

  return await j.get_configuration()

async def get_files(path):
  j = Jekyll(path)
  return j.get_files()
