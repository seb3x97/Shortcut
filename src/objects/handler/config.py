#---------- Locals ----------#

import src.utils.utils as utils
import src.utils.paths as paths
from src.objects.configs.custom import ConfigCustom

# Class Config
class Config:
    custom: ConfigCustom

    def __init__(self) -> None:

        text = utils.read_file_content(paths.FILE_CONFIG_CUSTOM)
        json = utils.convert_text_to_json_object(text)

        self.custom = ConfigCustom(**json)

    def save_config_custom(self):
        text = utils.convert_object_to_json_text(self.custom)
        utils.write_file_content(paths.FILE_CONFIG_CUSTOM, text)