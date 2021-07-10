import pytest
from code.testOS import Calculator
import  logging
import  yaml

@pytest.fixture(scope="class")
def setupClass():
    logging.info("class-->开始")
    yield Calculator()
    logging.info("class-->结束")

@pytest.fixture()
def setUp():
    logging.info("开始计算")
    yield ("用例开始执行")
    logging.info("结束计算")
# 将文件流转成python对象,获取yaml的测试数据
def get_calc_data():
    with open("../data/data1.yaml") as f:
        datas = yaml.safe_load(f)
    return (datas["int"],datas["float"])

#request是pytest的内置fixture
@pytest.fixture(params=get_calc_data()[0])
def get_datas(request):
    return request.param

#request是pytest的内置fixture
@pytest.fixture(params=get_calc_data()[1])
def get_datas1(request):
    return request.param

