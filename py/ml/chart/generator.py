import json
from chart.defines import *
import matplotlib.pyplot as plt


class Generator:
    """
    load from figure.json
    """

    def __init__(self):
        self.__charts = []
        self.__data = {}
        self.__styles = {}

    def load(self, define_file):
        if os.path.exists(define_file):
            self.__load(define_file)
        else:
            raise Exception(define_file + " not found")

    def __load(self, define_file):
        msg = json.loads(filter_json_annotation(define_file))
        for inc in msg['include']:
            fp = get_real_path(os.path.dirname(define_file), inc)
            self.__load(fp)

        for d in msg['data']:
            check_keys_and_raise(d, 'type')
            self.__parse_data(d, d['type'], os.path.dirname(define_file))

        for chart in msg['chart']:
            check_keys_and_raise(chart, 'type')
            self.__charts.append(chart)

    def __parse_data(self, data, data_type, rel_dir):
        if data_type == DataType.XRD:
            self.__parse_xrd_file(data, rel_dir)
        elif data_type == DataType.TENSION:
            self.__parse_tension_file(data, rel_dir)
        else:
            raise Exception("unknown data type file : " + data_type)

    def __parse_xrd_file(self, data, rel_dir):
        check_keys_and_raise(data, 'id', 'file', 'description')
        fp = get_real_path(rel_dir, data['file'])
        tdata = load_col_data_from_txt(fname=fp, skiprows=1, cnames=['theta', 'I'])
        tdata['type'] = DataType.XRD
        tdata['description'] = data['description']
        tdata['file'] = fp
        self.__data[data['id']] = tdata

    def __parse_tension_file(self, data, rel_dir):
        pass

    def draw(self):
        for chart in self.__charts:
            reset_mpl_styles()
            check_keys_and_raise(chart, 'type')
            chart_type = chart['type']
            if chart_type == ChartType.PLOT:
                self.__draw_plot_chart(chart)
            else:
                raise Exception("unknown chart type: " + str(chart_type))

    def __draw_plot_chart(self, chart):
        check_keys_and_raise(chart, 'id', 'type')
        reset_mpl_styles()  # 重置所有样式
        height = 8
        width = 10
        if check_key(chart, 'image-width', 'image-height'):
            height = chart['image-height']
            width = chart['image-width']
        fig = plt.figure(figsize=(width, height))
        ax = fig.add_subplot(111)
        if check_key(chart, 'styles'):
            apply_mpl_styles(chart['styles'])
        if check_key(chart, 'xlim'):
            ax.set_xlim(chart['xlim'][0], chart['xlim'][1])
        if check_key(chart, 'ylim'):
            ax.set_ylim(chart['ylim'][0], chart['ylim'][1])
        if check_key(chart, 'xlabel'):
            ax.set_xlabel(chart['xlabel'])
        if check_key(chart, 'ylabel'):
            ax.set_ylabel(chart['ylabel'])
        if check_key(chart, 'title'):
            ax.set_title(chart['title'])

        check_keys_and_raise(chart, 'series')
        for series in chart['series']:
            self.__draw_plot(series, ax)

        if check_key(chart, 'fname'):
            fig.savefig(chart['fname'])
        else:
            fig.show()

        if check_key(chart, 'styles'):
            reset_mpl_styles(chart['styles'])

    def __draw_plot(self, series, ax):
        _x = []
        _y = []
        if check_key(series, 'data'):
            check_keys_and_raise(series['data'], 'x', 'y')
            _x = series['data']['x']
            _y = series['data']['y']
            if not type(_x) is list and not type(_y) is list:
                raise Exception("data should be list type")
        elif check_key(series, 'data-ref'):
            _x, _y = self.__query_plot_data(series)
        if check_key(series, 'styles'):  # 应用样式
            apply_mpl_styles(series['styles'])

        if check_key(series, 'label'):
            ax.plot(_x, _y, label=series['label'])
        else:
            ax.plot(_x, _y)

        if check_key(series, 'styles'):  # 重置样式
            reset_mpl_styles(series['styles'])

    def __query_plot_data(self, series):
        _x = []
        _y = []
        ref = series['data-ref']
        if self.__data.__contains__(ref):
            data = self.__data.get(ref)
        else:
            raise Exception("no data's id is " + ref)
        check_keys_and_raise(data, 'type')
        d_type = data['type']
        if d_type == DataType.XRD:
            _x = data['theta'].copy()
            _y = data['I'].copy()

        if check_type(_x, list, np.ndarray) and check_type(_y, list, np.ndarray):
            return _x, _y
        else:
            raise Exception('list type is expected')
