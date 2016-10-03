import io
import sys
import code
import contextlib

import sublime
import sublime_plugin

module = sys.modules[__name__]
module.panels = {}


class PersistentPythonCommand(sublime_plugin.WindowCommand):
    """Run Python code within Sublime's internal Python interpreter"""

    def __init__(self, window):
        super().__init__(window)
        self._interpreter = code.InteractiveConsole()

    def run(self):
        view = self.window.active_view()
        selection = view.sel()
        content = "\n".join(view.substr(region) for region in selection)

        if not content:
            # Run all and clear
            region = sublime.Region(0, view.size())
            content = view.substr(region)
            view.run_command("select_all")
            view.run_command("right_delete")

        self.echo(content.rstrip())

        for line in content.split("\n"):

            # Capture context within loop, so as to provide
            # real-time updates of cheap calls intermixed
            # with expensive calls.
            with stdout() as f:
                self._interpreter.push(line)
            value = f.getvalue().strip()

            if value:
                self.echo(value)

    def echo(self, text):
        """Print `text` to a dedicated output panel"""
        self.window.run_command("persistent_python_echo", {"text": text})


class PersistentPythonEchoCommand(sublime_plugin.TextCommand):
    """Display output in dedicated panel"""

    def run(self, edit, text):
        window = self.view.window()

        # Enable output panel in whichever window
        # happens to be active at the time.
        if window.id() not in module.panels:
            module.panels.update({
                window.id(): window.create_output_panel("persistentpython")
            })

        panel = module.panels[window.id()]

        panel.insert(edit, panel.size(), str(text) + "\n")
        panel.show(panel.size())

        window.run_command("show_panel",
                           {"panel": "output.persistentpython"})


@contextlib.contextmanager
def stdout():
    """Redirect all output"""

    # Sublime makes modifications to stdout and stderr
    # that isn't reflected in sys.__stdout__, i.e.
    # >>> sys.stdout != sys.__stdout__
    # ..hence we must maintain our own local copy.
    _stdout = sys.stdout
    _stderr = sys.stderr

    stdout = sys.stdout = sys.stderr = io.StringIO()

    try:
        yield stdout

    finally:
        sys.stdout = _stdout
        sys.stderr = _stderr
