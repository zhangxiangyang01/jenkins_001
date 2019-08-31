# import pytest
#
# class Test07():
#     @pytest.mark.parametrize("username,psd,tel",[("小红","11111",183),("小绿","22222","159")])
#     def test_login(self,username,psd,tel):
#         print("用户名为：",username)
#         print("密码为：",psd)
#         print("电话为：",tel)

# -------------------------------------------------------------------------
import pytest

def get_data():
    return [("xiao","111","183"),("da","222","159")]

class Test07():
    @pytest.mark.parametrize("user,psd,tel",get_data())
    def test_login(self,user,psd,tel):
        print("用户名为：",user)
        print("密码为：",psd)
        print("电话为：",tel)
