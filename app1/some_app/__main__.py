import sys
import importlib.util

from some_app.app import SomeApp

BIN_NAME = 'someapp.py'  # TODO: bin에 등록되면 고정(someapp)


def main():
    module_name = 'some_app'
    module_path = sys.argv[0].replace(BIN_NAME, 'config/events.py')  # TODO: command 입력 받도록 ex) someapp -A config.events

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for m in mod.__dir__():
        if isinstance(getattr(mod, m), SomeApp):
            sys.exit(getattr(mod, m).run())
