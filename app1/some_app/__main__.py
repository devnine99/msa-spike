import sys
import importlib.util

from some_app.app import SomeApp

BIN_NAME = 'some_app.py'  # TODO: bin에 등록되면 고정(some_app)


def main():
    app = 'config.events'  # TODO: command 입력 받도록 ex) some_app -A config.events
    module_name = 'some_app'
    module_path = sys.argv[0].replace(BIN_NAME, f'{app.replace(".", "/")}.py')

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for m in mod.__dir__():
        if isinstance(getattr(mod, m), SomeApp):
            sys.exit(getattr(mod, m).run())
