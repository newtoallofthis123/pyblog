import os


class ReadFile:
    def __init__(self, filename, dirname):
        self.filename = filename
        self.dirname = dirname
        self.content = self.get_content()
        self.current_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\brain\\service', "")
        self.full_path = self.get_full_file()

    def get_full_file(self):
        return os.path.join(self.current_dir, self.dirname, self.filename)

    def file_exists(self):
        return os.path.isfile(self.full_path)

    def get_content(self):
        if not self.file_exists():
            return ""
        else:
            with open(self.full_path, 'r') as f:
                return f.read()

    def get_export_path(self):
        return os.path.join(self.current_dir, "build", self.dirname, self.filename)

    def write_file(self):
        if self.file_exists():
            with open(self.get_full_file(), 'w') as f:
                f.write(self.content)
            return True
        else:
            return False

    def export_file(self):
        if self.file_exists():
            with open(self.get_export_path(), 'w') as f:
                f.write(self.content)
            return True
        else:
            return False
