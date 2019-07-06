import hashlib
import json

SALT = 'jiayanparams'

# 针对post请求的md5加密方法


def post_md5_sign(params):
    # 实例化md5对象
    md5Obj = hashlib.md5()
    # 排序
    data = json.dumps(params, sort_keys=True)
    # 转为字典
    dict = json.loads(data)
    # 以key=value的形式放入数组
    List = []
    for key, value in dict.items():
        item = key + "=" + value
        List.append(item)
    # 最终加盐的字符串
    list_join = "&".join(List)
    salt_sign_str = SALT + list_join

    # 写入要加密的字节
    md5Obj.update(salt_sign_str.encode('utf-8'))
    # 获取密文
    sign = md5Obj.hexdigest()
    # 添加sign
    dict["sign"] = sign
    return dict


def md5(s):
    m = hashlib.md5(s.encode())
    return m.hexdigest()


# 另外一种sign签名实现方法
def sign(params):
    if isinstance(params, str):
        url = params
        url_without_params = url.split('?')[0]
        _sign = md5(f"{SALT}{url_without_params}")
        if "?" in url:
            return f"{url}&sign={_sign}"
        else:
            return f"{url}?sign={_sign}"
    else:
        js = params
        sorted_json = json.loads(json.dumps(js, sort_keys=True))
        json_arr = []
        for key in sorted_json:
            val = sorted_json.get(key)
            json_arr.append(f"{key}={val}")
        _sign = md5(SALT + '&'.join(json_arr))
        js['sign'] = _sign
        return js
