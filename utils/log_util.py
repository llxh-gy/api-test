import sys
from loguru import logger

def setup_logger():
    logger.remove()  # 移除默认控制台输出
    # 添加控制台输出，带颜色
    logger.add(sys.stdout, level="INFO", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}")
    # 添加文件输出，自动滚动
    logger.add("logs/api_test_{time}.log", level="DEBUG", rotation="10 MB", retention="30 days", format="{time} | {level} | {message}")
    return logger

# 使用单例模式，直接导入使用
logger = setup_logger()