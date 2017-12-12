import matplotlib as mpl
import os
import numpy as np

eps = 0.00000001


def list2array(o):
    if type(o) is np.ndarray:
        return o
    if type(o) is list:
        return np.array(o)
    raise Exception('list or ndarray is expected')


def check_keys_and_raise(msg, *keys):
    if isinstance(msg, dict):
        for k in keys:
            if not msg.__contains__(k):
                raise Exception("key " + str(k) + " not exists")
    else:
        raise Exception('illegal params, dict is needed')


def check_style(style_key, style_value):
    """
    检查样式是否合法：style_key存在，style_value也与默认值类型相同
    :param style_key:
    :param style_value:
    :return:
    """
    if mpl.rcParams.__contains__(style_key):
        if type(style_value) == mpl.rcParamsDefault[style_key]:
            return True
        else:
            print(style_key, "default type is ", type(mpl.rcParamsDefault[style_key]))
            return False
    else:
        print(style_key, "not exists")
        return False


def apply_mpl_style(style):
    """
    设置matplotlib样式
    :param style: 自定义样式
    :return: 无
    """
    if isinstance(style, dict):
        mpl.rcParams.update(style)
    else:
        raise Exception('illegal params, dict is needed')


def check_key(params, *keys):
    """
    检查params中是否包含key，需要包含所有的key
    :param params: dict对象
    :param keys: 需要检测的键值
    :return: 是否包含key
    """
    if isinstance(params, dict):
        for key in keys:
            if not params.__contains__(key):
                return False
        return True
    else:
        raise Exception('illegal params, dict is needed')


def reset_mpl_style(style=None):
    """
    重置mpl样式
    :param style: if None，重置所有样式
    :return: 无
    """
    if style is None:
        mpl.rcdefaults()
    elif isinstance(style, dict):
        for key in style.keys():
            if mpl.rcParams.__contains__(key):
                mpl.rcParams[key] = mpl.rcParamsDefault[key]
    else:
        raise Exception('illegal params, dict is needed')


def check_type(obj, *d_types):
    """
    只要有一个类型满足即可
    :param obj:
    :param d_types:
    :return:
    """
    for d_type in d_types:
        if isinstance(obj, d_type):
            return True
    return False


def get_real_path(ref_dir, rel_file):
    """
    获得相对于ref_dir的路径
    :param ref_dir:  参考路径
    :param rel_file:  相对路径
    :return: 目标路径
    """
    return os.path.join(ref_dir, rel_file).replace("\\", "/").replace("//", "/")


def filter_json_annotation(json_file):
    fp = open(json_file)
    str_flag = False
    note_flag = False
    json_str = ''
    text = fp.read()
    i = 0
    while i < len(text):
        c = text[i]
        if c == '"':
            if not note_flag:
                str_flag = not str_flag
                json_str = json_str + c
        elif c == '\n':
            note_flag = False
        elif c == '/':
            if not str_flag and len(text) > i + 1 and text[i + 1] == '/':
                i = i + 1
                note_flag = True
            else:
                json_str = json_str + c
        elif c == ' ':
            if str_flag:
                json_str = json_str + c
        elif not note_flag:
            json_str = json_str + c
        i = i + 1
    return json_str


def load_col_data_from_txt(fname, skiprows=0, comments='#', delimiter=None, cnames=None):
    d = np.loadtxt(fname=fname, delimiter=delimiter, skiprows=skiprows, comments=comments)
    if cnames is None or len(cnames) == 0:
        return {'_array': d}
    if len(d.shape) == 1:
        if len(cnames) == 1:
            return {cnames[0]: d}
        else:
            raise Exception('too many col names, only one dimension')
    elif len(d.shape) == 2:
        if d.shape[1] >= len(cnames):
            i = 0
            data = {}
            for name in cnames:
                data[name] = d[:, i]
                i = i + 1
            return data
        else:
            raise Exception('too many col names')


def max_in_range(y, x, flag):
    xl = 0
    if isinstance(x, np.ndarray):
        xl = x.shape[0]
    elif isinstance(x, list):
        xl = len(x)
    _y = []
    for i in range(xl):
        if flag - 1 < x[i] < flag + 1:
            _y.append(y[i])
    return np.max(_y)


def skip_theta(x, x_i):
    flag = x[x_i]
    xl = 0
    if isinstance(x, np.ndarray):
        xl = x.shape[0]
    elif isinstance(x, list):
        xl = len(x)
    for i in range(x_i, xl):
        if x[i] > flag + 1:
            return i
    return len(x)


def find_peak(x, y, peak):
    _I = []
    _p = []
    p_i = 0
    x_i = 0
    if isinstance(x, list):
        x = np.array(x)
    while x_i < x.shape[0] and p_i < len(peak):
        flag = peak[p_i]
        if flag <= x[x_i]:
            _I.append(max_in_range(y, x, flag))
            _p.append(flag)
            x_i = skip_theta(x, x_i)
            p_i = p_i + 1
        x_i = x_i + 1

    return _p, _I
