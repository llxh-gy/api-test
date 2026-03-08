import requests
from utils.log_util import logger
from utils.config_util import config


class APIRequest:
    def __init__(self):
        self.base_url = config.get('api', 'base_url')
        self.timeout = config.getint('api', 'timeout')
        self.session = requests.Session()

        # 从配置文件读取 API Key
        api_key = config.get('api', 'api_key', fallback=None)
        if api_key:
            self.session.headers.update({
                'x-api-key': api_key,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            logger.info("已添加 API Key 认证头")
        else:
            logger.warning("未配置 API Key，请求可能失败")

        # 其他默认头
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

    def request(self, method, url, **kwargs):
        full_url = self.base_url + url
        kwargs.setdefault('timeout', self.timeout)
        logger.info(f"请求 {method.upper()} {full_url} - 参数: {kwargs}")

        try:
            resp = self.session.request(method, full_url, **kwargs)
            logger.info(f"响应状态码: {resp.status_code}")
            logger.debug(f"响应内容: {resp.text}")
            return resp
        except Exception as e:
            logger.error(f"请求异常: {e}")
            raise

    def get(self, url, params=None, **kwargs):
        return self.request('get', url, params=params, **kwargs)

    def post(self, url, json=None, data=None, **kwargs):
        return self.request('post', url, json=json, data=data, **kwargs)

    def put(self, url, json=None, data=None, **kwargs):
        return self.request('put', url, json=json, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('delete', url, **kwargs)

# 实例化供测试使用
api_request = APIRequest()