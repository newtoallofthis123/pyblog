import os


class File:
    def __init__(self, filename, dirname):
        self.filename = filename
        self.dir = dirname
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)).
                                 replace('\\brain\\service', ""), self.dir, self.filename)
        self.export_path = os.path.join(os.path.dirname(os.path.abspath(__file__))
                                        .replace('\\brain\\service', ""), "build")

    def exists(self):
        return os.path.exists(self.path)

    def read(self):
        if self.exists():
            with open(self.path, 'r') as f:
                return f.read()
        else:
            return None

    def export(self, content, export_file):
        with open(os.path.join(self.export_path, export_file), 'w') as f:
            f.write(content)


def get_path(things):
    base = os.path.dirname(os.path.abspath(__file__)).replace('\\brain\\service', "")
    for thing in things:
        base = os.path.join(base, thing)
    return base


class ExportedFiles:
    def __init__(self):
        self.files = {
            "css": [],
            "js": [],
            "img": [],
            "html": []
        }

    def add(self, ext, file):
        self.files[ext].append(file)
        return self.files[ext]

    def get(self):
        return self.files
