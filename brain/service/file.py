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


def time_cal():
    from datetime import datetime, date
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    time_date = f'{current_t_f} {current_date}'
    return time_date


class New:
    def __init__(self, title):
        self.title = title
        self.date = time_cal()

    def create(self):
        path = get_path(["content"])
        with open(os.path.join(path, f"{self.title}.md"), 'w') as f:
            f.write(f"-----Date: {self.date}-------\n# {self.title}\n")
        return True
