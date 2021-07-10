import logging
import allure
import pytest

#打印获得的数据
# def test_get_datas(get_datas):
#     print(get_datas)

class TestCalculator:
    @pytest.mark.run(order=2)
    def test_add_int(self, get_datas, setupClass,setUp):
        logging.info(f"用例test_add_int : 开始执行{get_datas[0]}_{get_datas[1]}")
        assert get_datas[2] == setupClass.add(get_datas[0], get_datas[1])

    @pytest.mark.run(order=1)
    @allure.title("用例test_add_float标题 get_datas1[0]_get_datas1[1]")
    def test_add_float(self, get_datas1, setupClass,setUp):
        with allure.step("第一步---》开始断言"):
            logging.info(f"用例test_add_float : 开始执行{get_datas1[0]}_{get_datas1[1]}")
            assert get_datas1[2] == round(setupClass.add(get_datas1[0], get_datas1[1]), 1)
        with allure.step("第二步---》开始结束"):
            pass