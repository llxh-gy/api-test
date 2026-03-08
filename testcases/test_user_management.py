import allure
import pytest
from utils.api_util import api_request
from utils.log_util import logger

@allure.feature("用户管理模块")
class TestUserManagement:

    @allure.story("创建用户")
    @allure.title("测试创建新用户成功")
    def test_create_user(self, test_data):
        data = test_data["create_user"]
        with allure.step("发送 POST 请求创建用户"):
            resp = api_request.post("/api/users", json=data)
        with allure.step("校验响应状态码"):
            assert resp.status_code == 201
        with allure.step("校验响应内容"):
            resp_json = resp.json()
            assert resp_json["name"] == data["name"]
            assert resp_json["job"] == data["job"]
            assert "id" in resp_json
            assert "createdAt" in resp_json
        logger.info("创建用户成功")

    @allure.story("查询用户")
    @allure.title("测试查询单个用户成功")
    def test_get_single_user(self):
        user_id = 2
        with allure.step(f"发送 GET 请求查询用户 {user_id}"):
            resp = api_request.get(f"/api/users/{user_id}")
        with allure.step("校验响应状态码"):
            assert resp.status_code == 200
        with allure.step("校验响应数据"):
            resp_json = resp.json()
            assert resp_json["data"]["id"] == user_id
            assert "email" in resp_json["data"]
        logger.info(f"查询用户 {user_id} 成功")

    @allure.story("查询用户")
    @allure.title("测试查询不存在的用户返回404")
    def test_get_user_not_found(self, test_data):
        user_id = test_data["invalid_user_id"]
        with allure.step(f"发送 GET 请求查询不存在的用户 {user_id}"):
            resp = api_request.get(f"/api/users/{user_id}")
        with allure.step("校验响应状态码为404"):
            assert resp.status_code == 404
        logger.info(f"查询不存在用户 {user_id} 返回404，符合预期")

    @allure.story("更新用户")
    @allure.title("测试更新用户信息成功")
    def test_update_user(self, test_data):
        user_id = 2
        data = test_data["update_user"]
        with allure.step("发送 PUT 请求更新用户"):
            resp = api_request.put(f"/api/users/{user_id}", json=data)
        with allure.step("校验响应状态码"):
            assert resp.status_code == 200
        with allure.step("校验响应数据"):
            resp_json = resp.json()
            assert resp_json["name"] == data["name"]
            assert resp_json["job"] == data["job"]
            assert "updatedAt" in resp_json
        logger.info(f"更新用户 {user_id} 成功")

    @allure.story("删除用户")
    @allure.title("测试删除用户成功")
    def test_delete_user(self):
        user_id = 2
        with allure.step(f"发送 DELETE 请求删除用户 {user_id}"):
            resp = api_request.delete(f"/api/users/{user_id}")
        with allure.step("校验响应状态码为204"):
            assert resp.status_code == 204
        logger.info(f"删除用户 {user_id} 成功")