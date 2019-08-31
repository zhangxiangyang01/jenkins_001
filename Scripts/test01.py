import pytest

class Test01():
    def detup(self):
        print("setup执行")
    def teardown(self):
        print("teardown执行")

    def test001(self):
        print("test001执行")

    def test002(self):
        print("test001执行")

if __name__ == '__main__':
    pytest.main("-s test01.py")



