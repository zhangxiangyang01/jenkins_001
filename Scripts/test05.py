# import pytest
#
# @pytest.fixture(autouse=True)
# def before():  ---------括号内要 删除 self
#     print("before")
#
# # @pytest.mark.usefixtures("before")
#
# class Test04():
#     # @pytest.fixture()
#     # def before(self):
#     #     print("before")
#
#     def test_post(self):
#         print("增")
#
# # ------通过参数形式
#     # def test_delete(self,before):
#     #     print("删")
#
# #-----通过函数形式
#     # @pytest.mark.usefixtures("before")
#     # def test_put(self):
#     #     print("改")
#
#     def test_get(self):
#         print("查")

# -----------------------------------------------------------------
import pytest


@pytest.fixture(autouse=True)
def before():
    print("before")

# @pytest.mark.usefixtures("before")

class Test():

    def test_post(self):
        print("增")

    # @pytest.mark.usefixtures("before")
    def test_delete(self):
        print("删")

    def test_put(self):
        print("改")

    # def test_get(self):
    #     print("查")