import os
import pytest
import shutil

if __name__ == "__main__":
    # 清空旧的 allure 结果
    allure_results_dir = "./reports/allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)

    # 运行测试，生成 allure 结果
    pytest.main(["-v", "-s", "--alluredir", allure_results_dir, "testcases/"])

    # 生成 allure 报告
    os.system(f"allure generate {allure_results_dir} -o ./reports/allure-report --clean")
    print("Allure 报告已生成在 ./reports/allure-report 目录")