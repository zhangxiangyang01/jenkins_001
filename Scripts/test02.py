import pytest

class Test02():
    def detup(self):
        print("setup执行")
    def teardown(self):
        print("teardown执行")

    def test111(self):
        print("test001执行")

    def test222(self):
        print("test001执行")

if __name__ == '__main__':
    pytest.main("-s test01.py")



