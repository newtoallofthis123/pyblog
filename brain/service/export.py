from .common import *


class Export:
    def __init__(self, filename, content):
        self.filename = filename
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)).replace('\\brain\\service', ""),
                                 "build", filename)
        self.static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)).replace('\\brain\\service', ""),
                                        "build", "static")
        if os.path.isdir(os.path.join(self.static_path)):
            pass
        else:
            os.mkdir(os.path.join(self.static_path))
        self.content = content

    def export(self):
        with open(self.path, 'w') as f:
            f.write(self.content)
        return self.path

    def static_export(self, dirname):
        if os.path.isdir(os.path.join(self.static_path, dirname)):
            pass
        else:
            os.mkdir(os.path.join(self.static_path, dirname))
        with open(os.path.join(self.static_path, dirname, self.filename), 'w') as f:
            f.write(self.content)
