import os
import json
import yaml

class Configuration:
    """ Read yaml/json and create Dict"""
    def __init__(self, filepath):
        self.filepath = filepath
        self._config = {}
        self.load_config()

    def load_config(self):
        if not os.path.isfile(self.filepath):
            print(f"Error: Config file '{self.filepath}' not found.")
            return

        _, ext = os.path.splitext(self.filepath.lower()) #>> Check the extension, support yaml and json
        try:
            with open(self.filepath, 'r') as f:
                if ext in ['.json']:
                    self._config = json.load(f)
                elif ext in ['.yaml', '.yml']:
                    self._config = yaml.safe_load(f) or {}
                else:
                    print(f"Unsupported config file extension: '{ext}'")
                    return

                for key, value in self._config.items():
                    setattr(self, key, value)

        except (json.JSONDecodeError, yaml.YAMLError) as e:
            print(f"Error parsing config file '{self.filepath}': {e}")
        except Exception as e:
            print(f"Unexpected error reading config file: {e}")

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __repr__(self):
        return yaml.dump(self._config, default_flow_style=False)



