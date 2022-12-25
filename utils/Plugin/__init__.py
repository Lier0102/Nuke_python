from importlib import util
from .PluginABC import PluginABC
import os

plugins: list[type[PluginABC]] = []


def register_module(path: str):
    name = os.path.split(path)[-1]
    plugin_name = name.removesuffix(".py")
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    if spec and spec.loader:
        spec.loader.exec_module(module)
    plugin: PluginABC = getattr(module, plugin_name)
    plugins.append(plugin)


abs_path = os.path.abspath(__file__)
dirpath = os.path.dirname(abs_path)

plugins = []

for filename in os.listdir(dirpath):
    if (filename != "PluginABC.py"
            and not filename.startswith(".")
            and not filename.startswith("__")
            and filename.endswith(".py")):
        register_module(os.path.join(dirpath, filename))

plugins.sort(key=lambda x: x.plugin_name)
