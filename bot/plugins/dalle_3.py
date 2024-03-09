from typing import Dict

from .plugin import Plugin


class DallE3(Plugin):

    def get_source_name(self) -> str:
        return "DallE3"

    def get_spec(self) -> [Dict]:
        pass

    def execute(self, function_name, helper, **kwargs) -> Dict:
        pass
