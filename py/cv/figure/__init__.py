# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def load_font(fontsize=15):
    return ImageFont.truetype("C:\\Windows\\Fonts\\Arial.TTF", fontsize)


class Figure:
    """
    Figure process for paper
        1. add label
        2. arrange pics
    position and dimension are percent except resize, corp, size
    """

    def __init__(self, fimg=None):
        if fimg is None:
            self.__image__ = None
        elif isinstance(fimg, str):
            self.__image__ = Image.open(fimg)
        elif isinstance(fimg, Image.Image):
            self.__image__ = fimg
        self.image = self.__image__

    @staticmethod
    def new(fig_size, fill=(255, 255, 255), mode='RGB'):
        return Figure(Image.new(mode=mode, size=fig_size, color=fill))

    @property
    def size(self):
        return self.image.size

    def add_text(self, label, pos=(5, 5), color=(0, 0, 0), fontsize=10.0):
        draw = ImageDraw.Draw(self.image)
        w, h = self.size
        fontsize = int(h * fontsize / 100)
        draw.text(xy=pos, text=label, fill=color, font=load_font(fontsize))
        return self

    def add_line(self, start, end, color=(255, 255, 255), width=1.0):
        draw = ImageDraw.Draw(self.image)
        w, h = self.size
        width = int(h * width / 100)
        x, y = start
        start = (int(x * w / 100), int(y * h / 100))
        x, y = end
        end = (int(x * w / 100), int(y * h / 100))
        draw.line([start, end], color, width)
        return self

    def add_rect(self, upper_left, bottom_rigth, color=(255, 255, 255)):
        draw = ImageDraw.Draw(self.image)
        upper_left = self.percent2points(upper_left)
        bottom_rigth = self.percent2points(bottom_rigth)
        draw.rectangle(xy=[upper_left, bottom_rigth], fill=color)
        return self

    def add_scale(self, text, pos, size, padding=(1, 1, 1, 1), background=(255, 255, 255), foreground=(0, 0, 0),
                  line_width=1,
                  transparent=False, vspacing=1.0):
        if not transparent:
            self.add_rect(upper_left=pos, bottom_rigth=(pos[0] + size[0], pos[1] + size[1]), color=background)
        line_start = (pos[0] + padding[2], pos[1] + size[1] - padding[1] - line_width / 2.0)
        line_end = (pos[0] + size[0] - padding[3], pos[1] + size[1] - padding[1] - line_width / 2.0)
        self.add_line(start=line_start, end=line_end, color=foreground, width=1.0)
        w, h = self.size
        font_size = int((size[1] - padding[0] - padding[1] - line_width - vspacing) * h / 100)
        draw = ImageDraw.Draw(self.image)
        t_w, t_h = draw.textsize(text=text, font=load_font(font_size))
        t_pos = self.percent2points(pos)
        t_size = self.percent2points(size)
        t_pos = (int(t_pos[0] + t_size[0] / 2 - t_w / 2), int(t_pos[1] + padding[0] * h / 100))
        draw.text(xy=t_pos, text=text, fill=foreground, font=load_font(font_size))
        return self

    def resize(self, fig_size):
        self.image = self.image.resize(fig_size)
        return self

    def show(self):
        self.image.show()

    def save(self, fname):
        self.image.save(fname)

    def __del__(self):
        self.image.close()

    def percent2points(self, percent):
        w, h = self.size
        x, y = percent
        return int(x * w / 100), int(y * h / 100)

    @staticmethod
    def group(images, cols=3, spacing=(10, 10), fig_size=(500, 500), labels=None, label_pos=(5, 5), label_color=(0, 0, 0),
              fontsize=8.0):
        if labels is not None:
            for img, label in zip(images, labels):
                img.resize(fig_size).add_text(label, label_pos, label_color, fontsize)
        width = int(cols * fig_size[0] + cols * spacing[0] - spacing[0])
        rows = np.ceil(len(images) / cols)
        height = int(rows * fig_size[1] + (rows - 1) * spacing[1])
        image = Figure.new((width, height))
        for i in range(len(images)):
            row = np.floor(i / cols)
            col = i - row * cols
            pos = (int(col * spacing[0] + col * fig_size[0]), int(row * spacing[1] + row * fig_size[1]))
            pos = (pos[0], pos[1], pos[0] + fig_size[0], pos[1] + fig_size[1])
            image.paste(images[i], pos)
        return image

    def paste(self, img, pos):
        self.image.paste(img.image, pos)
        return self

    def __copy__(self):
        figure = Figure.new(self.size)
        figure.paste(self, (0,0,self.size[0], self.size[1]))
        return figure


if __name__ == '__main__':
    labels = ['(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)']

    figs = []
    for i in range(10):
        figs.append(Figure(r'C:\Users\gc_zc\Desktop\pyprj\data\A.png') \
                    .add_scale(text=labels[i] + ' figure', pos=(25, 45), size=(50, 15)))

    Figure.group(figs,cols=5, labels=labels, spacing=(2, 2)).show()
