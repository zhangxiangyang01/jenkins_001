import pytest

class Test03():

    def test_post(self):
        print("post")
        return False

    @pytest.mark.skipif(test_post=False,reason="条件成立，跳过此方法")
    def test_delete(self):
        print("delete")

    @pytest.mark.xfail(test_post=False,reason="条件成立，跳过此方法")
    def test_put(self):
        print("put")

    def test_get(self):
        print("get")