import pytest
import json
from utils.log_util import logger
from utils.api_util import api_request

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    logger.info("========== 测试会话开始 ==========")
    yield
    logger.info("========== 测试会话结束 ==========")

@pytest.fixture
def test_data():
    with open("data/users_data.json", "r", encoding="utf-8") as f:
        return json.load(f)