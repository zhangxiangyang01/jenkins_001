import pytest

class Test03():
    @pytest.mark.run(order=4)
    def test_post(self):
        print("post")

    @pytest.mark.run(order=3)
    def test_delete(self):
        print("delete")

    @pytest.mark.run(order=2)
    def test_put(self):
        print("put")

    @pytest.mark.run(order=1)
    def test_get(self):
        print("get")