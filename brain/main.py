from service.format import *
from service.common import *
from rich.panel import Panel
from rich.console import Console
from service.gen import Generator
import random

console = Console()


def main():
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('PyBlog'))
    ran_str = random.choice(
        ["The best way to blog", "Because Go is overrated", "Because I can", "Making Blogging Easy"])
    console.print(Panel.fit(f"Welcome to PyBlog! {ran_str}", title="PyBlog", border_style="green"))
    cmd = get_args()["cmd"]
    if cmd == "build":
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
