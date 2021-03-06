# -*- coding: utf-8 -*-

import json

from chart.utlis import *
import matplotlib.pyplot as plt
from chart.pipeline import pipeline
from chart.constant import *


class Generator:
    """
    load from figure.json
    """

    def __init__(self):
        self.__charts = []
        self.__data = {}
        self.__style = {}

    def load(self, define_file):
        if os.path.exists(define_file):
            self.__load(os.path.abspath(define_file))
        else:
            raise Exception(define_file + " not found")

    def __load(self, define_file):
        print("load... ", define_file)
        msg = json.loads(filter_json_annotation(define_file))
        if check_key(msg, 'include'):
            for inc in msg['include']:
                fp = get_real_path(os.path.dirname(define_file), inc)
                self.__load(fp)

        if check_key(msg, 'data'):
            for d in msg['data']:
                check_keys_and_raise(d, 'type')
                self.__parse_data(d, d['type'], os.path.dirname(define_file))

        if check_key(msg, 'chart'):
            for chart in msg['chart']:
                self.__charts.append(chart)

    def __parse_data(self, data, data_type, rel_dir):
        if data_type == DataType.XRD:
            self.__parse_xrd_file(data, rel_dir)
        elif data_type == DataType.TENSION:
            self.__parse_tension_file(data, rel_dir)
        elif data_type == DataType.XRD_PATTERN:
            self.__parse_xrd_pattern_data(data)
        else:
            raise Exception("unknown data type file : " + data_type)

    def __parse_xrd_pattern_data(self, data):
        check_keys_and_raise(data, 'peak')
        if not check_type(data['peak'], dict):
            raise Exception('peak of xrd pattern should be a dict')
        peaks = dict(data['peak'])
        if not check_key(self.__data, 'xrd_pattern'):
            self.__data['xrd_pattern'] = {}
        for key in peaks.keys():
            if not check_type(peaks[key], list):
                raise Exception('peak should be a list')
            self.__data['xrd_pattern'][key] = peaks.get(key)

    def __parse_xrd_file(self, data, rel_dir):
        check_keys_and_raise(data, 'id', 'file', 'description')
        fp = get_real_path(rel_dir, data['file'])
        t_data = load_col_data_from_txt(fname=fp, skiprows=1, cnames=['theta', 'I'])
        t_data['type'] = DataType.XRD
        t_data['description'] = data['description']
        t_data['file'] = fp
        self.__data[data['id']] = t_data

    def __parse_tension_file(self, data, rel_dir):
        pass

    def draw(self):
        for chart in self.__charts:
            reset_mpl_style()
            if check_key(chart, 'style'):
                apply_mpl_style(chart['style'])

            self.set_figure_size(chart)
            self.apply_chart_setting(chart)

            check_keys_and_raise(chart, 'series')
            for series in chart['series']:
                self.draw_chart_series(series)

            if check_key(chart, 'legend') and chart['legend']:
                ncols = 1
                if check_key(chart, 'legend_ncol'):
                    ncols = chart['legend_ncol']
                plt.legend(ncol=ncols)

            if check_key(chart, 'fname'):
                plt.savefig(chart['fname'])
            else:
                plt.show()

            plt.close()
            if check_key(chart, 'style'):
                reset_mpl_style(chart['style'])

    @staticmethod
    def set_figure_size(chart):
        height = 8
        width = 10
        if check_key(chart, 'image-width', 'image-height'):
            height = chart['image-height']
            width = chart['image-width']
        plt.figure(figsize=(width, height))

    @staticmethod
    def apply_chart_setting(chart):
        if check_key(chart, 'xlim'):
            plt.xlim(chart['xlim'][0], chart['xlim'][1])
        if check_key(chart, 'ylim'):
            plt.ylim(chart['ylim'][0], chart['ylim'][1])
        if check_key(chart, 'xlabel'):
            plt.xlabel(chart['xlabel'])
        if check_key(chart, 'ylabel'):
            plt.ylabel(chart['ylabel'])
        if check_key(chart, 'title'):
            plt.title(chart['title'])

    def draw_chart_series(self, series):
        if check_key(series, 'subplot'):
            plt.subplot(series['subplot'])
        if check_key(series, 'style'):
            apply_mpl_style(series['style'])

        check_keys_and_raise(series, 'type', 'data')
        chart_type = series['type']
        chart_data = series['data']
        if chart_type == ChartType.PLOT:
            self.plot(chart_data)
        elif chart_type == ChartType.XRD_PATTERN:
            self.xrd_pattern(chart_data)
        else:
            raise Exception('unknown chart type')

        if check_key(series, 'style'):
            reset_mpl_style(series['style'])

    def plot(self, chart_data):
        check_keys_and_raise(chart_data, 'x', 'y')
        x = chart_data['x']
        y = chart_data['y']
        if isinstance(x, str):
            x = self.query_data(x)
        if isinstance(y, str):
            y = self.query_data(y)

        if check_key(chart_data, 'x_pipeline'):
            for pipe in chart_data['x_pipeline'].split('|'):
                if not pipe.isspace() and len(pipe) > 2:
                    x = pipeline(x, pipe.strip())
        if check_key(chart_data, 'y_pipeline'):
            for pipe in chart_data['y_pipeline'].split('|'):
                if not pipe.isspace() and len(pipe) > 2:
                    y = pipeline(y, pipe.strip())

        if check_key(chart_data, 'label'):
            plt.plot(x, y, label=chart_data['label'])
        else:
            plt.plot(x, y)

    def query_data(self, data_key):
        dot_index = data_key.index('.')
        d_key = data_key[0:dot_index]
        d_attr = data_key[dot_index + 1:]
        if self.__data.__contains__(d_key) and self.__data[d_key].__contains__(d_attr):
            return self.__data[d_key][d_attr]
        else:
            raise Exception(data_key + " is not found")

    def xrd_pattern(self, chart_data):
        check_keys_and_raise(chart_data, 'x', 'y', 'peak')
        x = chart_data['x']
        y = chart_data['y']
        peak = chart_data['peak']
        if isinstance(x, str):
            x = self.query_data(x)
        if isinstance(y, str):
            y = self.query_data(y)
        if isinstance(peak, str):
            peak = self.query_data(peak)

        if not isinstance(peak, list):
            raise Exception('peak should be a list')
        peak.sort()
        x, y = find_peak(x, y, peak)
        y = np.array(y)

        if check_key(chart_data, 'offset') and check_type(chart_data['offset'], float, int):
            y = y + chart_data['offset']

        if check_key(chart_data, 'label'):
            plt.plot(x, y, label=chart_data['label'])
        else:
            plt.plot(x, y)
