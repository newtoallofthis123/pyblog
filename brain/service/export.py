from .file import ReadFile


class CopyFile:
    def __init__(self, filename, dirname, new_dirname):
        self.filename = filename
        self.dirname = dirname
        self.new_filename = filename
        self.new_dirname = new_dirname
        self.file_info = ReadFile(self.filename, self.dirname)

    def get_full_file(self):
        file_info = self.file_info
        return file_info.get_full_file()

    def file_exists(self):
        file_info = self.file_info
        return file_info.file_exists()

    def copy_file(self):
        if self.file_exists():
            with open(self.get_full_file(), 'r') as f:
                content = f.read()
            write_file =
            write_file.export_file()
            return True
        else:
            return False

export = CopyFile("test.md", "content", "")

export.copy_file()