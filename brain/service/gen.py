from .export import *
from .brain import *
from .file import ExportedFiles, File
from jinja2 import Template


class Generator:
    def __init__(self, filename="index.md"):
        self.filename = filename
        self.lang = "." + str(filename).split('.')[1]
        self.files = ExportedFiles()
        self.boiler = True

    def og_content(self):
        og_file = File(self.filename, 'content')
        content = og_file.read()
        return content

    def md_convert(self, content):
        from markdown import markdown
        md = markdown(content)
        return md

    def export_static(self):
        for file in os.listdir(get_path(['static'])):
            if file.endswith('.css'):
                css_file = File(file, 'static')
                css_content = css_file.read()
                self.files.add('css', file)
                export_file = Export(file, css_content)
                export_file.static_export('css')
            elif file.endswith('.js'):
                js_file = File(file, 'static')
                js_content = js_file.read()
                self.files.add('js', file)
                export_file = Export(file, js_content)
                export_file.static_export('js')
        return self.boiler

    def render_html(self, content):
        tm = Template(File('base.html', 'templates').read())
        print(self.files.get())
        html_content = tm.render(
            args=get_config(),
            files=self.files.get(),
            content=content
        )
        return html_content

    def export_html(self):
        for file in os.listdir(get_path(['content'])):
            if file.endswith('.md'):
                html_file = File(file, 'content')
                html_content = html_file.read()
                self.files.add('html', file.replace(".md", ".html"))
                export_file = Export(file.replace(".md", ".html"), self.render_html(self.md_convert(html_content)))
                export_file.export()
        return self.boiler

    def other_exports(self):
        for file in os.listdir(get_path(['templates'])):
            base_file = File(file, 'templates')
            tm = Template(base_file.read())
            content = tm.render(
                args=get_config(),
                files=self.files.get()
            )
            export_file = Export(file, content)
            export_file.export()
            return self.boiler

    def combine(self):
        self.export_static()
        self.export_html()
        self.other_exports()
        return self.boiler

    def build(self):
        if self.combine():
            return True
        else:
            return False

    def server(self):
        from http.server import HTTPServer, CGIHTTPRequestHandler
        os.chdir(get_path(['build']))
        server = HTTPServer(('', 8000), CGIHTTPRequestHandler)
        server.serve_forever()
