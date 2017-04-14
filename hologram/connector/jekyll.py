from sanic.log import log
from treelib import Node, Tree
import aiofiles
import yaml
import os


class Jekyll:
    def __init__(self, path):
        self.path = path
        self.tree = Tree()

    async def get_configuration(self):
        path = os.path.join(self.path, '_config.yml')
        log.info(path)
        if not os.path.exists(path):
          return {}

        async with aiofiles.open(path, mode='r') as f:
          content = await f.read()
          return yaml.load(content)

    def get_files(self):
        self.tree = Tree()
        for (folder, *childs) in os.walk(self.path):
            entry = folder.split('/')[-1]

            if not self.tree.get_node(folder) and folder == self.path:
                self.tree.create_node(entry, folder)
            childs = [ item for sublist in childs for item in sublist]
            for child in childs:
                self.tree.create_node(child, os.path.join(folder, child), parent=folder)

        return self.tree.to_json()

    async def get_data(self, path):
        pass

