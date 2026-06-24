import json
import os


class PluginManager:

    def __init__(self):

        self.plugin_file = "plugins.json"

        self.plugins = {}

        self.load_plugins()

    def load_plugins(self):

        if os.path.exists(
            self.plugin_file
        ):

            with open(
                self.plugin_file,
                "r",
                encoding="utf-8"
            ) as file:

                self.plugins = json.load(
                    file
                )

    def save_plugins(self):

        with open(
            self.plugin_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.plugins,
                file,
                indent=4
            )

    def create_plugin(

        self,

        name,

        response

    ):

        self.plugins[name] = {

            "response": response,

            "enabled": True

        }

        self.save_plugins()

    def enable_plugin(

        self,

        name

    ):

        if name in self.plugins:

            self.plugins[name][
                "enabled"
            ] = True

            self.save_plugins()

    def disable_plugin(

        self,

        name

    ):

        if name in self.plugins:

            self.plugins[name][
                "enabled"
            ] = False

            self.save_plugins()

    def run_plugin(

        self,

        name

    ):

        if name not in self.plugins:

            return "Plugin Not Found"

        if not self.plugins[name][
            "enabled"
        ]:

            return "Plugin Disabled"

        return self.plugins[name][
            "response"
        ]

    def list_plugins(self):

        return self.plugins