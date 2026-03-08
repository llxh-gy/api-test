import configparser
import os

class ConfigUtil:
    def __init__(self, config_path="config/config.ini"):
        self.config = configparser.ConfigParser()
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
        self.config.read(config_path, encoding='utf-8')

    def get(self, section, option, fallback=None):
        """获取配置项，如果不存在则返回 fallback 值"""
        return self.config.get(section, option, fallback=fallback)

    def getint(self, section, option):
        return self.config.getint(section, option)

# 全局配置对象
config = ConfigUtil()