from brain.service.format import *
from brain.service.common import *
from brain.service.file import *
from rich.panel import Panel
from rich.console import Console
from brain.service.gen import Generator
import random

console = Console()


def main():
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('PyBlog'))
    ran_str = random.choice(
        ["The best way to blog", "Because Go is overrated", "Because I can", "Making Blogging Easy"])
    console.print(Panel.fit(
        f"Welcome to PyBlog! {ran_str}", title="PyBlog", border_style="green"))
    cmd = get_args()["cmd"]
    if cmd == "help":
        c_print("You gave no arguments, so here's the help message", "danger")
        c_print("PyBlog Help", "success")
        console.print(Panel.fit(
            "[red]build[/red] - Builds the blog\n"
            "[blue]help[/blue] - Print this help message\n"
            "[green]serve[/green] - Builds and serves the blog on http.server\n"
            "[yellow]serve[/yellow] - Generates New Post"
        ))
    if cmd == "build":
        generator = Generator()
        if generator.build():
            c_print("Build Successful! Check the build directory 🥳", "success")
    if cmd == "serve":
        generator = Generator()
        if generator.build():
            c_print("Build Successful! Serving using http.server", "success")
            c_print(
                "This is not a production server, use a proper server for production", "warning")
            c_print("Serving on http://localhost:8000", "info")
            generator.server()
    if cmd == "new":
        c_print("PyBlog New", "success")
        title = prompt("Enter the title of the post: ")
        new_post = New(title)
        new_post.create()
        if new_post.create():
            c_print("Post created! Check the content directory", "success")
        else:
            c_print("Post creation failed", "danger")
        

if __name__ == "__main__":
    main()
