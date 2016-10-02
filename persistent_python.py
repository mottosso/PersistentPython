import os
import json
import code
import sublime
import sublime_plugin


class PersistentPythonCommand(sublime_plugin.WindowCommand):
    """Run Python code within Sublime's internal Python interpreter"""

    def __init__(self, window):
        super().__init__(window)
        self.interpreter = code.InteractiveInterpreter()

        dirname = os.path.dirname(__file__)
        fname = os.path.join(dirname, "Persistent Python.sublime-build")

        # if not os.path.exists(fname):
        with open(fname, "w") as f:
            json.dump({
                "target": "persistent_python",
                "selector": "source.python"
            }, f, indent=4)

    def run(self):
        view = self.window.active_view()
        selection = view.sel()

        if len(selection) > 1:
            raise ValueError(
                "Multiple regions selected.\n"
                "This command only works on a single selection at a time,\n"
                "please reselect and try again."
            )

        region = selection[0]
        content = view.substr(region)

        if not region:
            # Mimic Maya's behavior of (1) running the entire
            # block and (2) clearing the view if no text is selected.
            region = sublime.Region(0, view.size())
            content = view.substr(region)
            view.run_command("select_all")
            view.run_command("right_delete")

        # Echo what is about to be run
        print(content)

        for line in content.split("\n"):
            self.interpreter.runsource(line)
