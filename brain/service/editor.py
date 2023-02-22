import os


class Editor:
    def __init__(self, dirname):
        self.dirname = dirname
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)).replace('\\brain\\service', ""))
        self.files = os.listdir(os.path.join(self.path, self.dirname))
        self.dirs = []

    def get_all_files(self):
        for file in self.files:
            if os.path.isdir(os.path.join(self.path, self.dirname, file)):
                for f in os.listdir(os.path.join(self.path, self.dirname, file)):
                    self.files.append(os.path.join(file, f))
        return self.files


editor = Editor("build")
print(editor.get_all_files())
