from service.format import *
from service.brain import *
from rich.panel import Panel
from rich.console import Console
from service.gen import Generator


console = Console()


def main():
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('PyBlog'))
    console.print(Panel.fit("Welcome to PyBlog! The Best way to Blog", title="PyBlog", border_style="green"))
    cmd = get_args()["cmd"]
    if cmd == "build":
        generator = Generator()
        if generator.build():
            c_print("Build Successful! Check the build directory 🥳", "success")
    if cmd == "serve":
        generator = Generator()
        if generator.build():
            c_print("Build Successful! Serving using http.server", "success")
            c_print("This is not a production server, use a proper server for production", "warning")
            c_print("Serving on http://localhost:8000", "info")
            generator.server()


if __name__ == "__main__":
    main()
