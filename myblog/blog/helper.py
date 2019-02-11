import hashlib

from myblog.settings import SECRET_KEY


def set_password(password):
    # 密码加密
    for _ in range(1000):
        pwd = "{}{}".format(password, SECRET_KEY)
        h = hashlib.md5(pwd.encode('utf-8'))
        password = h.hexdigest()
    return password
