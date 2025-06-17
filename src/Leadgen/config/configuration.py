from Leadgen.constants import *
from Leadgen.utils.common import read_yaml, create_directories
from Leadgen.entity.config_entity import (BasicuserConfig
                                          )

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH,
        prompt_filepath = PROMPT_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        self.prompt = read_yaml(prompt_filepath)


        create_directories([self.config.artifacts_root])